class Stationery:
    def __init__(self, title='some type of stationery'):
        self.title = title

    def draw(self):
        print(f"let's draw with {self.title}!")


class Pen(Stationery):
    def draw(self):
        print(f"let's write with {self.title}...")


class Pencil(Stationery):
    def draw(self):
        print(f"Let's draw a pencil-picture with {self.title}? ;)")


class Handle(Stationery):
    def draw(self):
        print(f"Let's distinguish something with {self.title}! ")


stationery = Stationery()
stationery.draw()

pen = Pen('Bruno Visconti')
pen.draw()

pencil = Pencil('KOH-I-NOOR')
pencil.draw()

handle = Handle('VENTE')
handle.draw()
