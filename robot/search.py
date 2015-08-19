from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# This is a fairly useless algorithm!

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
  else:
    x=x+1
    move()
    turn(x%5)
