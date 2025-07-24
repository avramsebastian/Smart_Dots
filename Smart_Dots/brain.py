import random
import math
from settings import BRAIN_SIZE

class Brain:
    def __init__(self):
        self.step = 0
        self.directions = [(math.cos(angle), math.sin(angle)) for angle in [random.uniform(0, 2 * math.pi) for _ in range(BRAIN_SIZE)]]
        
    def gaussian_mutation(self):
        mutate_index = random.randint(0, BRAIN_SIZE - 1)
        x, y = self.directions[mutate_index]
        angle = math.atan2(y,x)
        angle += random.gauss(0,0.1)
        self.directions[mutate_index] = (math.cos(angle), math.sin(angle))