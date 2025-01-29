class Observation:

    def __init__(self, high, low, dew, pres):
        self.high_temperature = high
        self.low_temperature = low
        self.dewpoint = dew
        self.pressure = pres

    def F_to_K(self):
        K = (self.high_temperature + 459.67) * (5 / 9)
        return K

    def F_to_C(self):
        C = (self.high_temperature - 32) * (5 / 9)
        return C