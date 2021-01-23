from turtle import Turtle



ALIGNMENT = 'center'
Font = ("Courier", 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"/Users/jruot/PycharmProjects/snake/data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color('white')
        self.pu()
        self.goto(x=0, y=380)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"  High score {self.high_score}\nCurrent score {self.score}", move=False, align=ALIGNMENT,
                   font=Font)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"/Users/jruot/PycharmProjects/snake/data.txt", mode='w') as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
