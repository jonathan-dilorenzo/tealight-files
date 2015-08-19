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
  else:
    turn(dir)
    return True
    
while True:
  if super_move(dir):
    dir=-dir
  
    
    