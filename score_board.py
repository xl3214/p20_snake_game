from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_keeper.txt", mode="r") as score_keeper:
            self.high_score = int(score_keeper.read())
        self.color("white")
        self.up()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_keeper.txt", mode="w") as score_keeper:
                score_keeper.write(f"{self.high_score}")
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
