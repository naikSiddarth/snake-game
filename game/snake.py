from turtle import Turtle
STARTING_POSITION = [(0, 0),(-20, 0),(-40,0)]
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION: 
            self.add_segment(pos)

    def add_segment(self, pos):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.speed("slow")
            new_segment.goto(pos)
            self.segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range( len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num-1].xcor()
            y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def Up(self):  
        if self.head.heading() != 270.0:
            self.head.setheading(90)

    def Down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        

    def Left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def Right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)