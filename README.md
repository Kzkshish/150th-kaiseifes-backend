# 環境構築
## 仮想環境の構築 & モジュールのインストール
```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
## データベースの作成
```bash
$ brew install postgresql
$ psql
$ CREATE DATABASE kaiseifes_150th_backend;
```