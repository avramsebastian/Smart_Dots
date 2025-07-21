import random
import math

class Brain:
    def __init__(self, size):
        self.step = 0
        self.directions = [(math.cos(angle), math.sin(angle)) for angle in [random.uniform(0, 2 * math.pi) for _ in range(size)]]
        