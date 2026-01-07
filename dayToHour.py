# -*- coding: utf-8 -*-
# 一小时计数一次

import os 
from os.path import join, getsize 
import pip
import requests
import json
from urllib.parse import quote, unquote
import feedparser
import time
from datetime import datetime
from bs4 import BeautifulSoup
import pytz


class notification_Model:
    def notificationWeChatToken(self,titleMsg, message):
        url = "https://push.showdoc.com.cn/server/api/push/303b94dcc4ac08927ccbce0e72ad9fec430211407"
        # nowTmp = message
        # if len(regueURL) != 0:
        #     third = quote(regueURL, 'utf-8')
        #     nowTmp = nowTmp + '\n<br /> url:' + third
        payload = {
            "title": titleMsg,
            "content": message,
            "user_token": "12307831fb70e549bb4d5af466858b64839451758"
        }

        # print('payload:', payload)

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

 
    

class fuliba:  
    def netWork(self):
        url = 'https://fuliba2023.net/feed'
        feed = feedparser.parse(url)
        arrContent = []
        for entry in feed['entries']:
            # print(entry.keys())
            oneTime = entry['published']
            print(entry['published'] + '------' + entry['title'] + '------' + entry['link'])
            if self.transformTime(oneTime):
                print('1111111111111111')
                arrContent.append(entry['title'] + '-----:' + entry['link'])
                # notification_Model.notificationWeChatToken2(self=self,titleMsg=entry['title'],message='查看详情', regueURL=entry['link'])
            else:
                print('2222222222222222')

        print('arrContent:', arrContent)
        return arrContent

    def transformTime(self,oneTime):
        # 解析目标时间
        target_time = datetime.strptime(oneTime, "%a, %d %b %Y %H:%M:%S %z")
        
        # 设置目标时区为上海
        target_time = target_time.astimezone(pytz.timezone('Asia/Shanghai'))
        
        # 获取当前时间（上海时区）
        now = datetime.now(pytz.timezone('Asia/Shanghai'))
        
        # 计算时间差
        time_diff = now - target_time
        print('time_diff:',time_diff)
        return time_diff.total_seconds() <= 3600        
    


class juejin:
    def loadData(self,uuid):
        
        urlValueJueJin ='https://api.juejin.cn/content_api/v1/article/query_list?aid=2608&uuid=7351316729601197608&spider=0'
        headers = {
            'accept':'*/*',
            "Content-Type": "application/json",
            'accept-language':'zh-CN,zh;q=0.9',
            'content-type':'application/json',
            'origin':'https://juejin.cn',
            'priority':'u=1, i',
            'referer':'https://juejin.cn/',
            'sec-ch-ua':'"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-site',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
            'x-secsdk-csrf-token':'0001000000018142c0fe5e0687deb4fef31b493dcc253134c075f09cf887ff59ff118343d78c188814669520f224',
        }
        data = {"user_id":uuid,"sort_type":2,"cursor":"0"}
        requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
        s = requests.session()
        s.keep_alive = False # 关闭多余连接
        respose = s.post(url=urlValueJueJin,headers=headers,data=json.dumps(data))
        resultData = respose.json()
        
        print('resultData:', resultData)
        
        arrContent = []
        if resultData['err_no'] == 0 and resultData['err_msg'] == 'success':
            firstData = resultData['data']
            # print(firstData)
            for item in firstData:
                itemID = item['article_id']
                titleValue = item['article_info']['title']
                brief_content = item['article_info']['brief_content']
                cover_image = item['article_info']['cover_image']
                ctime = item['article_info']['mtime']
                # print(self.transformTime2(item['article_info']['mtime']),'---',self.transformTime2(item['article_info']['ctime']))
                if ctime == None:
                    ctime = item['article_info']['ctime']
                createTime = self.transformTime(ctime)
                
                if createTime:
                    # print(titleValue)
                  arrContent.append(titleValue + '-----:' + 'https://juejin.cn/post/' + str(itemID))
                    # notification_Model.notificationWeChatToken2(self=self,titleMsg=titleValue, message='查看详情',regueURL='https://juejin.cn/post/' + str(itemID))
        
            # notification_Model.notificationWeChatToken2(self=self,titleMsg='掘金', message=resultData['err_msg'], regueURL="")
        
        return arrContent

    def transformTime(self,timeString):
        py = pytz.timezone('Asia/Shanghai')
        old_time = datetime.fromtimestamp(float(timeString), py)
        now_time = datetime.now(py)
        totleTime = (now_time - old_time)
        stand_daysTime = totleTime.days
        stand_secondsTime = totleTime.seconds
        hoursTime = int(stand_secondsTime / 3600)
        minsTime = int((stand_secondsTime - hoursTime * 3600) / 60);
        secondsTime = (stand_secondsTime - hoursTime * 3600 - minsTime * 60);
        # print(old_time, '----->',stand_daysTime, '---',stand_secondsTime, '---',hoursTime, '---',minsTime, '---',secondsTime)
        # print(old_time, '----->', stand_secondsTime, '----->', stand_daysTime)
        if stand_secondsTime <= 3600 and stand_daysTime == 0:
            # print('--------->')
            return True
        else:
            return False
    
    def transformTime2(self,timeString):
        py = pytz.timezone('Asia/Shanghai')
        old_time = datetime.fromtimestamp(float(timeString), py)
        return old_time

        

class result_model:
    def total_func():
        arrOne = []
        arrOne = fuliba().netWork()
        # arr_uuids = ['1574156384091320', '3483683111318823', '2946346894759319', '53218623894222','1139531179102392','1063982986187486','3298190611978526']
        
        # arrSecond = []
        # for item in arr_uuids:
        #     arrThird = juejin().loadData(item)
        #     arrSecond.extend(arrThird)
        #     time.sleep(10)
        # title = '文章更新汇总'
        
        # if len(arrOne) == 0:
        #     title = '知乎文章更新'
        # if len(arrSecond) == 0:
        #     title = '掘金文章更新'
        # arrLast = arrOne+arrSecond
        # content = '\n'.join(arrLast)

        # if len(arrLast) != 0:
        #     notification_Model.notificationWeChatToken(notification_Model, title, content)
            
             

def main_handler(event, context):
    result_model.total_func()
    
    
if __name__ == '__main__':
    print('')
    # result_model.total_func()
    # notification_Model.notificationWeChatToken(notification_Model,'正在进行测试22', '在此关系图中，\n\n您可以看到刚刚创建的工作流程文件，以及 GitHub Actions 组件在层次结构中的组织方式。 每个步骤执行单个操作或 shell 脚本。 步骤 1 和 2 运行操作，步骤 3 和 4 运行 shell 脚本。 若要为工作流查找更多预生成的操作，')
    # notification_Model.notificationWeChatToken('1', '2', '2')

result_model.total_func()