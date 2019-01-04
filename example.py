import time
from methodcache import cache, Store

st = Store(ttl=5)

class Car:

    def __init__(self, serial_number, milage):
        self.serial_number = serial_number
        self.milage = milage


class CarManager:

    @cache(store=st, category="car")
    def get_cars(self):
        time.sleep(2)
        return [Car("JKaHO3hoHOe4GHOy4", 234214), Car("AJAHWho4HOI46HIOA4t", 34571)]

    @cache(store=st, category="car:manufacturer", ttl=5)
    def get_manufacturer(self):
        time.sleep(3)
        return ["BMW", "Opel", "Ford"]


class FruitManager:

    @cache(store=st, category="fruit")
    def get_fruits(self):
        time.sleep(3)
        return ["Apple", "Banana", "Pineapple"]

    @cache(store=st, category="fruit:country")
    def get_country(self):
        time.sleep(3)
        return ["Germany", "Ecuador", "Costa Rica"]


fruits = FruitManager()
print()
print("Without Cache")
print(fruits.get_fruits())
print(fruits.get_country())
print()
print("With Cache")
print("-"*10)
print(fruits.get_fruits())
print(fruits.get_country())


cars = CarManager()
print()
print("Without Cache")
print(cars.get_cars())
print(cars.get_manufacturer())
print()
print("With Cache")
print("-"*10)
print(cars.get_cars())
print(cars.get_manufacturer())
print()
print("With Expired TTL")
print("-"*10)
print(fruits.get_country())
print()
print("Get All Categorys")
print("-"*10)
print(st.get_all_categorys())
print(st.get_category("car"))

