from microbit import *
import music

current_pos = [0,0]

while True:
  current_pos = [0,0]           # スネークの頭の位置をリスト [x,y] で記憶する
  display.clear()
  
  """
  先生は [4,4] に到達するまでのプレイを１ゲームと捉えて、１ゲームごとにループするようにしています。
  こうすると、
  - ゲームの平均クリアタイムを求めてプレイヤー同士で競ったり、
  - 各ゲームで違うステージを作ったり
  したい時に改良しやすくなります。
  
  このようにプレイヤーからは同じ処理をしているように見えても、
  - より見やすいコード
  - より改良しやすいコード
  を作るように心がけよう。
  """
  while current_pos != [4,4]:   # スネークの最新の頭の位置が[4,4]になるまで以下の処理を繰り返す
    if button_a.was_pressed():
      current_pos[0] += 1
    if button_b.was_pressed():
      current_pos[1] += 1
      
    if current_pos[0] >= 4:     # x が 4 以上なら、これ以上進まないようにする
      current_pos[0] = 4
    if current_pos[1] >= 4:     # y が 4 以上なら、これ以上進まないようにする
      current_pos[1] = 4
      
    display.set_pixel(current_pos[0], current_pos[1], 9)  # スネークの新しい頭の位置[x,y]を描画する
    
  music.play(music.POWER_UP)    # スネークの最新の頭の位置が [4,4] になった while ループを抜けて音を再生する
    