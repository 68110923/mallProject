import requests
from lxml import etree
import re
import time

def get_url():
    host='https://www.1688mk.com'
    for i in range(2,3517):
        url=f'https://www.1688mk.com/move/3/index_{i}.html'
        req=requests.get(url)
        text=req.content.decode('utf-8')
        urllist=re.findall('<li><a href="(.*?)" target="_blank"><img src=".*?"/><h3>(.*?)</h3><span',text)
        print(len(urllist))
        for i in urllist:
            name=i[1]
            movepath=host+i[0]
            print(name,movepath)
            with open('链接3.txt','a',encoding='utf-8') as f:
                f.write(f'{name}:{movepath}\n')

def de():
    with open('链接3.txt','r',encoding='utf-8') as f:
        for i in f.readlines():
            line=re.findall('(.*?):(https://.*)',i)[0]
            req=requests.get(line[1])
            deurl=re.findall('<td bgcolor=".*?"><a target="_blank" href="(.*?)" ><b><font color=".*?">影片下载\[鼠标右键另存为\]</font>',req.content.decode('utf-8'))[0]
            print(line[0],'------',line[1],'------',deurl)
            # req=requests.get(deurl)
            with open('视频链接3.txt','a',encoding='utf-8') as f:
                f.write(f'{deurl}\n')

de()