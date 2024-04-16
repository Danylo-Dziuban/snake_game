from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.setpos(x=0, y=260)
        self.color('white')

        with open('high_score.txt', mode='r') as high_score:
            self.high_score = int(high_score.read())

        self.write(f"Score: {self.score} High score: {self.high_score}", False, ALIGNMENT, FONT)


    def reset_score(self):
        # self.teleport(x=0, y=0)
        # self.write("GAME OVER", False, ALIGNMENT, FONT)

        if self.score > self.high_score:
            self.high_score = self.score

            with open('high_score.txt', mode='w') as high_score:
                high_score.write(f'{self.score}')

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False, ALIGNMENT, FONT)

