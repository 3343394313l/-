from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import re
import winsound
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import subprocess
from os import system as clr
#----------------------------------------------------------------------------------------------超级屎山代码 值得拥有
def panduan3():
    global smdm,runmode
    if(runmode==3):
        try:
            s(0.2)
            ul_element = dr.find_element(By.CLASS_NAME, "prev_ul.clearfix")
            li_elements = ul_element.find_elements(By.TAG_NAME, "li")
            if (len(li_elements) == 3 and  "active" in li_elements[0].get_attribute("class")):  # 判断第一个 li 是否有 active 类名
                cl(li_elements[1])      
            smdm+='Y'
        except:
            smdm+='E'
def what_time(start_time):
    now = datetime.now()
    time_difference = now - start_time
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    result = []
    if hours > 0:
        result.append(f"{hours}h")
    if minutes > 0:
        result.append(f"{minutes}m")
    result.append(f"{seconds}s")
    return ' '.join(result)
def pand(x,y):
    while(1):
        try:
            a=dr.find_element(By.XPATH,x).text
            if(a==y):
                cl(f(x))
                break
        except:
            pass
        s(0.1)
#element = driver.find_element_by_link_text("课程")
def pandwb():
    while(1):
        try:
            a=dr.find_element(By.XPATH, "//*[@title='课程']")
            cl(a)
            break
        except:
            pass
    s(0.1)
def q():
    clr('cls')
js_codejh = """
const xpaths = [
    '/html/body/div[6]/div/div[1]/h2',
    '/html/body/div[6]/div/div[1]',
    '//*[@id="selector"]/div[3]/div[1]',
    '/html/body/div[7]/div[3]/div/div[1]/div[1]',
    '//*[@id="selector"]/div[2]'
];

xpaths.forEach(xpath => {
    const element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (element) {
        element.remove();
    }
});
"""

s=time.sleep
import keyboard
def huiche():
    keyboard.wait('enter')  
def cl(x):
    dr.execute_script("arguments[0].click();", x)
def f(x):
    return dr.find_element(By.XPATH,x)
import sys
def bof():
    global smdm
    panduan3()
    try:
        iframe1 = WebDriverWait(dr, 2).until(
            EC.presence_of_element_located((By.ID, "iframe"))
        )
        dr.switch_to.frame(iframe1)
        iframe = WebDriverWait(dr, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.ans-attach-online.ans-insertvideo-online"))
        )
        dr.switch_to.frame(iframe)
        play_button = WebDriverWait(dr, 2).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "vjs-big-play-button"))
        )
        cl(play_button)
        dr.switch_to.default_content()
        smdm+='Y'
    except:
        print('播放失败')
        smdm+='E'
def bofzt():
    global a1,b1,c1,smdm
    try:
        iframe1 = WebDriverWait(dr, 2).until(
            EC.presence_of_element_located((By.ID, "iframe"))
        )
        dr.switch_to.frame(iframe1)
        iframe = WebDriverWait(dr, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.ans-attach-online.ans-insertvideo-online"))
        )
        dr.switch_to.frame(iframe)
        video_element = dr.find_element(By.XPATH, '//*[@id="video_html5_api"]')
        js_code = """
        const video = arguments[0];
        return {
            paused: video.paused,
            currentTime: video.currentTime,
            duration: video.duration
        };
        """
        playback_status = dr.execute_script(js_code, video_element)
        dr.switch_to.default_content()
        if(playback_status["paused"]):
            a1='暂停中'
        else:
            a1='播放中'
        b1=playback_status["currentTime"]
        c1=playback_status["duration"]
        smdm+='Y'
    except:
        print('播放状态获取失败')
        smdm+='E'
#--------------------------------------------------------------------------------------------准备工作
if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)  # 打包后使用 .exe 文件所在目录
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))  # 脚本模式下使用脚本所在目录
os.chdir(base_dir)
chrome_path = os.path.join(base_dir, "chrome-win64", "chrome.exe")
chromedriver_path = os.path.join(base_dir, "chrome-win64", "chromedriver.exe")
options = Options()
options.add_argument("--user-data-dir=/user-data")
options.add_argument("--profile-directory=Default")
options.binary_location = chrome_path
service = Service(chromedriver_path)
dr = webdriver.Chrome(service=service, options=options)
#--------------------------------------------------------------------------------------------
url='https://v8.chaoxing.com/'
dr.get(url)
try:
    dr.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/ul/li[2]').click()
except:
    dr.find_element(By.XPATH,'//*[@id="showPrompt"]/a').click()#
    s(0.5)
    dr.find_element(By.XPATH,'//*[@id="first842065"]/h3').click()
    print('无需登录')
