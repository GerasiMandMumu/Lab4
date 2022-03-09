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

    def __str__(self):
        return f'{self.driver} {self.car} {self.fuel_type}\n'



