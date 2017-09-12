import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:@localhost/webspider?charset=utf8",encoding='utf-8', echo=False)

Base = declarative_base()  # 生成orm基类

class news(Base):
    __tablename__ = 'gamelives_lives'  # 表名
    id = Column(Integer, primary_key=True)
    url=Column(String(200))
    urlcontent = Column(String(300))

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
def addinfo(kw):
        Session = Session_class()  # 该出一定要把实例对象加上去否则写入重复的数据后会导致回滚从而暂停程序
        if Session.query(news).get(kw['id']):
            Session.query(news).filter_by(id=kw['id']).update(kw)
        else:
            user_obj = news(urlcontent=kw['urlcontent'],url=kw['url'])  # 生成创建的数据对象
            Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
        Session.commit()
        Session.close()

if __name__=='__main__':

    addinfo({'url': 'http://www.douyu.com/102411', 'urlcontent': 'https://rpic.douyucdn.cn/acrpic/170911/102411_1900.jpg---三笠ackerman丶1  在线人数:61426'})