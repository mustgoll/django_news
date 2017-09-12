import requests
from bs4 import BeautifulSoup
import re
from news.mysqlnews import addinfo
import os
from config import *
url='http://news.baidu.com/'
class news(object):
    def __init__(self):
        self.url=url
        self.news_data=dict()
    @property
    def html(self):
        data = requests.get(self.url).text
        return data
    @property
    def parse_html(self):
        a=re.findall('.*cpOptions_1.data.push([\s\S]*)imgList.push.*',self.html)
        b=a[0].split('cpOptions_1.data.push')
        for index,i in enumerate(b):
            self.news_data['id']=index+1
            self.news_data['urlcontect']=re.search('"title": "([\s\S]+?)",',i).group(1).replace('&quot;','"')+'---'+STATIC_LAST+os.path.basename(re.search('"imgUrl": "([\s\S]+?)",',i).group(1))
            self.news_data['url']=re.search('"url": "([\s\S]+?)",',i).group(1)
            self.news_data['newstype_id']=1
            imgwb=requests.get(re.search('"imgUrl": "([\s\S]+?)",',i).group(1).replace('\\','')).content
            with open(STATIC_DIR+os.path.basename(re.search('"imgUrl": "([\s\S]+?)",',i).group(1)),'wb') as f:
                f.write(imgwb)
            addinfo(self.news_data)
        html=BeautifulSoup(self.html,'lxml')
        lilist=html.select('#pane-news a')[0:20]
        for index,i in enumerate(lilist):
            self.news_data['id']=index+9
            self.news_data['urlcontect']=i.get_text()
            self.news_data['url']=i.get('href')
            self.news_data['newstype_id']=2
            addinfo(self.news_data)







if __name__=='__main__':

    c=news()
    c.parse_html