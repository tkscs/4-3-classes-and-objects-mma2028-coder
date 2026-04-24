import turtle
turtle.penup()
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        print f"({self.x},{self.y})"
    def draw(self):
        turtle.goto(self.x,self.y)
        turtle.write(str(self)), font = ('Arial', 32, 'normal')
    def scale(self,constant):
        self.x = self.x * constant
        self.y = self.y * constant
        new_point = Point(x,y, label = f"{constant}{str(self)}")
        return new_point
    def shift(self, constant_x=0, constant_y=0):
        self.x = self.x + constant_x
        self.y = self.y + constant_y
