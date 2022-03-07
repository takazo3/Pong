from turtle import Turtle
FONT = ("Courier", 60, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):\

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 10
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 10
        self.update_scoreboard()