class House:
    def __init__(self, name, length, width, free, value, increment):
        self.name = name
        self.length = length
        self.width = width
        self.free = free
        self.value = value
        self.increment = increment

class Ground:
	def __init__(self):
		self.grid = []
		self.width = 360
		self.length = 320

class Water:
    def __init__(self):
        self.width = 0
        self.length = 0
