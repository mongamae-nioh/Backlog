#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import csv

# Backlogへログイン > 個人設定　> API から作成したAPIキーを<APIKey>へ入力
BACKLOG_API_KEY = '<APIKey>'

# Backlogのプロジェクト > プロジェクト設定 をクリックすると表示されるURLのproject.idの値を<projectID>へ入力
PROJECTID = <projectID>

# Wikiへ追加する関数
def addWiki(name,content):
    # <spaceID>は使っているBacklogのURLからコピー
    # backlog.comの場合はbacklog.jpをbacklog.comへ置き換えてください
    url = "https://<spaceID>.backlog.jp/api/v2/wikis"
    payload = {
            'apiKey': BACKLOG_API_KEY,
            'projectId': PROJECTID,
            'name': name, # Wikiのタイトル
            'content': content, # Wikiの内容（必須）
    }
    r = requests.post(url, params=payload)
    print(r.text)

# csvを一気に登録する
# <csv filename>はCSVファイル名を入力
with open('<csv filename>', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # 最初の一行をヘッダーとして取得
    for name,content in reader:
        addWiki(name,content)
