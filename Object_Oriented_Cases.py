from math import pi
from functools import total_ordering
from abc import ABCMeta, abstractmethod

class intTuple(tuple):
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(intTuple, cls).__new__(cls, g)

    def __init__(self, iterable):
        super(intTuple, self).__init__(iterable)


@total_ordering

class shape(object):
    @abstractmethod
    def getArea(self):
        pass

    def __lt__(self, obj):
        print("in __lt__")
        if not isinstance(obj,shape):
            raise TypeError("obj is not shape")
        return self.getArea() < obj.getArea()

    def __eq__(self, obj):
        print(" in __eq__")
        if not isinstance(obj,shape):
            raise TypeError("obj is not shape")
        return self.getArea() == obj.getArea()


class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def getradius(self):
        return self.radius

    def setradius(self, value):
        if not isinstance(value,(int ,float)):
            raise ValueError("Wrong Type")
        self.radius = float(value)

    def getArea(self):
        return self.radius**2 * pi

    R = property(getradius(), setradius())



# Using descriptor for type check

class Attr(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError("expected an %s" % self.type_)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del isinstance.__dict__[self.name]

class Person():
    name = Attr("name", str)
    age = Attr("age", int)
    height = Attr('height', float)


    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height




