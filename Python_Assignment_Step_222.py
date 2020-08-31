class Vehicle:
    def __init__(self):
        self._numOfWheels = 4
        self.__engineType = 'Gasoline'

    def getEngineType(self):
        print(self.__engineType)

obj = Vehicle()
print(obj._numOfWheels)
obj.getEngineType()

