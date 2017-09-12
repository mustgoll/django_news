import requests
import re
from douyuTV.livesql import addinfo
import json
class live(object):

    def __init__(self):
        self.baseurl='http://open.douyucdn.cn/api/RoomApi/live/lol'
        self.douyudict=dict()
        self.header={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8',
        }
    def html(self):
        html = requests.get(self.baseurl, headers=self.header).text
        loljson=json.loads(html).get('data')
        id=1
        for item in loljson:
            self.douyudict['id']=id
            self.douyudict['url']=item.get('url')
            self.douyudict['urlcontent']=item.get('room_src')+'---'+item.get('nickname')+'  在线人数:'+str(item.get('online'))
            addinfo(self.douyudict)
            id+=1


if __name__=='__main__':
    a=live()
    a.html()