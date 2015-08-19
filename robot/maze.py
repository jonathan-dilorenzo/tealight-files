from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

dir=1
def super_move():
  if touch() != "wall":
    move()
  else:
    turn(dir)
    dir=-dir
    
while True:
  super_move()
    
    