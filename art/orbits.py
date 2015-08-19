from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

x = screen_width / 2
y = screen_height / 2
vx = 0
vy = 0
ax = 0
ay = 0

power = 0.3

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x2 = x + vx
  y2 = y + vy
  
  if x2 < 0:
    x=-x2
    vx=-vx
  elif x2 > screen_width:
    x=screen_width*2-x2
    vx=-vx
  else:
    x=x2
    
    
  if y2 < 0:
    y=-y2
    vy=-vy
  elif y2 > screen_height:
    y=screen_height*2-y2
    vy=-vy
  else:
    y=y2
  
  color("blue")
  
  spot(x,y,8)
  
  
