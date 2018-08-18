from urllib.parse import urlencode
import requests
from requests.exceptions import RequestException
import json
import re
from bs4 import BeautifulSoup
import os
import random
import threading
import time
#拿到索引页源码
start = time.time()
def get_page_index(offset, keyword):
    #将URL参数定义为一个字典，将offset和keyword作为变量传进来，便于获取不同页不同关键词的图片
    data = {
         'offset': offset,
         'format': 'json',
         'keyword': keyword,
         'autoload': 'true',
         'count': 20,
         'cur_tab': 3,
         'from': 'gallery'
    }
    #将参数通过urlencode方法变成URL参数，形成完整的可访问参数
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    #异常捕获，增加程序的健壮性
    try:
        #发送请求，获得源码
        html = requests.get(url)
        #判断访问是否成功
        if html.status_code == 200:
            #访问成功后返回结果
            return html.text
        #访问失败返回空
        return None
    #捕获到异常后，输出异常，并返回空
    except RequestException:
        print('请求详情页出错')
        return None

#对索引页进行解析，拿到目标页URL
def parse_page_index(html):
    #利用json.loads方法将str类型的源码转换为dict类型的
    frist_data = json.loads(html)
    #判断data是否在字典的key值中
    if frist_data and 'data' in frist_data.keys():
            #循环将data的values值拿出来
            for item in frist_data.get('data'):
                #判断article_url是否在item中
                if 'article_url' in item:
                    #用生成器将article_url的键值输出来
                    yield item.get('article_url')


#获取目标页
def get_page_detail(url):
    try:
        #将请求头部分定义为字典，模拟浏览器访问
        headers = {
            'method': 'GET',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'cookie': 'tt_webid=6534988989526164995; tt_webid=6534988989526164995; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=1624330beee15-08d69ca9636016-3f3c5906-1fa400-1624330beef475; tt_webid=6534988989526164995; uuid="w:be7f15122de6474295c4ca397daf17bd"; CNZZDATA1259612802=555149256-1521540822-https%253A%252F%252Fwww.baidu.com%252F%7C1521848634; __tasessionId=qhzjva3g51521852150356'
        }
        #获取详情页源码
        html = requests.get(url, headers=headers)
        #判断访问是否成功
        if html.status_code == 200:
            #成功，返回源码
            return html.text
        return None
    #异常，返回空
    except RequestException:
        return None

#对目标页进行解析，得到图片链接
def parse_page_detail(html):
    #定义一个BeautifulSoup对象，用lxml解析库
    soup = BeautifulSoup(html, 'lxml')
    #将title标签的内容提取出来
    global title
    title = soup.select('title')[0].get_text()
    #定义一个匹配URL所在json数据的正则表达式
    images_pattern = re.compile(r'JSON.parse\((".*")\)', re.S)
    #对详情页源码进行匹配，获得目标数据
    result = re.search(images_pattern, html)
    #通过对JSON数据反序列化，得到python字典对象
    dic = json.loads(json.loads(result.group(1)))
    #取出图片URL
    if dic and 'sub_images' in dic.keys():
        sub_images = dic.get('sub_images')
        images = [item.get('url') for item in sub_images]
        #下载图片
        threads = []
        for image in images:
            t = threading.Thread(target=download_images, args=(image,))
            threads.append(t)
        for thred in threads:
         	thred.start()
        for thred in threads:
         	thred.join()
        return {
            'title': title,
            'images': images
        }


#将图片下载下来
def download_images(url):
    # print('正在下载:', url)
    try:
        response = requests.get(url, timeout=1)
        if response.status_code == 200:
            save_to_local(response.content)
        else:
            return None
    except RequestException:
        return None


#将图片保存到本地
def save_to_local(content):
        num = random.randint(0, 10000)
        file_path_ex = '{0}'.format(r'C:\Users\Ricardo-H\Desktop\头条街拍\%s' %title)
        file_path = file_path_ex.replace(':', '')
        if not os.path.exists(file_path):
            #新建文件夹
            os.makedirs(file_path)
            pic_path = '{0}/街拍{1}.jpg'.format(file_path, num)
            with open(pic_path, 'ab') as f:
                f.write(content)
                f.close()
        else:
             pic_path = '{0}/街拍{1}.jpg'.format(file_path, num)
             with open(pic_path, 'ab') as f:
                f.write(content)
                f.close()


# #主函数
def main():
    res = get_page_index(0, '街拍')
    for url in parse_page_index(res):
        html = get_page_detail(url)
        if html:
            parse_page_detail(html)

#程序入口
if __name__ == '__main__':
    main()
    elapsed = (time.time() - start)
    print(elapsed)
