#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Animal is-a object, that is a class named "object"... just to confuse matters ;)
class Animal(object):
    def pet(self):
        print "Insert default petting message here"

# Dog is an Animal
class Dog(Animal):
    def __init__(self, name):
        # Dog has a name
        self.name = name

    def pet(self):
        print "The dog is happy but smells awfully"

# Cat is an animal
class Cat(Animal):
    def __init__(self, name):
        # Cat has a name
        self.name = name

    def pet(self):
        print "The cat is purrning and then bites you"

# Person is an object
class Person(object):
    def __init__(self, name):
        # Person has a name
        self.name = name

        # Person has a pet of some kind
        self.pet = None

# Employee is a Person
class Employee(Person):
    def __init__(self, name, salary):
        # Employee assigns it's name through superclass constructor | Magic!
        super(Employee, self).__init__(name)
        # Employee has a salary. Not surprisingly, really
        self.salary = salary

# Fish is an object and has no members.
class Fish(object):
    pass

# Salmon is a Fish
class Salmon(Fish):
    pass

# Halibut is a Fish, too.
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# bill is a Cat
bill = Cat("Bill")

# mary is a Person
mary = Person("Mary")

# Mary has a pet - bill
mary.pet = bill

# frank is an Employee with a good salary
frank = Employee("Frank", 120000)

# frank has a pet - rover
frank.pet = rover

# flipper is a Fish
flipper = Fish()

# crouse is a Salmon
crouse = Salmon()

# harry is a Halibut
harry = Halibut()

# petting mary's pet:
mary.pet.pet()

# petting frank's pet:
print "Attempting to pet the pet of", frank.name
frank.pet.pet()
