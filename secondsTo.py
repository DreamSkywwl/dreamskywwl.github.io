
# -*- coding:utf-8 -*-
#coding=utf-8

import requests
import time
 



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
        requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
        s = requests.session()
        s.keep_alive = False # 关闭多余连接
        # s.proxies = {"https": "47.100.104.247:8080", "http": "36.248.10.47:8080", }
        response = s.post(url, headers=headers, data=payload)
        print(response.text)


timeValue = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
notification_Model.notificationWeChatToken(notification_Model, timeValue,'理论是正确的，然后呢？一实操就完蛋。其实托洛茨基的不断革命论和斯大林的一国建成社会主义，都是半斤八两。苏联在冷战中也是不断输出革命，苏联解体直接原因就是加盟共和国造反。托洛茨基最大的问题就在于他自始至终没有将自己的理论，上升到党的意志。列宁曾建议托洛茨基担任人民委员会副主席、内务人民委员。人民委员会是苏联最高行政机构主席是列宁，继任者是斯大林。内务人民委员会掌管警察内卫，而下属机构“契卡”，在后来发展成为大名鼎鼎的间谍机构“克格勃”。现任俄罗斯总统普京的老东家。作者：逐风\n链接：https://www.zhihu.com/question/10705032349/answer/1931226581239588709 \n来源：知乎\n著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。')
    