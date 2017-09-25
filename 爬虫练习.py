import requests
from bs4 import BeautifulSoup
import re
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillBossinfo(blist,html):
	soup=BeautifulSoup(html,"html.parser")
	for b in soup.find_all("div",class_="job-primary"):

		d = re.compile(r'<h3 class=\"name\">.*?<')
		pos = d.findall(str(b))[0][17:-1]#正则,需将原tag变为str再检索

		sal = b.span.string

		com = b.find('div',class_="info-comapny")
		e = re.compile(r'<h3 class.*?<')
		com2 = e.findall(str(com))[0][17:-1]#注意findall后结果[0],为第一个结果。

		blist.append([com2,pos,sal])

def printBossList(blist, num):
	tplt = "{0:^5}\t{1:^10}\t{2:^10}"#定义format函数顶头标题宽度，\t为制表符
	print(tplt.format("公司","职位","薪水",chr(12288))) #chr(12288)表明，中文字符宽度不够时，采用中文空格填充，可保证中文对齐
	for i in range(num):
		b=blist[i]
		print(tplt.format(b[0],b[1],b[2],chr(12288)))#中英文混编的对齐 chr(12288)无法解决


def main():
	#page = input('请输入要查询的网页数：')
	url = "http://www.zhipin.com/c101020100/h_101020100/?query=python&page=2"
	binfo = []
	html = getHTMLText(url)
	fillBossinfo(binfo, html)
	printBossList(binfo, 15)
main()
