## 知能ロボコン機体の開発
* 機体名 : one-cannon
* １つのアームで、ボールの吸引回収と射出を行う戦車型の自律ロボット
* 学部３年次の研究テーマとして、３人チームで開発

## 知能ロボットコンテストとは
* スタート時を除いて人為的な操作を一切禁止された、自律型ロボットの大会
* 赤・青・黄のボール15個を、それぞれの色のゴールに入れると得点となる

    [公式HPのリンク](http://www.inrof.org/irc/)      　  

# overview
<img src="https://user-images.githubusercontent.com/45473923/78965145-27d66080-7b37-11ea-95ef-4c8ed0d6fd88.JPG" width=45%> <img src="https://user-images.githubusercontent.com/45473923/78965169-3a509a00-7b37-11ea-9926-cc55da3de0c4.JPG" width=45%> 

## Demo Movie
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/bEosERW4-E4/0.jpg)](http://www.youtube.com/watch?v=bEosERW4-E4)

   [Youtubeアカウントのリンク](https://www.youtube.com/channel/UC2I3qbTQnZT58ISES_YTEEw?view_as=subscriber)

## 知能ロボコン機体[one-cannon]の機能
* ボールの回収はDCモータによる吸引機構で行う
* ボールの射出はラック&ピニオン機構により、バネをモータで圧縮し射出する
* 外部カメラからの角度・距離データをもとにエンコーダを用いて旋回・直進
* ロボットの位置・姿勢は「April Tags」という取り付けたタグを用いて推定
* ボールの位置・色の認識は「OpenCV」を用いた画像処理で行う
* フォトリフレクタを7個使用し、ボールエリアまでライントレース
* 圧力センサで吸引機構のボール有無を確認
* ボールや壁への接触はリミットセンサと圧力センサで回避
* 吸引時の首振り機能により吸引範囲の拡大
* ゴール方向の旋回を3パターン用意し、最短経路でゴール方向へ照準を合わせる

## License
* This repository is licensed under the BSD 3-Clause License, see LICENSE.


