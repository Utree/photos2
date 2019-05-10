## 概要
画像編集サイト

### 全体のアーキテクチャ
![](https://d2mxuefqeaa7sj.cloudfront.net/s_F5BD2AC707D626C6F3286771CE0C236A048149558DDB7F75DEFC080E81A03A17_1538976095106_+2018-10-08+14.20.54.png)

### API_v1ドキュメント
https://qiita.com/yuuki_sekiya/private/a6a0d87917425227abf4

## API_v2ドキュメント
comming soon

### DB ER図
![](https://d2mxuefqeaa7sj.cloudfront.net/s_F5BD2AC707D626C6F3286771CE0C236A048149558DDB7F75DEFC080E81A03A17_1538567298724_+2018-10-03+20.47.34.png)

## 環境
- プラットフォーム: Cloud9
- 言語: Python3
- データベース: SQLite
- ライブラリ: requirements.txtを参照

# 注意
DBと画像の保存先をリポジトリ内に設定しているので、herokuにデプロイしてあるサービスは、1時間毎にユーザー情報と保存済みの画像が削除されます

