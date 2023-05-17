import json
with open("menu_realtime\menu_realtime\menu items.json") as f:
    data = json.load(f)
    # print(data)

# Q1) Print all names of the categories in the menu ?
print(" The Menu Categories:")
for category in data:
    print(category["name"])

# Q2) Check whether menu-items present or not in the categories ?
for i in data:
    if 'menuItems' in category and category['menuItems'] is not None:
        print(f"{category['name']} category has menu items.")
    else:
        print(f"{category['name']} category does not have menu items.")

# Q3) Check whether the sub-categories present or not in the menu ?
for category in data:
    if 'subCategories' in category and category['subCategories'] is not None:
        print(f"{category['name']} category has sub-categories.")
    else:
        print(f"{category['name']} category does not have sub-categories.")


# Q4) Print all the categories and their respective items in the menu ?

for category in data:
    print(f"{category['name']} category:")
    if 'subCategories' in category and category['subCategories'] is not None:
        for sub_category in category['subCategories']:
            print(f"\t{sub_category['name']} sub-category:")
            if 'menuItems' in sub_category and sub_category['menuItems'] is not None:
                for menu_item in sub_category['menuItems']:
                    print(f"\t\t{menu_item['name']}")
            else:
                print("\t\tNo menu items in this sub-category.")
    elif 'menuItems' in category and category['menuItems'] is not None:
        for menu_item in category['menuItems']:
            print(f"\t{menu_item['name']}")
    else:
        print("\tNo sub-categories or menu items in this category.")


# Q5) Print all the sub-categories and their respective items in the menu ?
for category in data:
        if 'subCategories' in category and category['subCategories'] is not None:
            for sub_category in category['subCategories']:
                print(f"{sub_category['name']} sub-category:")
                if 'menuItems' in sub_category and sub_category['menuItems'] is not None:
                    for menu_item in sub_category['menuItems']:
                        print(f"\t{menu_item['name']}")
                else:
                    print("\tNo menu items in this sub-category.")
# Q6) Give an overview of the menu, like categories, sub-categories, and items present in it ?
for category in data:
    print(f"{category['name']} category:")
    if 'subCategories' in category and category['subCategories'] is not None:
            for sub_category in category['subCategories']:
                print(f"\t{sub_category['name']} sub-category:")
                if 'menuItems' in sub_category and sub_category['menuItems'] is not None:
                    for menu_item in sub_category['menuItems']:
                        print(f"\t\t{menu_item['name']}")
                else:
                    print("\t\tNo menu items in this sub-category.")
    else:
            print("\tNo sub-categories in this category.")
