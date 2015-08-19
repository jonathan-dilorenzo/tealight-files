from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

s=5
n=8

for i in range(0,n):
  for j in range(0,5):
    for k in range(0,s-1):
      move()
    turn(1)
  turn(3)