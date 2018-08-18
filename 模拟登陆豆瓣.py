import requests
import re

# sson = requests.session()
def simu_login():
    headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    data = {
        'source': 'None',
        'redir': 'https://www.douban.com',
        'form_email': 13548644245,
        'form_password': 'dblh5832',
        'captcha_solution': '',
        'captcha_id': '',
        'login': u'登录'
    }
    response = requests.get('https://accounts.douban.com/login?', headers=headers)
    html = response.text
    captcha_id = re.findall('<input type="hidden" name="captcha-id" value="(.*?)"/>', html)[0]
    print(captcha_id)
    captcha_url = 'https://www.douban.com/misc/captcha?id={}&size=s'.format(captcha_id)
    result = requests.get(captcha_url)
    with open('captcha.jpg', 'wb+') as f:
        f.write(result.content)
    captcha_solution = input('请输入验证码：')
    data['captcha-solution'] = captcha_solution
    data['captcha-id'] = captcha_id
    print(data)
    res = requests.post(url='https://accounts.douban.com/login?', data=data, headers=headers)
    print(res.status_code)
    # print(res.text)
    with open('xx.html', 'w', encoding='utf-8') as f:
        f.write(res.text)
simu_login()
