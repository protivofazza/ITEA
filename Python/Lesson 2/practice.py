# 1
class Vehicle:

    def __init__(self, name, color, year, weight):
        self._name = name
        self._color = color
        self._year = year
        self._weight = weight
        self.locked = True

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value

    def get_year(self):
        return self._year

    def set_year(self, value):
        self._year = value

    def get_weight(self):
        return self._weight

    def set_weight(self, value):
        self._weight = value

    def unlock(self):
        self.locked = False

    def lock(self):
        self.locked = True

    def move(self, speed):
        if not self.locked:
            print(f"Vehicle {self._name} is moving at speed {speed}mph")
        else:
            print("Unlock your car!")


class Car(Vehicle):

    def move(self, speed):
        if not self.locked:
            print(f"Your supercar {self._name} ({self._year}) is moving at speed {speed}mph")
        else:
            print("Your car is locked")


class Truck(Vehicle):

    def __init__(self, name, color, year, weight, length, empty=True):
        self._length = length
        self._empty = empty
        super().__init__(name, color, year, weight)

    def get_length(self):
        return self._length

    def set_length(self, value):
        self._length = value

    def is_empty(self):
        return self._empty

    def load(self):
        if self._empty:
            self._empty = False
            print(f"{self._name} is successfully loaded")
        else:
            print(f"{self._name} is already loaded. Unload it first!")

    def unload(self):
        if not self._empty:
            self._empty = True
            print(f"{self._name} is successfully unloaded")
        else:
            print(f"{self._name} is already empty. Load it first!")

    def move(self, speed):
        if not self.locked:
            print(f"Your truck {self._name} is moving at speed {speed}mph")
        else:
            print("Your truck is locked")


tesla = Car("Tesla", "Black", 2020, 1500)
tesla.unlock()
tesla.move(100)

uaz = Truck("UAZ", "Yellow", 1980, 7000, 7, True)
uaz.unlock()
uaz.load()
uaz.move(30)

print("-"*30)


# 2
class Shop:

    total_products_sold = 0

    def __init__(self, name):
        self._name = name
        self._sold_goods = 0

    def sell(self, count):
        self._sold_goods += count
        Shop.total_products_sold += count

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_sold_goods(self):
        return self._sold_goods


novus = Shop("NOVUS")
atb = Shop("ATB")
novus.sell(100)
atb.sell(200)
print(Shop.total_products_sold)

print("-"*30)


# 3
class Point:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

    def get_z(self):
        return self._z

    def set_z(self, value):
        self._z = value

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y, self._z + other._z)

    def __sub__(self, other):
        return Point(self._x - other._x, self._y - other._y, self._z - other._z)

    def __truediv__(self, other):
        return Point(self._x / other._x, self._y / other._y, self._z / other._z)

    def __mul__(self, other):
        return Point(self._x * other._x, self._y * other._y, self._z * other._z)

    def __neg__(self):
        return Point(-self._x, -self._y, -self._z)


p1 = Point(1, 2, 3)
p2 = Point(2, 3, 4)
p3 = p1*p2
print(p3.get_x())
print(p3.get_y())
print(p3.get_z())

print("-"*30)


# 4
