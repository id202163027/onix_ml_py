class Shape:
    def __init__(self, x, y):
        self.x = x; self.y = y
    def get_center(self):
        return [self.x, self.y]
    def move(self, x, y):
        self.x = x; self.y = y
    @classmethod
    def get_distance(cls, c1, c2):
        return ( (c1.x - c2.x)**2 + (c1.y - c2.y)**2 )**.5

class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side
    def area(self):
        return self.side * self.side
    def get_vertex(self):
        return [[self.x - self.side/2, self.y + self.side/2],
                [self.x + self.side/2, self.y + self.side/2],
                [self.x - self.side/2, self.y - self.side/2],
                [self.x + self.side/2, self.y - self.side/2]]

class Triangle(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side
    def area(self):
        return self.side * self.side * (3**.5)/4
    def get_vertex(self):
        return [[self.x, self.y + self.side * (3**.5)/3],
                [self.x - self.side/2, self.y - self.side * (3**.5)/6],
                [self.x + self.side/2, self.y - self.side * (3**.5)/6]]

class Circle(Shape):
    pi = 3.14159
    def __init__(self, r=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = r
    def area(self):
        return self.radius * self.radius * Circle.pi

s = Square()
print("% s = Square()")
s.move(.5,.5)
print("% s.move(.5,.5)")
print("% s.area()\n", s.area())
print("% s.get_center()\n", s.get_center())
print("% s.get_vertex()\n", s.get_vertex())
t = Triangle(1,1.5,.5)
print("% t = Triangle(1,1.5,.5)")
print("% Shape.get_distance(s, t)\n", Shape.get_distance(s, t))
c = Circle()
print("% c = Circle()")
print("% c.area()\n", c.area())