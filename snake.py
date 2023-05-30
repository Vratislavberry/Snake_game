from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.player = []
        self.food_score = 0
        x = 0
        for i in range(3):
            self.player.append(self.add_block(x))
            x -= 20
        self.head = self.player[0]
        self.head.color("green")


    def add_block(self, x, y = 0):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.speed("fastest")
        turtle.color("white") if len(self.player) % 2 == 1 else turtle.color("grey")
        turtle.setposition(x, y)
        return turtle


    def move(self):
        for block_num in range(len(self.player) - 1, 0, -1):
            new_x = self.player[block_num - 1].xcor()
            new_y = self.player[block_num - 1].ycor()
            self.player[block_num].goto(new_x, new_y)
        self.player[0].forward(20)

    def append_snake(self):
        tail_position = self.player[-1].position()
        self.move()
        self.player.append(self.add_block(tail_position[0], tail_position[1]))


    def head_in_body(self):
        for block in self.player[1:]:
            if self.head.distance(block) < 1:
                return True
        return False


    def inc_score(self):
        self.food_score += 1

    def up(self):
        self.head.setheading(UP) if self.head.heading() != DOWN else DOWN


    def down(self):
        self.head.setheading(DOWN) if self.head.heading() != UP else UP


    def left(self):
        self.head.setheading(LEFT) if self.head.heading() != RIGHT else RIGHT



    def right(self):
        self.head.setheading(RIGHT) if self.head.heading() != LEFT else LEFT
