from MarsRoverClass import Rover


rover1 = Rover(-10, -10, "E", [-10, 10, -10, 10])
print(rover1.x)
print(rover1.y)

print(rover1.compass)
rover1.commands(["b"])
print(rover1.x)
