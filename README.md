# ROBOCON2020
- [スクリプトをまとめたディレクトリ](./scripts)
    - [環境構築用スクリプト](./scripts/install.sh)

- [サーバー側のファイルをまとめたディレクトリ](./server)
    - [送信する値と楽器の状態をまとめたファイル](./server/instrument.py)
    - [各通信機器のアドレスを保持したファイル](./server/address.py)
    - [通信関連をクラス化したファイル](./server/RN42.py)
    - [PCで実行する用のファイル](./server/server.py)

- [クライアント側のファイルをまとめたディレクトリ](./client)
    - [送信する値と楽器の状態をまとめたファイル](./client/instrument.py)
    - [各通信機器のアドレスを保持したファイル](./client/address.py)
    - [通信関連をクラス化したファイル](./client/RN42.py)
    - [クライアント側で実行する用のファイル](./client/client_0.py)

- [データを可視化するためのファイルをまとめたディレクトリ](./compare)
    - [ログを可視化するファイル](./compare.py)
