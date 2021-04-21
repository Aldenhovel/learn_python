import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import re

def reSearch(rule, text):
    try:
        block = re.search(rule, text).span()
        res = text[block[0]:block[1]]
        return (res,block[1])
    except:
        return None

def PrettyXml(element, indent='\t', newline='\n', level=0):
    if element:
        if (element.text is None) or element.text.isspace():
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
    temp = list(element)
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):
            subelement.tail = newline + indent * (level + 1)
        else:
            subelement.tail = newline + indent * level
        PrettyXml(subelement, indent, newline, level=level + 1)


def _getPageText(url):
    return requests.get(url).text

def _getCellPhoneData(text):
    soup = BeautifulSoup(text, features='html.parser')
    body = soup.body
    dt = body.find('div', class_='wrapper clearfix')\
                    .find('div', class_='content')\
                    .find('div', class_='pic-mode-box')\
                    .find('ul', id='J_PicMode')\
                    .find_all('li')
    res_dt = []
    for block in dt:
        try:
            name = reSearch('.*（', block.a.img['alt'])[0][:-1]
            URL = block.a['href']
            pictURL = block.a.img['.src']
            res_dt.append({'name':name, 'URL':URL, 'picURL':pictURL})
        except:
            pass
    return res_dt

def _getScore():
    path = "name.xml"
    tree = ET.parse(path)
    root = tree.getroot()
    phones = root.findall('phone')
    count = 0
    for phone in phones:
        try:
            phone_id = reSearch(r'[0-9]{7}', phone.find('URL').text)[0]
            score_url = 'https://detail.zol.com.cn/1327/$/review.shtml'.replace('$', phone_id)
            text = requests.get(score_url).text
            soup = BeautifulSoup(text)
            body = soup.body
            dt = []
            block = body.find_all('div', class_='wrapper clearfix')[1]\
                              .find('div', class_='content')\
                              .find('div', class_='review-comments-score new-review-comments')\
                              .find('div', class_='total-bd clearfix')
            total_score = block.find('div', class_='total-score').find('strong').text
            dt.append(total_score)
            score_block_list = block.find('div', class_='features-score features-score-5')\
                              .find_all('div', class_='features-circle')
            for score_block in score_block_list:
                score = score_block.find('div', class_='circle-value').text
                dt.append(score)

            total_score = ET.Element('total_score')
            total_score.text = dt[0]
            value_for_money = ET.Element('v4m')
            value_for_money.text = dt[1]
            power = ET.Element('power')
            power.text = dt[2]
            battery = ET.Element('battery')
            battery.text = dt[3]
            look = ET.Element('look')
            look.text = dt[4]
            snap = ET.Element('snap')
            snap.text = dt[5]

            phone.append(total_score)
            phone.append(value_for_money)
            phone.append(power)
            phone.append(battery)
            phone.append(look)
            phone.append(snap)

            print(dt)
            PrettyXml(root)
            tree.write(path, encoding='utf-8', xml_declaration=True)
            count += 1
            print(str(count)+' finish...'+phone.find('name').text)
        except:
            print('已跳过一条......')



def _saveToXML(dt):
    path = "name.xml"
    tree = ET.parse(path)
    root = tree.getroot()
    for data in dt:
        phone = ET.Element("phone")
        name = ET.Element("name")
        name.text = data['name']
        URL = ET.Element("URL")
        URL.text = data['URL']
        picURL = ET.Element('picURL')
        picURL.text = data['picURL']
        phone.append(name)
        phone.append(URL)
        phone.append(picURL)
        root.append(phone)
    PrettyXml(root)
    tree.write(path, encoding='utf-8', xml_declaration=True)
    print('finish...')

if __name__ == "__main__":

    for i in range(1, 15):
        url = 'https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_$.html'.replace('$', str(i))
        text = _getPageText(url)
        dt = _getCellPhoneData(text)
        _saveToXML(dt)
        print(i)
    _getScore()