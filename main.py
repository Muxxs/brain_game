#coding=utf-8

#baidu
import urllib2,os,time
import urllib
from aip import AipOcr
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
User_Agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
url = "https://www.baidu.com/s?wd="

import urllib
import urllib2
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        print 1
        return fp.read()

def threading_str(html,words):
    #time_start=time.time()
    print words, html.count(words)
    #time_emd=time.time()
    #print words,time_emd-time_start

def baidu(words,an):
    global User_Agent
    global url
    key = words
    key_code = urllib.quote(key)
    url_all = url + key_code
    req = urllib2.Request(url_all)
    req.add_header('User-Agent', User_Agent)
    data = str(urllib2.urlopen(req).read())
    #an_=[]
    #text_replace=["<br>","</br>",""]
    #data=data.replace(" ","")
    print "result:"
    for i in an:
        import threading
        t1=threading.Thread(target=threading_str,args=(data,i))
        t1.start()
def start(n):
    time_start = time.time()
    num=str(n)
    #这里地址要自己测试
    os.system("adb shell screencap -p /sdcard/"+num+".png")
    #这里可能要加个延时
    os.system("adb pull /sdcard/"+num+".png")
    print os.system("mv ~/"+num+".png ~/Desktop/ask-question/"+num+".png")
    image = get_file_content("/Users/wangjiao/Desktop/ask-question/"+num+'.png')
    """ 调用通用文字识别（含位置高精度版） """
    res=client.accurate(image)
    question=""
    an=[]
    time_end = time.time()
    print "上传",time_end - time_start,
    print "s"
    for i in res['words_result']:
        words=i['words'].encode('utf-8')
        width=i['location']['width']
        top=i['location']['top']
        left=i['location']['left']
        height=i['location']['height']

        #随便拿一个手机测试的，具体数据自己试

        if top<=600 and top>=500 and left>43 and height>40:
            question=question+words
        elif top>=600 and left<622 and left>43 and height>40:
            for x in words.split(" "):
                an.append(x)
    baidu(question,an)
    time_end = time.time()
    print time_end - time_start,
    print "s"

i=False
while i==False:
    type=raw_input("输入任何内容开始：")
    start(str(type))
