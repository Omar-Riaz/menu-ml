import os
import csv, json
import sys
json_file = open("C:\\Users\\Omar\\Desktop\\menu ML\\cleaned datasets\\" + sys.argv[1] + ".json", "r", errors='ignore', encoding='utf8')                    #open output csv and input json files
csv_file = open("C:\\Users\\Omar\\Desktop\\menu ML\\cleaned datasets\\csv\\menu" + sys.argv[1] + ".csv", "w", newline='')
data = json.load(json_file)
output = csv.writer(csv_file, delimiter = ',')
ingredients = set()                                                                                                 #gather all unique ingredients
for key in data["menu_items"]:
    ingredients.update(data["menu_items"][key]['ingredients'])
rows = ['apiKey', 'basePrice', 'cuisines', 'description', 'foodTypes', 'name', 'restaurant'] + list(ingredients)
output.writerow(rows)  # header row
for key in data["menu_items"]:
    item = data["menu_items"][key]
        for cuisine in item['cuisines']:
            ingr_vals = [1 if x in item['ingredients'] else 0 for x in list(ingredients)]
            item['cuisines'] = cuisine.lower()
            item['foodTypes'] = item['foodTypes'][0]
            vals = list(item.values())
            del vals[5]
            row = map(list(vals) + ingr_vals, lambda x: unicode(x).encode('utf-8'))
            output.writerow(row)
csv_file.close()
json_file.close()
