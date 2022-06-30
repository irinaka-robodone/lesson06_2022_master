from microbit import *
import music
x = 0
y = 0
while True:
  
  if x == 4 and y == 4:
    music.play(music.POWER_UP)
    x = 0
    y = 0
    display.clear()
  if button_a.was_pressed():
    x += 1
    if x > 4:
      x = 4
      
  elif button_b.was_pressed():
    y += 1
    if y > 4:
      y = 4
  display.set_pixel(x,y,9)
