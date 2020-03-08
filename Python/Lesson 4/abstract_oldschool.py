class AbstractVehicle:

    def drive(self):
        raise NotImplementedError()

    def beep(self):
        raise NotImplementedError()


class Vehicle(AbstractVehicle):
    pass

a = Vehicle()

a.drive()