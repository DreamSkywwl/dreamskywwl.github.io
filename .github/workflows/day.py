# -*- coding: utf-8 -*-
import json
from urllib.parse import quote, unquote
import datetime


import requests
from bs4 import BeautifulSoup
import urllib.request


class weChat_listening:
    def requestURL(self):
        wechat_URL = 'https://mp.weixin.qq.com/cgi-bin/announce?action=getannouncementlist&lang=zh_CN'
        wechat_Header = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        }
        
        responseValue = requests.get(url=wechat_URL,headers=wechat_Header)
        # print(responseValue.text)
        beautifulSoup = BeautifulSoup(responseValue.text, 'html.parser')
        resultStrring = beautifulSoup.find('li', class_ = 'mp_news_item')
        
        item_title = resultStrring.select('strong')[0].get_text()
        item_time = resultStrring.select('span')[0].get_text()
        yes_time = self.timeTransform()
        print(str(yes_time) + '-----' + item_time)
        if item_time in str(yes_time):
            print(item_title)
            notification_class().notificationToken("微信公众号系统公告", item_title)
        else:
            print(item_title)
            # notification_class().notificationToken(item_title, item_time)
        
        
        # if resultStrring:
        #    resultSimple = resultStrring.find('li', id = 'mp_news_item')

    def timeTransform(self):
        today = datetime.date.today()
        # 3.计算昨天的日期
        yesterday = today - datetime.timedelta(days=1)
        return yesterday



class notification_class:
    # 钉钉机器人的调用
    def dingdingTalk(self,msg):
        HEADERS = {"Content-Type": "application/json;charset=utf-8"}
        key = "e9b59afdcad471cd70b8e4016f2752a03084d66c34abea961f2ebf8a3d785a30"
        url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % key
        data_info = {
            "msgtype": "text",
            "text": {
                # "content": "Log: \n" + msg
                "content": msg
            },
            "isAtAll": True
        }

        value = json.dumps(data_info)
        response = requests.post(url, data=value, headers=HEADERS)

    def notificationToken(self,titleMsg, message):
    # tkoen = 'WwuUQD5ZNv7Aq9A67AswCN'#晓粉的
        tkoen = 'eJYzQEezv5JtJeR6mDQfVG'  # 我的
        first = urllib.parse.quote(titleMsg, 'utf-8')
        second = urllib.parse.quote(message, 'utf-8')
        nowTmp = 'https://api.day.app/{}/{}/{}'.format(tkoen, first, second)
        print(nowTmp)
        res = requests.post(nowTmp)

        if res.json()['code'] == 200:
            print('发送成功')
        else:
            print(res.text)
    def notificationWeChatToken(self,titleMsg, message):
        url = "https://api.anpush.com/push/UUW4N522SA4JRHQQT9RH1I5Z21MMP4"

        payload = {
            "title": titleMsg,
            "content": message,
            "channel": "63552"
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        print(url)
        response = requests.post(url, headers=headers, data=payload)
        print(response.status_code)
        notification_class().notificationWeChatToken2(titleMsg, message)
        print(response.text)
    def notificationWeChatToken2(self,titleMsg, message):
        url = "https://api.letserver.run/message/info?token=cq0mkh8jn87bju92b0ag&msg=" + titleMsg
        print(url)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.get(url, headers=headers)

        print(response.status_code)
        print(response.text)

 

def handler(event, context):
    d1 = datetime.datetime.now();
    d2 = datetime.datetime(2021, 2, 17);
    d3 = datetime.datetime(2024, 5, 16);
    d4 = (d1 - d2).days + 1; # 在一起多久
    d5 = (d1 - d3).days + 1; # 孩子已经多少天
    msg = 'Tips: 认识晓粉已经' + str(d4) + '天'
    msg2 = 'Tips: 孩子已经' + str(d5) + '天'
    # notification_class().notificationWeChatToken(titleMsg='宝宝' + str(d5) + '天', message=msg + '<br />\n' + msg2)
    notification_class().notificationWeChatToken2(titleMsg='宝宝' + str(d5) + '天', message=msg + '<br />\n' + msg2)
    weChat_listening().requestURL()
  

if __name__ == '__main__':
    # handler()
    d1 = datetime.datetime.now();
    d2 = datetime.datetime(2021, 2, 17);
    d3 = datetime.datetime(2024, 5, 16);
    d4 = (d1 - d2).days + 1; # 在一起多久
    d5 = (d1 - d3).days + 1; # 孩子已经多少天
    msg = 'Tips: 认识晓粉已经' + str(d4) + '天'
    msg2 = 'Tips: 孩子已经' + str(d5) + '天'
    print(msg)
    # notification_class().notificationWeChatToken(titleMsg='宝宝' + str(d5) + '天', message=msg + '<br />\n' + msg2)
    notification_class().notificationWeChatToken2(titleMsg='AAA宝宝' + str(d5) + '天', message=msg + '<br />\n' + msg2)
    # weChat_listening().requestURL()





d1 = datetime.datetime.now();
d2 = datetime.datetime(2021, 2, 17);
d3 = datetime.datetime(2024, 5, 16);
d4 = (d1 - d2).days + 1; # 在一起多久
d5 = (d1 - d3).days + 1; # 孩子已经多少天
msg = 'Tips: 认识晓粉已经' + str(d4) + '天'
msg2 = 'Tips: 孩子已经' + str(d5) + '天'
print(msg)
    # notification_class().notificationWeChatToken(titleMsg='宝宝' + str(d5) + '天', message=msg + '<br />\n' + msg2)
notification_class().notificationWeChatToken2(titleMsg='AAA宝宝' + str(d5) + '天', message=msg + '<br />\n' + msg2)
    # weChat_listening().requestURL()