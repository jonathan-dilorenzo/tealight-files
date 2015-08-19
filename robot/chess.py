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

#for i in range(0,n):
#  for j in range(0,5):
#    for k in range(0,s-1):
#      move()
#    turn(1)
#  turn(3)

x=0

while True:
  if touch() == "fruit":
    x=0
    move()
  elif right_side() == "fruit":
    x=0
    turn(1)
    move()
  elif left_side() == "fruit":
    x=0
    turn(3)
    move()
  elif look() == "fruit":
    x=0
    move()
  elif x < 3:
    x=x+1
    turn(1)
  elif touch() == "wall":
    break
  else:
    x=x+1
    move()
    turn(x%5)
