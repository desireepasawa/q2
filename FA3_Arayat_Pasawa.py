from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return"[pH Sensor] Reading: 7.2 pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self):
        return"[Temperature Sensor] Reading: 24.5C"

print("Lab Inventory System")

ph = PHSensor()
temp = TempSensor()

print(ph.get_reading())
print(temp.get_reading())

my_sensor = Sensor()
      
