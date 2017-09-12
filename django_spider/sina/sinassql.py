import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:@localhost/webspider?charset=utf8",encoding='utf-8', echo=False)

Base = declarative_base()  # 生成orm基类

class news(Base):
    __tablename__ = 'gamelives_sina'  # 表名
    id = Column(Integer, primary_key=True)
    url=Column(String(1000))
    utlstr = Column(String(500))

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
def addinfo(kw):
        Session = Session_class()  # 该出一定要把实例对象加上去否则写入重复的数据后会导致回滚从而暂停程序
        if Session.query(news).get(kw['id']):
            Session.query(news).filter_by(id=kw['id']).update(kw)
        else:
            user_obj = news(utlstr=kw['utlstr'],url=kw['url'])  # 生成创建的数据对象
            Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
        Session.commit()
        Session.close()

if __name__=='__main__':

    addinfo({'url': '"/weibo/%25E8%25BE%259E%25E8%2581%258C%25E5%25A5%25B3%25E6%2595%2599%25E5%25B8%2588%25E6%25B2%25A1%25E5%258E%25BB%25E7%259C%258B%25E4%25B8%2596%25E7%2595%258C&Refer=top"', 'urlcontect': '辞职女教师没去看世界---热', 'id': 1}
)