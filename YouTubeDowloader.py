#!/usr/bin/python
#-*-coding:gbk-*-
from animation import running
from pytube import YouTube
import urllib2
import re
import os
import time
from  bs4 import BeautifulSoup
import uuid
import sys
import platform
reload(sys)
sys.setdefaultencoding('gbk')
def downloadOne(dlUrl):
    reponse = urllib2.urlopen(dlUrl)
    htmlstr = reponse.read()
    soup = BeautifulSoup(htmlstr, 'lxml')
    print("begining download  video:----"+soup.title.text.replace(" ",""))
    fileid = str(uuid.uuid1())
    if downloadfbv=="4":
         YouTube(dlUrl).streams.first().download(output_path=downloadDct,filename=fileid)
         os.rename(downloadDct + "/"+fileid+".mp4",downloadDct + "/"+soup.title.text.replace(" ","")+".mp4")
    elif downloadfbv=="5":
         YouTube(dlUrl).streams.filter(mime_type="video/mp4",res="360p").first().download(output_path=downloadDct,filename=fileid)
         os.rename(downloadDct + "/"+fileid+".mp4",downloadDct + "/"+soup.title.text.replace(" ","")+".mp4")
    elif downloadfbv=="3":
        fileid2=str(uuid.uuid1())
        YouTube(dlUrl).streams.filter(mime_type="video/webm", res="1080p").first().download(output_path=downloadDct,
                                                                                                filename=fileid)
        YouTube(dlUrl).streams.filter(mime_type="audio/webm",abr="128kbps").first().download(
            output_path=downloadDct,
            filename=fileid2)
        print(os.getcwd()+
            "/ffmpeg/bin/ffmpeg -i " + downloadDct + "/" + fileid2 + ".webm -i " + downloadDct + "/" + fileid + ".webm -f mp4 -y " +downloadDct+"/"+ soup.title.text.replace(" ","") + ".mp4")
        os.system(
            os.getcwd()+
            "/ffmpeg/bin/ffmpeg -i " + downloadDct + "/" + fileid2 + ".webm -i " + downloadDct + "/" + fileid + ".webm -f mp4 -y " +downloadDct+"/"+ soup.title.text.replace(" ","") + ".mp4")
        if isLinux():
            os.system("rm -rvf " + downloadDct.replace("/","//")+ "//" + fileid + ".webm")
            os.system("rm -rvf " + downloadDct.replace("/","//")+ "//"  + fileid2 + "webm")
        else:
            os.system("del " + downloadDct.replace("/","//")+ "//"  + fileid + ".webm")
            os.system("del " + downloadDct.replace("/","//")+ "//" + fileid2 + ".webm")
    elif downloadfbv=="2":
        fileid2 = str(uuid.uuid1())
        YouTube(dlUrl).streams.filter(mime_type="video/webm", res="1440p").first().download(
            output_path=downloadDct,
            filename=fileid)
        YouTube(downloadUrl).streams.filter(mime_type="audio/webm", abr="128kbps").first().download(
            output_path=downloadDct,
            filename=fileid2)
        os.system(
            os.getcwd()+
            "/ffmpeg/bin/ffmpeg -i " + downloadDct + "/" + fileid2 + ".webm -i " + downloadDct + "/" + fileid + ".webm -f mp4 -y " +downloadDct+"/"+ "hello" + ".mp4")
        if isLinux():
            os.system("rm -rvf " + downloadDct.replace("/","//")  +"\\"+ fileid + ".webm")
            os.system("rm -rvf " + downloadDct.replace("/","//")+ "\\" + fileid2 + ".webm")
        else:
            os.system("del " +downloadDct.replace("/","//")+ "\\"   + fileid + ".webm")
            os.system("del " + downloadDct + "/" + fileid2 + ".webm")
    elif downloadfbv == "1":
        fileid2 = str(uuid.uuid1())
        YouTube(downloadUrl).streams.filter(mime_type="video/webm", res="2160p").first().download(
            output_path=downloadDct,
            filename=fileid)
        YouTube(dlUrl).streams.filter(mime_type="audio/webm", abr="128kbps").first().download(
            output_path=downloadDct,
            filename=fileid2)
        os.system(os.getcwd()+
            "/ffmpeg/bin/ffmpeg -i " +downloadDct+"/"+ fileid2 + ".webm -i " +downloadDct+"/"+ fileid + ".webm -f mp4 -y " +downloadDct+"/"+ soup.title.text.replace(" ","") + ".mp4")
        if isLinux():
            os.system("rm -rvf "+downloadDct.replace("/","//")+ "\\"+fileid+".webm")
            os.system("rm -rvf "+downloadDct.replace("/","//")+ "\\" +fileid2+".webm")
        else:
            os.system("del "+downloadDct.replace("/","//")+ "\\" +fileid+".webm")
            os.system("del " +downloadDct.replace("/","//")+ "\\" + fileid2 + ".webm")
def downloadYTB(selectNum):

    if selectNum=="1":
       try:
          downloadOne(downloadUrl)
       except:
           print("download error")
    elif selectNum=="3":
        f = open("./downloadUrl.txt", 'r+')
        for line in f.readlines():
            if not line == '\n':
                if line[0] == 'h':
                    try:
                        downloadOne(str(line.strip('\n')))
                    except:
                        print("download error")
    else:
        reponse = urllib2.urlopen(downloadUrl)
        htmlstr = reponse.read()
        soup = BeautifulSoup(htmlstr, 'lxml')
        # print soup.prettify()
        # print soup.children.next()
        for i in soup.find_all(href=re.compile("watch"),
                               class_="yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2"):
            # print i
            hrefvalue = re.findall(r'href="(.*?)" rel="nofollow" title="(.*?)"', str(i), re.I)
            try:
             downloadOne("https://www.youtube.com/"+hrefvalue[0][0])
            except:
                print("download error")



if __name__ == '__main__':
    running.start()
    print("油管下载器，作者:Hitsme,版本V0.1")
    selectNum = ""
    downloadUrl = ""
    downloadDct = ""
    downloadfbv = ""
    while True:
        selectNum = raw_input("选择下载模式 :\n 1.单个视频下载\n 2.批量下载（目前只能下载一个youtuber频道主页前30个视频，后续解决）\n 3.批量下载txt文件链接\n\n输入选择序号:")

        if selectNum == "1":
            print("当前选择下载模式为单个视频下载, 请输入下载链接, 例如:https://www.youtube.com/watch?v=mmdSNDK7Ovk")
        elif selectNum == "2":
            print("当前选择下载模式为批量下载视频，请输入下载链接，例如:https://www.youtube.com/channel/UCoC47do520os_4DBMEFGg4A/videos")
        elif selectNum=="3":
            print("当前选择批量下载txt链接，请在downloadUrl.txt添加下载链接")
        else:
            print("输入有误，请重新输入!")
            continue
        if selectNum!="3":
          downloadUrl = raw_input("输入你的下载链接:")
        downloadDct = raw_input("输入下载存放目录:")
        downloadfbv = raw_input(
            "输入下载视频分辨率（高于1080p视频需要视频和音频做合并，速度会慢，电脑配置低请下载1080p以下的视频）:\n1.4k\n2.2k\n3.1080p\n4.720p\n5.360p\n\n输入你要下载分辨率序号:")
        break


    def isLinux():
        print(platform.platform())
        if str(platform.platform()).index("Windows") > -1:
            return False
        else:
            return True
    downloadYTB(selectNum)
    time.sleep(50)