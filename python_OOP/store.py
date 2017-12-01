class store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    def add_product(self, product):
        self.products.append(product)
        return self
    def remove_product(self, product):
        self.products.remove(product)
        return self
    def inventory(self):
        print self.products
        print self.location
        print self.owner
        return self

store1 = store(["apple", "orange", "eggs", "milk"], "Downtown", "Jim")

store1.inventory()
store1.add_product("soda").inventory()
store1.remove_product("eggs").inventory()