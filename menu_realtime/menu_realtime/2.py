# ----2) Check whether menu-items present or not in the categories
import json
with open('menu_realtime\menu_realtime\menu items.json') as f:
    data = json.load(f)
    for i in data:
        print(i)
    