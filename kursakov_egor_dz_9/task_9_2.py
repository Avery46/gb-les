


class road:
    
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'неободимая {round(asphalt_mass)} массa асфальта')


answ = road(5000, 20)
answ.mass()
