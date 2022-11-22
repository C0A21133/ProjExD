# 第1回
## 消えたアルファベットを探すゲーム（kadai/kadai01.py）
### 遊び方
* コマンドラインでkadai01.pyを実行すると，標準出力に問題が表示される．
* 標準入力から答えを入力する．
* 正解なら「正解！！！」と表示される．
* 不正解なら「不正解」と表示される．
* 不正解の場合、10回まで繰り返す。
### プログラム内䛾解説
* main関数：クイズプログラムの全体の流れを担当する．
* select_target_alphabet関数：ランダムにTarget_Lengthの数だけアルファベットえらぶ．
* select_missing_alphabet関数：target_listからMissing_Lengthの数だけアルファベットを抽出し、 (ques_list, ans_list) を返す