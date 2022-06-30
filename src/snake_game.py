from microbit import *
import music

current_pos = [0,0]

while True:
  current_pos = [0,0]       # スネークの頭の位置をリスト [x,y] で記憶する
  display.clear()
  while current_pos != [4,4]:
    if button_a.was_pressed():
      current_pos[0] += 1
    if button_b.was_pressed():
      current_pos[1] += 1
      
    if current_pos[0] >= 4:     # x が 4 以上なら、これ以上進まないようにする
      current_pos[0] = 4
    if current_pos[1] >= 4:     # y が 4 以上なら、これ以上進まないようにする
      current_pos[1] = 4
      
    display.set_pixel(current_pos[0], current_pos[1], 9)  # スネークの新しい頭の位置[x,y]を描画する
    
  music.play(music.POWER_UP)
    