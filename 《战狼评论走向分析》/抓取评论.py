import requests
from lxml import etree
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import time


def get_page_resource(num):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
        }
        url = 'https://movie.douban.com/subject/26363254/reviews?start={}'.format(num)
        response = requests.get(url, headers=headers, timeout=1)
        if response.status_code == 200:
            return response.text
        else:
            return 0
    except RequestException:
        return 0


def get_index_url(html):
    selector = etree.HTML(html)
    data = selector.xpath('//div[@class="main review-item"]')
    for item in data:
        url = item.xpath('div[@class="main-bd"]/h2/a/@href')
        yield [
            url[0]
        ]


def get_review_page(url, num):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
            'Referer': 'https://movie.douban.com/subject/26363254/reviews?start={}'.format(num)
        }
        response = requests.get(url, headers=headers, timeout=2)
        if response.status_code == 200:
            return response.text
        else:
            return 0
    except RequestException:
        return 0


def get_review(html):
    soup = BeautifulSoup(html, 'lxml')
    res = soup.find_all('div', {'class': 'review-content clearfix'})
    for item in res:
        return item.get_text()


def write_into_file(review):
    with open(r'demo.txt', 'a', encoding='utf-8') as f:
        f.write(review)
        f.close()


def main():
    for i in range(10, 20):
        print('正在下载第', i, '页评论')
        res = get_page_resource(i * 20)
        data = get_index_url(res)
        for url in data:
            time.sleep(2)
            html = get_review_page(url[0], i * 20)
            if html:
                review = get_review(html)
                write_into_file(review)


if __name__ == '__main__':
    main()
