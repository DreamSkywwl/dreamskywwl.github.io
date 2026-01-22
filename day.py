# -*- coding: utf-8 -*-
# 一天计数一次
import json
from urllib.parse import quote, unquote
import datetime
import time

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
            time.sleep(2)
            notification_Model.notificationWeChatToken(notification_Model,"微信公众号系统公告", item_title)
        else:
            print(item_title)
            # notification_Model().notificationToken(item_title, item_time)
        
        
        # if resultStrring:
        #    resultSimple = resultStrring.find('li', id = 'mp_news_item')

    def timeTransform(self):
        today = datetime.date.today()
        # 3.计算昨天的日期
        yesterday = today - datetime.timedelta(days=1)
        return yesterday



class notification_Model:
   
    def notificationWeChatToken(self,titleMsg, message):
        url = "https://push.showdoc.com.cn/server/api/push/303b94dcc4ac08927ccbce0e72ad9fec430211407"
        
        payload = {
            "title": titleMsg,
            "content": message,
            "user_token": "12307831fb70e549bb4d5af466858b64839451758"
        }
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "priority": "u=1, i",
            "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        }

        response = requests.post(url, headers=headers, data=payload)
        notification_Model().notificationWeChatToken2(titleMsg)
        print(response.text)
    
    def notificationWeChatToken2(self,titleMsg, ):
        
        url = "https://api.letserver.run/message/info?token=cq0mkh8jn87bju92b0ag&msg=" + titleMsg
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.get(url, headers=headers)

        print(response.text)

 

 

def handler():
    d1 = datetime.datetime.now();
    d2 = datetime.datetime(2021, 2, 17);
    d3 = datetime.datetime(2024, 5, 16);
    d4 = (d1 - d2).days + 1; # 在一起多久
    d5 = (d1 - d3).days + 1; # 孩子已经多少天
    msg = 'Tips: 认识晓粉已经' + str(d4) + '天'
    msg2 = 'Tips: 孩子已经' + str(d5) + '天'
    print(msg)
    notification_Model.notificationWeChatToken(notification_Model,titleMsg='宝宝' + str(d5) + '天', message=msg + '<br />\n' + msg2)
    # notification_Model.notificationWeChatToken(notification_Model,titleMsg='AAA宝宝' + str(d5) + '天', message=msg + '<br />\n' + msg2)
    weChat_listening().requestURL()
  
handler()
if __name__ == '__main__':
    # handler()
    print('')
    '''
    d1 = datetime.datetime.now();
    d2 = datetime.datetime(2021, 2, 17);
    d3 = datetime.datetime(2024, 5, 16);
    d4 = (d1 - d2).days + 1; # 在一起多久
    d5 = (d1 - d3).days + 1; # 孩子已经多少天
    msg = 'Tips: 认识晓粉已经' + str(d4) + '天'
    msg2 = 'Tips: 孩子已经' + str(d5) + '天'
    print(msg)
    notification_Model.notificationWeChatToken(notification_Model,titleMsg='宝宝' + str(d5) + '天', message=msg + '<br />\n' + msg2)
    # notification_Model.notificationWeChatToken(notification_Model,titleMsg='AAA宝宝' + str(d5) + '天', message=msg + '<br />\n' + msg2)
    weChat_listening().requestURL()

    '''