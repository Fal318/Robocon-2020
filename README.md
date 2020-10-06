# ROBOCON2020
## ディレクトリ構成
- [ラズパイ側](./client)
  - [ウクレレ](./client/client_u.py)
  - [パーカッション](./client/client_p.py)
  - [ライブラリ](./client/library/)
    - [CSVのヘッダーをまとめたファイル](./client/library/head.py)
    - [シリアル通信用](./client/library/serial_connect.py)
- [各種データ](./data)
  - [実行時に使うCSVの保存先](./data/csv/)
- [サーバー側関連のディレクトリ](./master)
  - [PCで実行する用](.//master/master.py)
  - [各通信機器のアドレス](./master/address.py)
  - [ライブラリ](./master/library/)
    - [Bluetooth通信関連のライブラリ](./master/library/bt_connect.py)
    - [開始時間の管理](./master/library/timestamp.py)
- [スクリプト関連のディレクトリ](./scripts)
  - [実行用のスクリプト関連](./scripts/run)
    - [実行用のスクリプト](./scripts/run/run.sh)
  - [環境構築関連のスクリプト](./scripts/setup/)
    - [環境構築用スクリプト](./scripts/setup/install.sh)

## 送信するデータ
### ウクレレ
  - データの大きさ:24bit
    |データの範囲|データの大きさ(bit)|データの内容|
    |:-:|:-:|:-:|
    |1~4|4|弦|
    |5~11|7|BPM|
    |12|1|ストロークのタイミング|
    |13|1|ストロークのオンオフ|
    |14~19|6|コード番号|
    |20~22|3|表情|
    |23~24|2|首の状態|
  - BPMが0になることはないのでBPMが0の場合は終了コード
### パーカッション
  - データの大きさ:24bit
    |データの範囲|データの大きさ(bit)|データの内容|
    |:-:|:-:|:-:|
    |1|1|カスタネット|
    |2|2|シェイカー|
    |3|3|タンバリン|
    |4~5|2|目のLEDのパターン|
    |6~8|3|目のLEDの色|
    |9~24|16|データサイズ調整用の空データ|
  - 空データのbitは1固定。終了時だけ0。