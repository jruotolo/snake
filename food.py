from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('blue')
        self.shapesize(stretch_wid=.75, stretch_len=.75)
        self.pu()
        self.setpos(x=randint(-280, 280), y=randint(-280, 280))
        self.speed('fastest')

    def refresh(self):
        self.setpos(x=randint(-280, 280), y=randint(-280, 280))
