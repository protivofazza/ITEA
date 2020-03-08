from abc import ABC, abstractmethod

# abstract bases classes


class AbstractVehicle(ABC):

    @abstractmethod
    def drive(self):
        print("Driving")

    @abstractmethod
    def beep(self):
        print("Beeping")


class Vehicle(AbstractVehicle):

    def __init__(self, model, engine):
        self._model = model
        self._engine = engine

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    #print(a.)

    def drive(self):
        super().drive()

    def beep(self):
        super().beep()


auto = Vehicle(1, 2)

auto.drive()
auto.beep()
auto.model = 5
print(auto.model)



