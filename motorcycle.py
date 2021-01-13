from gearError import GearError


class Motorcycle:
    def __init__(self, brand, model, color, min_gear=0, max_gear=5, gear=0):
        self.brand = brand
        self.model = model
        self.color = color
        self.turn_on = False
        self.min_gear = min_gear
        self.max_gear = max_gear
        self.gear = gear

    def turnOn(self):
        self.turn_on = True

    def turnOff(self):
        self.turn_on = False

    def status(self):
        return self.turn_on

    @property
    def minimumGear(self):
        return self.min_gear

    @property
    def maximumGear(self):
        return self.max_gear

    @minimumGear.setter
    def minimumGear(self, value):
        self.min_gear = value

    @maximumGear.setter
    def maximumGear(self, value):
        self.max_gear = value

    def verifyMotorOn(self):
        if self.status():
            return True

    def verifyGear(self, gear):
        if gear >= self.min_gear and gear < self.max_gear:
            return True
        raise GearError

    def increaseGear(self):
        if self.verifyMotorOn():
            self.gear += 1
            if self.verifyGear(self.gear):
                return self.gear

    def decraseGear(self):
        if self.verifyMotorOn():
            self.gear -= 1
            if self.verifyGear(self.gear):
                return self.gear

    def __str__(self):
        return f'Brand: {self.brand} \n Model: {self.model} \n Color: {self.color} \n Turned on: {self.turn_on} \n Minimum Gear: {self.min_gear} ' \
               f' \n Maximum Gear: {self.max_gear} \n Gear: {self.gear}'
