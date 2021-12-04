from bs4 import BeautifulSoup
import requests


def get_keyword_number(keyword):

    url = "https://www.google.com/search?q={}".format(keyword)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')
        number = soup.select_one('#result-stats').text

        if number.find('약') > -1:
            number = int(number[number.find('약')+2:number.rfind('개')].replace(',', ''))
        else:
            number = int(number[number.find('t')+2:number.rfind('r')].replace(',', ''))

        return number if number else 0
    except:
        return 0
