from bs4 import BeautifulSoup as bs
import xlwt
import requests


"""
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0, 0, label = 'Row 0, Column 0 Value')
workbook.save('english-root.xls')

"""
count = 0

url = 'http://www.etymon.cn'


def get_data(html):
    cookies = requests.get(f'{url}{html}').cookies
    return bs(requests.get(f'{url}{html}', cookies=cookies).content.decode(), 'lxml')


workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')

for j in range(1, 39):
    data = get_data(f'/yingyucigen/list_1_{j}.html')
    for i in data.find_all('dt'):
        data2 = get_data(i.find('a')['href'])
        try:
            worksheet.write(count, 0, label=data2.find('dt').get_text())
            worksheet.write(count, 1, label=data2.find('dd').get_text())
            print(data2.find('dt').get_text())
            print(data2.find('dd').get_text())
            count += 1
        except AttributeError as e:
            print(e)

workbook.save('english-root.xls')
print(f"总条数为：{count}")


