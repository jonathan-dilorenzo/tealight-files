from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

dir=1

def super_move(dir):
  if touch() != "wall":
    move()
  elif left_side == "wall":
    turn(3)
  else:
    turn(1)
    
while True:
  super_move(dir)
  
    
    