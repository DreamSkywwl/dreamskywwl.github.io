# -*- coding: utf-8 -*-
import datetime
import requests


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
        print('showdoc Status:' + response.text)
    

# 获取当前日期和时间
now = datetime.datetime.now()

# 提取年月日时分秒
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
timeINvalue = 'dreamskywwl.github.io: {}-{}-{} {}:{}:{}'.format(year,month,day,hour,minute,second)
print(timeINvalue)
notification_Model.notificationWeChatToken(notification_Model,titleMsg='更新时间', message=timeINvalue)