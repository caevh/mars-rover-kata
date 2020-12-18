from kataRefactor import *

world1 = World([-10, 10, -10, 10])
rover1 = Rover(10, 10, "E", world1)
print(rover1.x)
print(rover1.y)

print(rover1.compass)
rover1.commands(["f"])
print(rover1.x)
