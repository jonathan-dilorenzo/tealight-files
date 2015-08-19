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
  elif left_side() == "wall":
    turn(1)
  else:
    turn(3)
    
while True:
  super_move()
  
    
    