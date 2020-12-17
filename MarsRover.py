class Rover:
    def __init__(self, x, y, compass):
        self.x = x
        self.y = y
        self.compass = compass
    def move_forward(self):
        if self.compass == "N":
            self.x += 1
        elif self.compass == "S":
            self.x -= 1
        elif self.compass == "W":
            self.y -= 1
        elif self.compass == "E":
            self.y += 1

    def move_backward(self):
        if self.compass == "N":
            self.x -= 1
        elif self.compass == "S":
            self.x += 1
        elif self.compass == "W":
            self.y += 1
        elif self.compass == "E":
            self.y -= 1

    def turn_left(self):
        directions = {"N": "W", "W": "S", "S": "E", "E": "N"}
        self.compass = directions[self.compass]

    def turn_right(self):
        directions = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.compass = directions[self.compass]
    
    def commands(self, move):
        for instruction in move:
            if instruction == "f":
                self.move_forward()
            elif instruction =="b":
                self.move_backward()
            elif instruction == "l":
                self.turn_left()
            elif instruction == "r":
                self.turn_right()
        self.location()
    
    def location(self):
        print(f"Current coordinates: ({self.x}, {self.y})")
        print(f"direction: {self.compass}")




rover1 = Rover(0, 0, "N")
print(rover1.x)
print(rover1.y)
# rover1.move_forward()
# print(rover1.x)
# print(rover1.y)
#rover1.turn_right()
# rover1.turn_left()
print(rover1.compass)
rover1.commands(["f", "f", "l", "f", "b", "b", "r", "f"])
# print(rover1.x)
# print(rover1.compass)
# print(rover1.y)
