# 知能ロボコン機体[one-cannon]の機能
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

## Demo Movie
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/bEosERW4-E4/0.jpg)](http://www.youtube.com/watch?v=bEosERW4-E4)
