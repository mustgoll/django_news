from acfun.acfunmain import acf
from douyuTV.livemain import live
from news.baidumain import news
from sina.sinamain import sina
from config import *
from multiprocessing import Process
import time

def p1():
    while True:
        a=acf()
        a.acfnow()
        a.ranknow()
        print('更新A站成功 updatetime:%s' % time.strftime('%Y/%m/%d %H:%M'))
        time.sleep(A)
def p2():
    while True:
        a=live()
        a.html()
        print('更新游戏直播成功 updatetime:%s' % time.strftime('%Y/%m/%d %H:%M'))
        time.sleep(D)

def p3():
    while True:
        a=news()
        a.parse_html
        print('更新百度新闻成功 updatetime:%s' % time.strftime('%Y/%m/%d %H:%M'))
        time.sleep(N)

def p4():
    while True:
        a=sina()
        a.newnow()
        print('更新微博排行成功 updatetime:%s' % time.strftime('%Y/%m/%d %H:%M'))
        time.sleep(S)

if __name__=='__main__':

    acf=Process(target=p1)
    acf.start()
    live=Process(target=p2)
    live.start()
    news=Process(target=p3)
    news.start()
    sina=Process(target=p4)
    sina.start()
    sina.join()






