from turtle import Turtle
ALIGN = "left"
FONT = ("Ariel", 20, "normal")

class Scoreboard(Turtle):



    def __init__(self):
        super().__init__()

        self.score  = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x=-300, y=250)
        self.update_score()


    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(x=-70, y=0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)


    def score_count(self):
        self.score += 1
        self.clear()
        self.update_score()
    

