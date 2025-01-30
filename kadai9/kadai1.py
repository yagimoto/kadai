import requests
from bs4 import BeautifulSoup
import re
from openpyxl import Workbook

#観測地点によってurlを変える
url = "https://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php?prec_no=91&block_no=47936&year=&month=&day=&view="
response = requests.get(url)
response.encoding = response.apparent_encoding  # 文字化け防止
data = response.text

soup = BeautifulSoup(data, 'html.parser')

temp_dict = {}

for row in soup.find_all('tr', class_='mtx'):
    cols = row.find_all('td')
    if not cols:
        continue
    
    # 年の取得（リンク内のテキストを取得）
    year_tag = cols[0].find('a')
    if not year_tag:
        continue
    year = year_tag.text.strip()

    # 気温データの取得（最後の値は平均値のため省く）
    temperatures = [re.sub(r'[^0-9.]', '', td.text.strip()) for td in cols[1:-1]]
    temperatures = [float(temp) if temp.replace('.', '', 1).isdigit() else None for temp in temperatures]

    temp_dict[year] = temperatures

wb = Workbook()
ws = wb.active
ws.title = "Temperature Data"

header = ["Year"] + [f"Month_{i+1}" for i in range(len(next(iter(temp_dict.values()), [])))]
ws.append(header)

for year, temperatures in temp_dict.items():
    ws.append([year] + temperatures)

wb.save("temperature_data.xlsx")

