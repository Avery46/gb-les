class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'1 сообщение'


class Pen(Stationery):
    def draw(self):
        return f'2 сообщение {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'3 сообщение {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'4 сообщение {self.title}'


pen = Pen('с ручкой')
print(pen.draw())
pencil = Pencil('с карандашем')
print(pencil.draw())
handle = Handle('с маркером')
print(handle.draw())