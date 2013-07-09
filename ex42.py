#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Animal is-a object, that is a class named "object"... just to confuse matters ;)
class Animal(object):
    pass

# ??
class Dog(Animal):
    def __init__(self, name):
        # ??
        self.name = name

# ??
class Cat(Animal):
    def __init__(self, name):
        # ??
        self.name = name

# ??
class Person(object):
    def __init__(self, name):
        # ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

# ??
class Employee(Person):
    def __init__(self, name, salary):
        # ?? Magic!
        super(Employee, self).__init__(name)
        # ??
        self.salary = salary

# ??
class Fish(object):
    pass

# ??
class Salmon(Fish):
    pass

# ??
class Halibut(Fish):
    pass

# rova is-a Dog
rover = Dog("Rover")

# ??
bill = Cat("Bill")

# ??
mary = Person("Mary)

# ??
mary.pet = bill

# ??
frank = Employee("Frank", 120000)

# ??
frank.pet = rover

# ??
flipper = Fish()

# ??
crouse = Salmon()

# ??
harry = Halibut()
