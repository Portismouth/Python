class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000: self.tax = .15 
        else: self.tax = .12
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax
            
Car1 = Car(5000, "30mph", "Full", "40mpg")
Car2 = Car(50000, "100mph", "Full", "15mpg")
Car3 = Car(55000, "95mph", "Full", "30mpg")
Car4 = Car(45000, "30mph", "Full", "40mpg")
Car5 = Car(8000, "30mph", "Full", "40mpg")
Car6 = Car(9000, "30mph", "Full", "40mpg")

Car1.display_all()
Car2.display_all()
Car3.display_all()
Car4.display_all()
Car5.display_all()
Car6.display_all()
