class Bird:
    def __init__(self, species, sub_species=None):
        self.__class = "Aves"
        self.__species = species
        self.__subspecies = None
        self.__flying = None
        self.__color = None
        self.__size = None
        self.__beak = None
        self.__special = None
        self.__sound = None

    def set_flying(self, b):
        self.__flying = b

    def is_flying(self):
        return self.__flying

    def speciality(self):
        print("Speciality of {}:\n  Color : {}.\t Size : {}.\t Beak : {}. \t {}".format(self.__species, self.__color,
                                                                                        self.__size, self.__beak,
                                                                                        self.__special))

    def set_speciality(self, color, size, beak, special=None):
        self.__color = color
        self.__size = size
        self.__beak = beak
        self.__special = special

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        print("Sound of {} is {}".format(self.__species, self.__sound))


##########################################################################################

class Eagle(Bird):

    def __init__(self, sub_species):
        super().__init__("Eagle", sub_species)
        self.__wingspan = None
        self.set_sound("Kleek Kleek")

    def set_wingspan(self, w):
        self.__wingspan = w

    def get_wingspan(self):
        print("Wingspan is {} meters.".format(Self.__wingspan))


##########################################################################################

class Peacock(Bird):

    def __init__(self):
        super().__init__("Peacock")
        self.set_sound("Meow")
        self.__plumage = None

    def set_plumage(self, val):
        self.__plumage = val

    def is_plumage_spread(self, val):
        return self.__plumage

# //Encapsultion
class Elephant:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs
    def get_color(self):
        return (self.color)
    def get_legs(self):
        return  (self.legs)
    def set_color(self, c):
        self.color = c
    def set_legs(self, l):
        self.legs = l
class Dog:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

class Cat:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l
class Rabbit:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

class Tiger:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l
class Lion:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

class Penguin:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

class Dolphin:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

class Monkey:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

class Giraffe:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

b1 = Eagle("Bald Eagle")
b1.set_flying(True)
b1.set_speciality("Dark Brown", "Large", "Curved Yellow Beak", "White Neck")
b1.speciality()
print("\n")

p1 = Peacock()
p1.set_sound("Meow")
p1.set_speciality("Blue", "Large", "Small Beak", "Beautiful Plumage")
p1.speciality()
p1.set_plumage(True)
print("\n")


elephant = Elephant()
elephant.set_color("grey")
elephant.set_legs(4)
print("Elephant has", elephant.get_color(), "color and", elephant.get_legs(), "legs")

d = Dog()
d.set_color("Yellow")
d.set_legs(4)
print("This dog has",d.get_color(), "color and", d.get_legs(), "legs")

c = Cat()
c.set_color("Black")
c.set_legs(4)
print("This Cat has",c.get_color(), "color and", c.get_legs(), "legs")

r = Rabbit()
r.set_color("Black")
r.set_legs(4)
print("This Rabbit has",r.get_color(), "color and", r.get_legs(), "legs")

t = Tiger()
t.set_color("Yellow")
t.set_legs(4)
print("This Tiger has",t.get_color(), "color and", t.get_legs(), "legs")

l = Lion()
l.set_color("Silver")
l.set_legs(4)
print("This Lion has",l.get_color(), "color and", l.get_legs(), "legs")

p = Penguin()
p.set_color("Blue")
p.set_legs(2)
print("This Penguin has",p.get_color(), "color and", p.get_legs(), "legs")

g = Giraffe()
g.set_color("Yellow")
g.set_legs(4)
print("This Giraffe has",g.get_color(), "color and", g.get_legs(), "legs")

d = Dolphin()
d.set_color("Silver")
d.set_legs(0)
print("This Dolphin has",d.get_color(), "color and", d.get_legs(), "legs")

m = Monkey()
m.set_color("Silver")
m.set_legs(4)
print("This Monkey has",m.get_color(), "color and", m.get_legs(), "legs")



