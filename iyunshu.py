# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

from http import cookiejar   #py3

iyunshu_session = requests.Session()
iyunshu_session.cookies = cookiejar.LWPCookieJar(filename = "iyunshuCookies.txt")

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
header = {
    "Content-Type": "application/json",
    "Referer": "http://www.iyunshu.com/index.html",
    "User-Agent": useragent,
    "Origin": "http://www.iyunshu.com"
}




def iyunshu_login():
    print("开始模拟登录")
    
    posturl = 'http://www.iyunshu.com/ouser-web/mobileLogin/login.do'
    postdata = {
        "mobile": "19939105638",
        "password": "3b16dc694c38d04f7d7451cc37d3c654",
        "platform": 3
    }
    
    resp = requests.post(posturl, json = postdata, headers = header)
    
    print(f"statusCode = {resp.status_code}")
    print(f"text = {resp.text}")
    
    iyunshu_session.cookies.save()


def isLoginStatus():
    my_url = "https://mb2c.iyunshu.com/my/home.html"    #页面“我的”
    header = {
        "User-Agent": useragent,
    }
    
    resp = requests.get(my_url, headers = header, all_redirects = False)
    print("isLoginStatus = {resp.status_code}")
    if resp.status_code != 200:
        return False
    else:
        return True
    
def iyunshu_sign():
    sign_url = "https://mb2c.iyunshu.com/api/social/write/sign/doSign"
    header = {
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": useragent
    }
    resp = requests.post(sign_url, headers = header)
    print(resp.text)
    
    
if __name__ == "__main__":
    iyunshu_session.cookies.load()
    islogin = isLoginStatus()
    print("is login iyunshu: {islogin}")
    if islogin == False:
        print("cookies已失效")
        iyunshu_login()
        

    iyunshu_sign()