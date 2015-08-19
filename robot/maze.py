from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def super_move():
  if touch() != "wall":
    move()
  else:
    turn(1)
    
while True:
  super_move()
    
    