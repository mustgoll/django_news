import requests
import re
from sina.sinassql import addinfo
from bs4 import BeautifulSoup
class sina(object):

    def __init__(self):
        self.baseurl='http://s.weibo.com/top/summary'
        self.newnowdict=dict()

    def newnow(self):
        cate='cate=realtimehot'
        html=requests.get(self.baseurl,params=cate).text
        patter=re.compile(r'"<div class=\\"hot_ranklist\\">\\n(.*?)\\n<\\/div>\\n<!-- share hot_band -->')
        soup=BeautifulSoup(patter.search(html).group(1),'lxml')
        for index,dom in enumerate(soup.find_all('p',class_=r'\"star_name\"')):
            self.newnowdict['url']='http://s.weibo.com'+dom.find('a').get('href').encode().decode('unicode_escape').replace('\\','').replace('"','')
            mid=dom.a.get_text().encode().decode('unicode_escape').split('\n')
            lll=[]
            for i in mid:
                if i and not i.isspace():
                    lll.append(i.strip())
            self.newnowdict['utlstr']='---'.join(lll)
            self.newnowdict['id']=index+1
            addinfo(self.newnowdict)

if __name__=='__main__':
    a=sina()
    a.newnow()