class Rover:
    def __init__(self, x, y, compass):
        self.x = x
        self.y = y
        self.compass = compass
    def move_forward(self):
        self.x += 1
    def move_backward(self):
        self.x -= 1

        
rover1 = Rover(0, 0, "N")
print(rover1.x)
rover2 = Rover(1, 1, "N")
print(rover2.x)
rover1.move_forward()
print(rover1.x)
rover1.move_backward()
print(rover1.x)