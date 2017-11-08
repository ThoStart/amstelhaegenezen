class House:
    def __init__(self, name, length, width, free, value, increment):
        self.name = name
        self.length = length * 2
        self.width = width * 2
        self.free = free * 2
        self.value = value
        self.increment = increment

class Water:
    def __init__(self):
        self.width = 0
        self.length = 0
