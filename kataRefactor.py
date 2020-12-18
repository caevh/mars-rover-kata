import random
class Rover:

    def __init__(self, x, y, compass, world):
        self.world = world
        self.x = x
        self.y = y
        self.compass = compass
        self.world.globe_gen(x, y)

    def move_forward(self):
        # Moves the rover forward and depending on which way its facing will +,- from x or y axis
        if self.compass == "N":
            self.x += 1
        elif self.compass == "S":
            self.x -= 1
        elif self.compass == "W":
            self.y -= 1
        elif self.compass == "E":
            self.y += 1

    def move_backward(self):
        # Moves the rover backwards and depending on which way its facing will +, - from x or y axis
        if self.compass == "N":
            self.x -= 1
        elif self.compass == "S":
            self.x += 1
        elif self.compass == "W":
            self.y += 1
        elif self.compass == "E":
            self.y -= 1
    
    def turn_left(self):
        # Used to turn the rover left
        directions = {"N": "W", "W": "S", "S": "E", "E": "N"}
        self.compass = directions[self.compass]

    def turn_right(self):
        # Used to turn the rover right
        directions = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.compass = directions[self.compass]

    def commands(self, instructions):
        # Used to loop through instructions and depending on the command will call the correct method to move or turn the rover
        # Also has exception incase a wrong str is used as input
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
        reference_world = self.world.globe_gen(self.x, self.y)
        if self.x == reference_world[0] + 1:
            self.x = self.world.x_axis_wrapper(self.x)
        elif self.x == reference_world[1]:
            self.x = self.world.x_axis_wrapper(self.x)
        elif self.y == reference_world[2]:
            self.y = self.world.y_axis_wrapper(self.y)
        elif self.y == reference_world[-1]:
            self.y = self.world.y_axis_wrapper(self.y)

        # Used to print where the Rover is at the end of the sequence
        print(f"Current coordinates: ({self.x}, {self.y})")
        print(f"direction: {self.compass}")

class World:
    def __init__(self, globe=[]):
        self.globe = globe
    
    def globe_gen(self, x, y):
        globe = []
        if x > y:
            x_y_axis = random.randint(x, x+20)
        else:
            x_y_axis = random.randint(y, y+20)
        globe.append(-x_y_axis)
        globe.append(x_y_axis)
        globe.append(-x_y_axis)
        globe.append(x_y_axis)
        self.globe = globe
        print(globe)
        return globe


    def x_axis_wrapper(self, x):
        # Used to wrap when rover reaches the end of the world on the y axis
        north_south_edge = self.globe[1] + 1
        if x == north_south_edge:
            x = -10
            return x
        elif x == -north_south_edge:
            x = 10
            return x
    
    def y_axis_wrapper(self, y):
        # Used to wrap when rover reaches the end of the globe on the y axis
        east_west_edge = self.globe[-1] + 1
        if y == east_west_edge:
            y = -10
            return y
        elif y == -east_west_edge:
            y = 10
            return y