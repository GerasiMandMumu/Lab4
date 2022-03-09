from ComplexAuto import ComplexMotor
from Entities import Car, Driver, FuelType


car = Car('BWM', 200, 6)
driver = Driver('Иван', 'Иванов', 30)
fuel_type = FuelType('1', '1', '95')


obj1 = ComplexMotor(driver, car, fuel_type)

print(obj1)
