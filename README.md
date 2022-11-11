# プログラミング研究部の出席管理システム

## 使い方
1. パッケージをインストールする
```sh
$ sudo update && sudo upgrade
$ sudo apt install git make python3 python3-pip
```

2. git clone
```sh
$ git clone https://github.com/yumekiti/prog_discord.git
```

3. パッケージのインストール
```sh
$ cd prog_discord
$ pip install -r requirements.txt
```

4. .envファイルの作成
```sh
$ cp .env.sample .env
```

5. .envファイルの編集
```sh
$ vim .env
```

6. 実行
```sh
$ python main.py
```

## .envファイルの例
```sh
TOKEN=hoge              # DiscordBotのトークン
CHANNEL_ID=123456789    # チャンネルID(メンション用)
CLASSROOM=2302          # 活動場所(任意)
ATTEND=17               # 出席時間
RECODE=20               # 記録時間
REPORT=01               # Excelの生成日
```

## systemdの設定
/lib/systemd/system/discord-bot.service
```sh
[Unit]
Description = discord-bot.service daemon

[Service]
ExecStart=/usr/bin/python3 /var/www/prog_discord/src/main.py
Restart=always
Type=simple
User=root

[Install]
WantedBy = multi-user.target
```

起動
```sh
$ systemctl start discord-bot.service
```

自動起動
```sh
$ systemctl enable discord-bot.service
```

## 自動実行される処理
|内容|時間|備考|
|-|-|-|
|出席確認メッセージ|毎日17時||
|記録処理|毎日20時||
|Excelファイルの更新|月初め||

## 処理の流れ
17時に確認メッセージを送信され、リアクションを押すと出席を確認する。<br>
20時に記録処理を行い、月初めにExcelファイルを生成する。