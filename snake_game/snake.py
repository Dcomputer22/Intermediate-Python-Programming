from turtle import Turtle
SNAKE_AXIS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_segment = []
        self.create_snake()
        self.head = self.snake_segment[0]

    def create_snake(self):
        for position in SNAKE_AXIS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segment.append(new_segment)

    def reset(self):
        for segment in self.snake_segment:
            segment.goto(1000, 1000)
        self.snake_segment.clear()
        self.create_snake()
        self.head = self.snake_segment[0]
    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.snake_segment[-1].position())
        # -1 because I need to get hold of the last segment in the list regardless of the segment length

    def move(self):
        for seg_num in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[seg_num - 1].xcor()
            new_y = self.snake_segment[seg_num - 1].ycor()
            self.snake_segment[seg_num].goto(new_x, new_y)
        self.snake_segment[0].forward(MOVE_DISTANCE)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
