class bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def display_info(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def ride(self):
        self.miles += 10
        print "Riding"
        return self
    def reverse(self):
        if self.miles <= 4:
            print "The bike has no miles"
        else: 
            self.miles -= 5
            print "Reversing"
        return self
            


# bike1 = bike("$200", "15 mph")
# bike2 = bike("$500", "25 mph")
bike3 = bike("$750", "35 mph")

# bike1.ride()
# bike1.ride()
# bike1.ride()
# bike1.display_info()

# bike2.ride().ride().reverse().reverse().display_info

bike3.reverse().reverse().reverse().display_info()
