class MotorError(Exception):
    def __init__(self):
        super().__init__("The motorcycle is off, please turn on")
