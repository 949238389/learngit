#-*-coding:utf8-*-
import requests
import re
import sys
#print sys.getdefaultencoding()

html = requests.get('http://zhixing.bjtu.edu.cn/forum-624-1.html')
jianzhi = re.findall('class="s xst">(.*?)</a>',html.text,re.S)
chinese = u'数据挖掘|Python'

print chinese

for each in jianzhi:
    if not re.search(chinese,each) is None:
        print each
