# ----- Retail Store-----
class retailstore:
    def __init__(self,name,location,products):
        self.name = name
        self.location = location
        self.products = products

    def add_product(self,product):
        self.products.append(product)

p1 = retailstore("dmart","rajahmundry",["chocolates","cool drinks"])
print(p1.name)

p1.add_product("ice creams")
print(p1.products)


# ------ Resturant Managemant System----
class resturant:
    def __init__(self,resturantname, items,price):
        self.name = resturantname
        self.items = items
        self.item_price = price
        
    def add_items(self,item):
        self.items.append(item)
    def add_price(self,price):
        self.item_price.append(price)

c1 = resturant("spicy kitchen",["soup","chicken lollipop"],[200,340])
c1.add_items("dilkush biryani")
print(c1.item_price)
print(c1.items)

# ----- Parking Lot
class parkinglot:
    def __init__(self,id,floor,dimension):
        self.id = id
        self.floor = floor
        self. dimension = dimension
class car:
    def __init__(self,dimension,type_car):
        self.dimension = dimension
        self.type_car = type_car
class register:
    def __init__(self,car_id,solt_id,in_time,out_time):
        self.car_id = car_id
        self.solt_id = solt_id
        self.in_time = in_time
        self.out_time = out_time


# --- Resturant Management System
class resturant:
    def __init__(self,name,phoneno,address):
        self.name = name
        self.address = address
        self.ph = phoneno
        self.menu = []
    def customer(self):
        return f"{self.name},{self.phoneno}"
    def add_menu_item(self,item_name,item_price): 
        self.menu.append({"name":item_name, "price":item_price})
    def display_mem(self):
        print(f"{self.name} menu")
        for items in self.menu:
            print(f"{items['name']} : {items['price']}")
res = resturant("Spicy Mandi Resturant","durgamcheruvu","9876543876")
res.add_menu_item("chicken fried mandi", "560.7")
print(res.display_mem())