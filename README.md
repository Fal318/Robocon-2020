# ROBOCON2020
## ディレクトリ構成
- [slave側](./client)
  - [ウクレレ](./client/client_u.py)
  - [パーカッション](./client/client_p.py)
  - [ライブラリ](./client/library/)
    - [CSVのヘッダーをまとめたファイル](./client/library/head.py)
    - [シリアル通信用](./client/library/serial_connect.py)
- [各種データ](./data)
  - [実行時に使うCSVの保存先](./data/)
- [master関連のディレクトリ](./master)
  - [PCで実行する用](./master/master.py)
  - [各通信機器のアドレス](./master/address.py)
  - [ライブラリ](./master/library/)
    - [Bluetooth通信関連のライブラリ](./master/library/bt_connect.py)
    - [開始時間の管理](./master/library/timestamp.py)
- [スクリプト関連のディレクトリ](./scripts)
  - [実行用のスクリプト関連](./scripts/run)
    - [実行用のスクリプト](./scripts/run/run.sh)
  - [環境構築関連のスクリプト](./scripts/setup/)
    - [環境構築用スクリプト](./scripts/setup/install.sh)


    