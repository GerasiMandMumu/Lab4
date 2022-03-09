# Водитель
class Driver:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        return f'{self.name} {self.surname}: {self.age}'

# Автомобиль
class Car:
    def __init__(self, brand, power, engine_capacity):
        self.brand = brand
        self.power = power
        self.engine_capacity = engine_capacity
    def __str__(self):
        return f'{self.brand} {self.power} {self.engine_capacity}'
    
# Тип топлива
class FuelType:
    def __init__(self, heat_combustion, humidity, title):
        self.heat_combustion = heat_combustion
        self.humidity = humidity
        self.title = title
    def __str__(self):
        return f'{self.title} {self.humidity} {self.heat_combustion}'
