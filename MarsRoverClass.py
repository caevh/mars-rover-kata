class World:
    def __init__(self, globe, x, y, compass):
        self.globe = globe
        self.x = x
        self.y = y
        self.compass = compass

    def x_axis_wrapper(self):
        if self.x == 11 and self.compass == "N":
            self.x = -10
        if self.x == 11 and self.compass == "S":
            self.x = -10
        elif self.x == -11 and self.compass == "S":
            self.x = 10
        elif self.x == -11 and self.compass == "N":
            self.x = 10
    
    def y_axis_wrapper(self):
        if self.y == 11 and self.compass == "E":
            self.y = -10
        elif self.y == 11 and self.compass == "W":
            self.y = -10
        elif self.y == -11 and self.compass == "W":
            self.y = 10
        elif self.y == -11 and self.compass == "E":
            self.y = 10
 

class Rover(World):
    def __init__(self, x, y, compass, globe):
        super().__init__(globe, x, y, compass)


    def move_forward(self):
        if self.compass == "N":
            self.x += 1
            self.x_axis_wrapper()
        elif self.compass == "S":
            self.x -= 1
            self.x_axis_wrapper()
        elif self.compass == "W":
            self.y -= 1
            self.y_axis_wrapper()
        elif self.compass == "E":
            self.y += 1
            self.y_axis_wrapper()

    def move_backward(self):
        if self.compass == "N":
            self.x -= 1
            self.x_axis_wrapper()
        elif self.compass == "S":
            self.x += 1
            self.x_axis_wrapper()
        elif self.compass == "W":
            self.y += 1
            self.y_axis_wrapper()
        elif self.compass == "E":
            self.y -= 1
            self.y_axis_wrapper()

    def turn_left(self):
        directions = {"N": "W", "W": "S", "S": "E", "E": "N"}
        self.compass = directions[self.compass]

    def turn_right(self):
        directions = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.compass = directions[self.compass]
    
    def commands(self, instructions):
        for instruction in instructions:
            if instruction == "f":
                self.move_forward()
            elif instruction == "b":
                self.move_backward()
            elif instruction == "l":
                self.turn_left()
            elif instruction == "r":
                self.turn_right()
            else:
                unknown = instructions.index(instruction)
                print(f"Command at index {unknown} ({instruction}) isn't recognised, so it is skipped")
                continue

        self.location()
    
    def location(self):
        print(f"Current coordinates: ({self.x}, {self.y})")
        print(f"direction: {self.compass}")

