class GearError(Exception):
    def __init__(self):
        super().__init__("The operation cannot be completed because the gear is invalid")
