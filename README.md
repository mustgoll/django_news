# 实例网站(test)

## 备注
个人工作之余搭建的小网站，网站性质为非商业用途，主要目的是为正在学
习python web框架的同学们提供参考及实践。
模块结构：爬虫模块django_spider和django项目。各自独立运行，互补影响，通过Mysql交接  
前端部分主要通过bootstrap框架+ajax快速开发，界面最简化，至于观赏性，请忽略-，-
后端部分通过django+mysql+spider组成，由爬虫爬取相关网站的数据
储存至数据库，通过django模版引擎解析至前端网页。
线上结构:django+uwsgi+ngnix
#####声明：网站内容为第三方网站获取，只能作为学习交流，非商业用途

### 安装Python

至少Python3.5以上

### 安装Msql

安装好之后将Mysql服务开启，并前往django.settings配置

### 配置网站爬虫模块

```
cd django_spider
```

进入django_spider 目录，配置config文件，由于baidu图片url
设置了同源策略，无法通过img.src获取图片，改为将图片下载存放在
静态文件目录下调用，A、D、N、S分辨代表了爬取4个网站间隔时间，
由于爬取4个不同的网站，开启了多进程模式，被封ip的机率很小，
该爬虫为理想状态下的爬取，未做过多的异常处理，请自行增加。
* 运行
```
run.py
```
###安装依赖

```
pip install requests
pip install django
pip install sqlalchemy
pip install Beautfulsoup
pip install pymysql
```

####django模块

    请使用manage.py创建数据库相关表单
    安装相关依赖库开始运行


## 项目参考

[https://github.com/](https://github.com/)
