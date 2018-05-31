#-*_coding:utf8-*-
# 使用GsExtractor类的示例程序
# 访问集搜客论坛，以xslt为模板提取论坛内容
# xslt保存在xslt_bbs.xml中
from urllib import request
from lxml import etree
from GsExtractor import *

# 访问并读取网页内容
url = "http://www.gooseeker.com/cn/forum/7"
conn = request.urlopen(url)
doc = etree.HTML(conn.read())
print(doc)
print("换行\n")


bbsExtra = GsExtractor()    # 生成xsltExtractor对象
bbsExtra.setXsltFromFile("xslt_bbs.xml")    # 调用set方法设置xslt内容
result = bbsExtra.extract(doc)    # 调用extract方法提取所需内容

print(str(result))