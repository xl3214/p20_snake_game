from turtle import Turtle

MOVE_DISTANCE = 20
DIRECTIONS = {"Up": 90, "Down": 270, "Left": 180, "Right": 0}
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Add a new segment to the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTIONS["Down"]:
            self.head.setheading(DIRECTIONS["Up"])

    def down(self):
        if self.head.heading() != DIRECTIONS["Up"]:
            self.head.setheading(DIRECTIONS["Down"])

    def left(self):
        if self.head.heading() != DIRECTIONS["Right"]:
            self.head.setheading(DIRECTIONS["Left"])

    def right(self):
        if self.head.heading() != DIRECTIONS["Left"]:
            self.head.setheading(DIRECTIONS["Right"])

    def reset(self):
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
