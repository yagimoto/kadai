import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#観測地点によってurlを変える
url = "https://www.data.jma.go.jp/stats/etrn/view/monthly_s3.php?prec_no=91&block_no=47940&year=&month=&day=&view="

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

years = []
averages = []

# 各行(tr)を取得
rows = soup.find_all('tr', class_='mtx')

for row in rows:
    # 年の取得
    year_tag = row.find('a')
    if year_tag:
        year = year_tag.text.strip()  # 西暦を取得

    # 各セル(td)を取得
    tds = row.find_all('td', class_='data_0_0_0_0')

    # 最後のセルの値（年平均気温）を取得
    if tds:
        raw_value = tds[-1].text.strip()  # 前後の空白を削除
        cleaned_value = ''.join(c for c in raw_value if c.isdigit() or c == '.')  # 数字と小数点のみ取得
        if cleaned_value:  # 空でなければ変換
            years.append(int(year))  # 西暦を別のリストに格納
            averages.append(float(cleaned_value))  # 年平均気温を別のリストに格納

plt.plot(years, averages)
plt.show()
