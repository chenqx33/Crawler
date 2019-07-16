import json

import requests
from bs4 import BeautifulSoup
import xlwt

def formatConTent(content):
    str = content[14:]
    var = str[:-1]
    var.replace('\'', '\\\'')
    return var


def get_page(page):
    url_temp = 'https://temp.163.com/special/00804KVA/cm_guonei_0{}.js'
    return_list = []
    resultList=[]
    for i in range(page):
        url = url_temp.format(i + 2)
        response = requests.get(url)
        if response.status_code != 200:
            continue
        content = response.text
        _content = formatConTent(content)
        result = json.loads(_content)
        return_list.append(result)
        for index in range(len(result)):
            resultList.append(get_content(result[index].get('tlink')))

    save_excel(resultList)
    return return_list


def get_content(url):
    source = ''
    author = ''
    body = ''
    resp = requests.get(url)
    if resp.status_code == 200:
        body = resp.text
        bs4 = BeautifulSoup(body)
        source = bs4.find('a', id='ne_article_source').get_text()
        author = bs4.find('span', class_='ep-editor').get_text()
        body = bs4.find('div', class_='post_text').get_text()
    return source, author, body


def save_excel(resultList):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('第一个sheet')
    head = ['来源','作者','内容']
    for h in range(len(head)):
        sheet.write(0,h,head[h])
    i=1
    for list in resultList:
        j=0
        for data in list:
            sheet.write(i,j,data)
            j+=1
        i+=1
    book.save('zol1.xls')
get_page(1)
