class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.health
        return self
class dog(Animal):
    def set_health(self):
        self.health = 150
        return self
    def pet_dog(self):
        self.health += 5
        return self
class dragon(Animal):
    def set_health(self):
        self.health = 170
        return self
    def fly(self):
        self.health -= 10
        return self
    def display_health(Animal):
        print Animal.health
        print "I am a dragon."

# bird = Animal("Bird", 20)
# bird.walk().walk().walk().run().run()
# bird.display_health()

# doggie = dog("Noah", 10)
# doggie.set_health().walk().walk().walk().run().run().pet_dog().display_health()

dragon_x = dragon("Parallax", 10)
dragon_x.set_health().display_health()
dragon_x.pet_dog() #returns error
doggie.fly() #returns error