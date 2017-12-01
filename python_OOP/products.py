class product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self, num):
        self.price = (self.price*num)+self.price
        return self
    def return_product(self, condition):
        if condition is "defective":
            self.status = "defective"
            self.price = 0
        elif condition is "in box":
            self.status = "for sale"
        elif condition is "opened":
            self.status = "used"
            self.price = self.price-(self.price*.20)
        return self
    def display_info(self):
        print self.price
        print self.item_name
        print self.weight
        print self.brand
        print self.status
        return self
        

    
product1 = product(12, "Super Blender", "5lbs", "Oster")

product1.display_info().return_product("opened")
product1.display_info()

