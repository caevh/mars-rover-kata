from kataRefactor import *

world1 = World()
world1.globe_gen()
rover1 = Rover(10, -10, "N", world1)
print(rover1.x)
print(rover1.y)

print(rover1.compass)
rover1.commands(["f"])
print(rover1.x)
