#--- Q1) Print all names of the categories in the menu ?
import json
with open('menu_realtime\menu_realtime\menu items.json') as f:
    data = json.load(f)
    print(data)
    for item in data:
        if 'name' in item:
            print(item['name'])

