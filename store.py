class Store:
    def __init__(self, name):
        self.name = name  ##so we can add more stores
        self.product_list = []

    def add_product(self, new_product):
        self.product_list.append(new_product)  ##append is the python version of push

    def inflation(self, percent_increase):


    def set_clearance(self, category, percent_discount):

    def sell_product(self, id):
        self.product_list.pop(id)
## Product name, id (need to figure out how I'm going to establish this, maybe id = <int>?) Product is established in the other
## class, then attached here


class Product:
    def __init__(self, name, price, category):
        self.name = []
        self.price = price
        self.category = category

    def print_info(self):
        print (f"Product Name:" self.name, "Category:" self.category, "Price:" self.price")

    def update_price(self, percent_change, is_increased):
        self.percent_change = 
