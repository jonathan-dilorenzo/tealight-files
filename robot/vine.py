from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
x=0
dir=1

def super_move():
  if touch() != "wall":
    move()

while True:
  if touch() == "fruit":
    x=0
    super_move()
  elif right_side() == "fruit":
    x=0
    turn(1)
    super_move()
  elif left_side() == "fruit":
    x=0
    turn(3)
    super_move()
  elif look() == "fruit":
    x=0
    super_move()
  elif x < 3:
    x=x+1
    turn(1)
  elif touch() == "wall":
    turn(1)
  else:
    x=0
    super_move()
    turn(1)
    super_move()