q()
pand('/html/body/div[4]/p/a','点击这里进个人空间')
pandwb()
a1=''
b1=''
c1=''
smdm=''
huiche()
dr.close()
window_handles = dr.window_handles
dr.switch_to.window(window_handles[0])
#-------------------------------------------------净化
dr.execute_script(js_codejh)
dr.execute_script("""
    var elements = document.querySelectorAll('div.firstLayer');
    elements.forEach(function(element) {
        element.remove();
    });
""")
s(1)
#----------------------------------------------------------------------------------------获取信息
ttt = dr.find_elements(By.CSS_SELECTOR, "span.posCatalog_name")
titles = []
span_elements = []  
for span in ttt:
    title = span.get_attribute("title")
    if title and "测试" not in title: 
        titles.append(title)
        span_elements.append(span)  
        # print(title)
    else:
        dr.execute_script("arguments[0].parentNode.remove();", span)
cl(span_elements[0])
spanText=dr.find_elements(By.CLASS_NAME,'spanText')
runmode=0
if(len(spanText)==1):
    root_lis = dr.find_element(By.ID, "coursetree").find_element(By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")
    for li in root_lis:
        try:
            a=li.find_element(By.CLASS_NAME, "posCatalog_level").find_element(By.TAG_NAME, "ul").find_elements(By.XPATH, "./li")
            for i in a:
                try:
                    sb=i.find_element(By.CLASS_NAME,'posCatalog_select')
                    dr.execute_script("arguments[0].remove();", sb)
                    sb2=i.find_element(By.TAG_NAME,'ul').find_elements(By.XPATH, "./li")
                except:
                    pass
                for iii in sb2:
                    try:
                        div=iii.find_element(By.TAG_NAME,'div')
                        shu=div.find_elements(By.TAG_NAME,'span')
                        if(len(shu)==1):
                            dr.execute_script("arguments[0].remove();", iii)
                    except:
                        pass
        except:
            pass
    runmode=1
    try:
        wancheng=len(dr.find_elements(By.CLASS_NAME,'icon_Completed'))
    except:
        wancheng=0
elif(len(spanText)==2):
    runmode=2
    q()
    index=0
    for i in titles:
        print(index,i)
        index+=1
    wancheng=int(input('输入起始序号:'))
else:
    runmode=3
    q()
    index=0
    for i in titles:
        print(index,i)
        index+=1
    wancheng=int(input('输入起始序号:'))
initwan=wancheng
zhen=wancheng
q()
try:
    cl(span_elements[zhen])
    bof()
except:
    pass
from datetime import datetime
start_time = datetime.now()
while(3):
    smdm=''
    try:
        wancheng=zhen
        try:
            iframe1 = WebDriverWait(dr, 3).until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe"))
            )
            dr.switch_to.frame(iframe1)
            div_element = WebDriverWait(dr, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ans-job-icon.ans-job-icon-clear"))
            )
            ztai = div_element.get_attribute("aria-label")
            try:
                iframe = WebDriverWait(dr, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.ans-attach-online.ans-insertvideo-online"))
               )
                dr.switch_to.frame(iframe)
                radio_element = dr.find_element(By.CSS_SELECTOR, "input[type='radio']")
                cl(radio_element)
                submit=dr.find_element(By.ID,'videoquiz-submit')
                cl(submit)
                smdm+='Y'
            except:
                smdm+='E'
            smdm+='Y'
        except:
            smdm+='E'
        finally:
            dr.switch_to.default_content()
        smdm+='(Y1)'
        if(ztai=='任务点已完成'):
            zhen+=1
            if(zhen==len(span_elements)):
                break
            cl(span_elements[zhen])
            bof()
        smdm+='(Y2)'
        bofzt()
        smdm+='(Y3)'
        q()
        if(a1=='暂停中'):
            cl(span_elements[zhen])
            # cl(span_elements[zhen])
            bof() 
        smdm+='(Y4)'
        print('神秘代码：',smdm,' 运行模式:',runmode)
        print(titles[zhen])
        print(f'{zhen+1}/{len(span_elements)}','    已完成:',wancheng,' 剩余:',len(span_elements)-zhen)  
        print('本次执行完成了:',wancheng-initwan,'个小节  运行时间:',what_time(start_time))
        print(a1,f'视频进度：{int(int(b1)/int(c1)*100)}%')
        s(3)
    except:
        s(10)
        pass
print('全部刷完')
winsound.Beep(1000, 200)
winsound.Beep(1000, 200)
winsound.Beep(1000, 200)
winsound.Beep(1000, 200)
winsound.Beep(1000, 200)
winsound.Beep(1000, 200)
while(1):
    winsound.Beep(1000, 200)
    s(1)