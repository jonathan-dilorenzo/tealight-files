from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

r=100

for i in range(0,r):
  move(10)
  turn(360.0/r)
  color(colors[i%3])