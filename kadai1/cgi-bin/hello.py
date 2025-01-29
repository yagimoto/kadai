#!/usr/bin/env python3

import cgi
import datetime

def main():
    # 現在時刻を取得
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # HTTPヘッダーとHTMLコンテンツを出力
    print("Content-Type: text/html\n")
    print("<html>")
    print("<head>")
    print("<title>現在時刻</title>")
    print("</head>")
    print("<body>")
    print(f"<h1>現在時刻: {formatted_time}</h1>")
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    main()
