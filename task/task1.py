class Figura:
    count=0
    def __init__(self, color, name):
        self.color=color
        self.name=name
        Figura.count+=1
    def  info(self):
        print("Имя", self.name,
              "\nЦвет", self.color )
class Krug(Figura):
    count=0
    def __init__(self, color, name, radius, x, y):
        self.radius=radius
        self.x=x
        self.y=y
        super().__init__(color, name)

    def  info(self):
        print("R", self.radius,
              "\nX", self.x,
              "\nY", self.y, )
        super().info()

l1=Figura("red", "krug")
l1.info()
l2=Krug("red", "allax", "33", "55", "-0.5")
l2.info()