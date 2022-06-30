from microbit import *
import music
x = 0
y = 0
display.set_pixel(0,0,9)
while True:
  if button_a.was_pressed():
    x = x + 1
    if x >= 5:
      x = 4
    display.set_pixel(x,y,9)
  if button_b.was_pressed():
    y = y + 1
    if y >= 5:
      y = 4
    display.set_pixel(x,y,9)
  elif x == 4 and y == 4:
    music.play(music.POWER_UP)
    display.clear()
    x = 0
    y = 0
    display.set_pixel(0,0,9)



