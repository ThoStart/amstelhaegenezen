class House:
    def __init__(self, type, id, length, width, free, value, increment):
        self.type = type
        self.id = id
        self.length = length * 2
        self.width = width * 2
        self.free = free * 2
        self.value = value
        self.increment = increment

class Water:
    def __init__(self):
        self.width = 0
        self.length = 0
