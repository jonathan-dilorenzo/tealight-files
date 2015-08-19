from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

r=100

for i in range(0,r):
  move(2)
  turn(360/r)
  color(colors[i%3])