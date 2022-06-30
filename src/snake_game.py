from microbit import *
import music

current_pos = [0,0]

while True:
  current_pos = [0,0]
  display.clear()
  while current_pos != [4,4]:
    if button_a.was_pressed():  # ボタンAが押されたら、次へ
      current_pos[0] += 1                 #  xを＋１する
    if button_b.was_pressed():
      current_pos[1] += 1
      
    if current_pos[0] >= 4:
      current_pos[0] = 4
    if current_pos[1] >= 4:
      current_pos[1] = 4
      
    display.set_pixel(current_pos[0], current_pos[1], 9)
    
  music.play(music.POWER_UP)
    