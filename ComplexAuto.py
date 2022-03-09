from Entities import Car, Driver, FuelType

class ComplexMotor:
    def __init__(self, driver, car, fuel_type):
        self.driver = driver
        self.car = car
        self.fuel_type = fuel_type

    # Расчет путевого листа
    def calculationWaybill(self):
        pass
    
    # Расчет пробега автомобиля
    def setVehicleMileage(self, mileage):
        self.mileage = mileage
        
    # Расчет фактического расхода топлива 
    def setActualFuel(self, actual_feel):
        self.actual_feel = actual_feel
        
    # Расчет расхода топлива по норме
    def setConsumptionFuelNorm(self, fuel_norm):
        self.fuel_norm = fuel_norm
        
    # Расчет числа отработанных часов
    def setHoursWorked(self, hours):
        self.hours = hours
        
    # Расчет числа тонно-километров
    def setTonKilometers(self, ton_km):
        self.ton_km = ton_km


car = Car('BWM', 200, 6)
driver = Driver('Иван', 'Иванов', 30)
fuel_type = FuelType('1', '1', '95')


obj1 = ComplexMotor(driver, car, fuel_type)

print(obj1.driver)
print(obj1.fuel_type)
print(obj1.car)
