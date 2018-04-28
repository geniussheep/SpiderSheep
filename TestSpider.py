#encoding:UTF-8
import urllib.request
import re

url = "https://user.qzone.qq.com/115674440"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)
pQqZoneUrl = re.compile(r'http[s]{0,1}://user.qzone.qq.com/\d]')



for qqZoneUrl in pQqZoneUrl.finditer(data):
    print(qqZoneUrl)