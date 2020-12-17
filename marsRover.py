class Thing:
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
        if self.compass == "N":
            self.compass = "W"
        elif self.compass == "W":
            self.compass = "S"
        elif self.compass == "S":
            self.compass = "E"
        elif self.compass == "E":
            self.compass = "N"

    def turn_right(self):
        if self.compass == "N":
            self.compass = "E"
        elif self.compass == "E":
            self.compass = "S"
        elif self.compass == "S":
            self.compass = "W"
        elif self.compass == "W":
            self.compass = "N"

class Martian(Thing):
    
    def destroy(self):
        print("Destroy")

class Rover(Thing):
        
    def scan(self):
        print("Scanning")


rover1 = Rover(0, 0, "N")
m = Martian(1, 2, "S")
players = [rover1, m]

for player in players:
    print(player.x)