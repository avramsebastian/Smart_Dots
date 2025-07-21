from dot import Dot

class Population:
    def __init__ (self):
      self.Dots = [Dot() for _ in range(100)]

    def show(self,screen):
       for i in range(len(self.Dots)):
          self.Dots[i].show(screen)

    def update(self):
       for i in range(len(self.Dots)):
          self.Dots[i].update()
