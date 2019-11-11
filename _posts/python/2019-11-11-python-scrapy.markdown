---
layout: post
title: "Scrapy笔记01"
date: 2019-11-11 
tags: Python solution basis
---



Python爬虫框架:Scrapy入门
Scrapy是一个为了爬取网站数据,提取结构性数据而编写的应用框架.它使用Twisted这个异步网络库来处理网络通讯,架构清晰,并且包含了各种中间件接口,可以灵活的完成各种需求.个人认为Scrapy是Python世界里面最强大的爬虫框架,没有之一,它比BeautifulSoup更加的完善,BeautifulSoup可以说是轮子,而Scrapy则是车子,不需要你关注太多的细节.Scrapy不仅支持Python2.7,Python3也支持.

安装:
pip install scrapy -> VC++14.0 Twisted
解决方法:离线安装 pip install xxx.whl

scrapy bench 如果成功了才代表真的安装成功,别的花里胡哨都没有用

Scrapy Engine(引擎): 重中之重,负责

### Scrapy结构图
![scrapy_structure](/images/posts/python/scrapy_structure.png)