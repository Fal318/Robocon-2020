# ROBOCON2020
## ディレクトリ構成
- [クライアント側関連](./client)
  - [デバッグ時のクライアントの代用](./client/client.py)
  - [ライブラリ](./client/library/)
    - [音階と整数値の対応をまとめたファイル](./client/library/key.py)
- [解析関連](./compare)
  - [ログの可視化用](./compare/compare.py)
- [各種データ](./data)
  - [実行時に使うCSVの保存先](./data/csv/)
  - [実行時に生成されるログの保存先](./data/log/)
  - [CSV生成時に使うMIDIの保存先](./data/midi/)
- [サーバー側関連のディレクトリ](./master)
  - [PCで実行する用](.//master/master.py)
  - [各通信機器のアドレス](./master/address.py)
  - [ライブラリ](./master/library/)
    - [通信関連のライブラリ](./master/library/connect.py)
    - [音階と整数値の対応をまとめたファイル](./master/library/key.py)
    - [MIDIデータをCSVに変換する](./master/library/midi_to_csv.py)
    - [複数のCSVを結合する](./master/library/merge_csv.py)
- [スクリプト関連のディレクトリ](./scripts)
  - [実行用のスクリプト関連](./scripts/run)
    - [実行用のスクリプト](./scripts/run/run.sh)
    - [CSV生成用のスクリプト](./scripts/run/midi_to_csv.sh)
  - [環境構築関連のスクリプト](./scripts/setup/)
    - [環境構築用スクリプト](./scripts/setup/install.sh)

## MIDIの楽器番号の割り当て方
|楽器名|番号|
|---|--:|
|ウクレレ|33|
|カスタネット|116|
|タンバリン|113|
|シェイカー|122|

