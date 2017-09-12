import requests
import re
from acfun.acfsql import addinfo
class acf(object):

    def __init__(self):
        self.baseurl='http://www.acfun.cn/'
        self.acfdict=dict()
        self.header={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Host':'www.acfun.cn',

        }
        self.encode_content=self.html()
    def html(self):
        html = requests.get(self.baseurl, headers=self.header)
        if html.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(html.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = html.apparent_encoding
        return html.content.decode(encoding)

    def acfnow(self):
        url1=re.findall(r'm-name="香蕉榜"(.*)clearfix crop-margin hidden',self.encode_content)[0]
        imgurl=re.findall(r'href="(/v/ac[0-9]+?)" data-did=',url1)
        imgsrc=re.findall(r' data-original="(.*?)"',url1)
        imgtitle=re.findall(r'评论:(\d*)">(.*?)</a>',url1)
        id=1
        for x,y,z in zip(imgurl,imgsrc,imgtitle):
            self.acfdict=dict(zip(['url','urlcontent','id'],['http://www.acfun.cn'+x,y+'---'+z[1],id]))
            addinfo(self.acfdict)
            id+=1
    def ranknow(self):
        url1=re.findall(r'm-name="工作情感"(.*?)m-name="动漫文化"',self.encode_content)[0]
        urltop=re.findall(r'<a href="(/a/ac[0-9]+?)" target="_blank" title="(.*?)&#13;UP:',url1)[1:]
        url2=re.findall(r'<div m-id="17" m-name="排行榜" m-type="17" class="module-main"><div class="module-con">(.*?)<ul data-con="2" class="hidden">',self.encode_content)[0]
        urlmid=re.findall(r'i></span><a href="(/v/ac\d*)" title="(.*?)&#13;UP:',url2)
        url3=re.findall(r'<div m-id="63" m-name="排行榜" m-type="17" class="module-main"><div class="module-con">(.*?)<ul data-con="2" class="hidden">',self.encode_content)[0]
        urlfoot=re.findall(r'i></span><a href="(/v/ac\d*)" title="(.*?)&#13;UP:',url3)
        id=11
        for i in urltop+urlmid+urlfoot:
            self.acfdict=dict(zip(['url','urlcontent','id'],['http://www.acfun.cn'+i[0],i[1],id]))
            addinfo(self.acfdict)
            id+=1
if __name__=='__main__':
    a=acf()
    a.ranknow()