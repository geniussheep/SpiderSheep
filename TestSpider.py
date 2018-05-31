#encoding:UTF-8
import os,re,gzip,time
import urllib.request,urllib.parse
import http.cookiejar
from selenium import webdriver
from  lxml import etree

url = "https://user.qzone.qq.com/115674440"

requestHeader = {
# ":authority": "user.qzone.qq.com",
# ":method": "GET",
# ":path": "/115674440",
# ":scheme": "https",
# 'Connection': 'Keep-Alive',
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-CN,zh;q=0.9",
"cache-control": "max-age=0",
"cookie": "pt2gguin=o0115674440; RK=NeSNR1mUUe; ptcz=5a37e7677dd4b29030ec20deef034bcd743163c16395ef32e0719bb3509f4161; pgv_pvid=8493980150; o_cookie=115674440; pac_uid=1_115674440; tvfe_boss_uuid=c31e6bd58954be5d; pgv_pvi=4755230720; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; __Q_w_s__QZN_TodoMsgCnt=1; Loading=Yes; scstat=3; _qpsvr_localtk=0.2378570669931539; pgv_si=s4457470976; uin=o0115674440; skey=@X0unr9aGo; ptisp=cnc; p_uin=o0115674440; pt4_token=0C6puHPQaY7mKgjvUGbZKza7Wc64CNI0Z7AdPKGiedY_; p_skey=XNIa0NcDxSLBVmpnnlmLGeCpuGiGxHvqsXnXUe84wo4_; fnc=2; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; pgv_info=ssid=s9950738200; cpu_performance_v8=9; qzmusicplayer=qzone_player_115674440_1525343410841",
"if-modified-since": "Thu, 03 May 2018 10:30:09 GMT",
"referer": "https://qzs.qq.com/qzone/v5/loginsucc.html?para=izone",
"upgrade-insecure-requests": "1",
"user-agent": "ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

def ungzip(data):
    try:  # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data

# driver = webdriver.Chrome()
# #开始加载
# driver.get(url)
# #等待2秒，更据动态网页加载耗时自定义
# time.sleep(2)
# # 获取网页内容
# content = driver.page_source.encode('utf-8')
# # 获取docment
# doc = etree.HTML(content)
# print(doc);

opener = getOpener(requestHeader)
data = opener.open(url).read()
data = ungzip(data)
print(data);

pQqZoneUrl = re.compile(r'http[s]{0,1}://user.qzone.qq.com/\d')
for qqZoneUrl in pQqZoneUrl.finditer(data):
    print(qqZoneUrl)