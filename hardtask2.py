# todo: Magic methods.
# Create a hierarchy out of birds. Implement 4 classes:
#
# class Bird with an attribute name and methods fly and walk.
# class FlyingBird with attributes name, ration, and with the same methods. ration must have a default value. Implement the method eat which will describe its typical ration.
# class NonFlyingBird with same characteristics but which obviously without attribute fly. Add the same "eat" method but with other implementation regarding the swimming bird tastes.
# class SuperBird which can do all of it: walk, fly, swim and eat. But be careful which "eat" method you inherit.
# Implement str() function call for each class.
#
# Example:
# >>> b = Bird("Any")
# >>> b.walk()
# "Any bird can walk"
#
# p = NonFlyingBird("Penguin", "fish")
# >> p.swim()
# "Penguin bird can swim"
# >>> p.fly()
# AttributeError: 'Penguin' object has no attribute 'fly'
# >>> p.eat()
# "It eats mostly fish"
#
# c = FlyingBird("Canary")
# >>> str(c)
# "Canary bird can walk and fly"
# >>> c.eat()
# "It eats mostly grains"
#
# s = SuperBird("Gull")
# >>> str(s)
# "Gull bird can walk, swim and fly"
# >>> s.eat()
# "It eats mostly fish"
# Have a look at the mro method or the attribute mro
#
# Шаблон:
# class Bird:
#     pass
#
# class FlyingBird:
#     pass
#
# class NonFlyingBird:
#     pass
#
# class SuperBird:
#     pass


# class Bird with an attribute name and methods fly and walk.
class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        pass

    def walk(self):
        print(f'{self.name} can walk')


# class FlyingBird with attributes name, ration, and with the same methods. ration must have a default value.
# Implement the method eat which will describe its typical ration.
class FlyingBird(Bird):
    def __init__(self, name, ration=None):
        super().__init__(name)
        if ration is None:
            ration = 'grains'
        self.ration = ration

    def eat(self):
        print(f'This birdie eats mostly {self.ration}')

    def __str__(self):
        return f'{self.name} can walk and fly'


# class NonFlyingBird with same characteristics but which obviously without attribute fly. Add the same "eat" method
# but with other implementation regarding the swimming bird tastes.
class NonFlyingBird(FlyingBird):
    def __init__(self, name, ration=None):
        super().__init__(name)
        if ration is None:
            ration = 'fish'
        self.ration = ration

    def fly(self):
        raise AttributeError("'NonFlyingBird' has no attribute 'fly'")

    def swim(self):
        print(f'{self.name} can swim')


class SuperBird(NonFlyingBird):
    def __init__(self, name, ration=None):
        super().__init__(name, ration)
        if ration is None:
            ration = 'fish'
        self.ration = ration

    def fly(self):
        return FlyingBird.fly()

    def __str__(self):
        return f'{self.name} can swim, walk and fly'


b = Bird("Any")
b.walk()

p = NonFlyingBird("Penguin", "fish")
p.swim()
try:
    p.fly()
except AttributeError as e:
    print(AttributeError, e)
p.eat()

c = FlyingBird("Canary")
print(str(c))
c.eat()

s = SuperBird("Gull")
print(str(s))
s.eat()
