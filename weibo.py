import requests
import time
import re
import urllib.parse
import base64
import binascii
import execjs
import traceback
from urllib.parse import unquote
from bs4 import BeautifulSoup

## 自己发布微博的内容
postwebstr = "哈哈"
## 评论内容
commentstr = "啊这"
## cookie
cookie = "SSOLoginState=1604377083; _s_tentry=login.sina.com.cn; Apache=7229284692431.1875.1604377085997; WBtopGlobal_register_version=91c79ed46b5606b9; SUB=_2A25yr5PwDeRhGeFL6loV9ijOyjWIHXVR3II4rDV8PUNbmtANLRnjkW9NQnQTuWnXNXfzPteKes1HdEc-lKTbks6N; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhYGfh5ugzzCTolLhSckrYC5JpX5KMhUgL.FoMfeKnXSoqEeK.2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMXeoncSh-0eozp; wvr=6; wb_timefeed_7518466219=1; wb_view_log_7518466219=1440*9002; webim_unReadCount=%7B%22time%22%3A1605100622844%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A44%2C%22msgbox%22%3A0%7D"
def gettimestr():
    t = time.time()
    timestr = str(int(round(t * 1000)))
    return timestr

def gettentimestr():
    t = time.time()
    timestr = str(int(t))
    return timestr


# 
def postwb(text,cookie):
    timestr = gettimestr()
    # cookie = eval(cookie)
    #https://weibo.com/aj/mblog/add?ajwvr=6&__rnd=1604290551582
    postheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36','Content-Type': 'application/x-www-form-urlencoded; Charset=UTF-8','Accept': '*/*','Accept-Language': 'zh-cn','Referer': 'https://weibo.com/'}
    posturl = 'https://weibo.com/aj/mblog/add?ajwvr=6&__rnd=' + timestr
    print(posturl)
    postdata = urllib.parse.quote(text)
    data = 'location=v6_content_home&text='+ postdata + '&appkey=&style_type=1&pic_id=&tid=&pdetail=&mid=&isReEdit=false&rank=0&rankid=&module=stissue&pub_source=main_&pub_type=dialog&isPri=0&_t=0'
    response = requests.post(posturl,data=data,headers=postheader,cookies=cookie)
    

def extract_cookies(cookie):
    """从浏览器或者request headers中拿到cookie字符串，提取为字典格式的cookies"""
    cookies = dict([l.split("=", 1) for l in cookie.split("; ")])
    return cookies

def getCommentUrl(url, cookie):

    s = requests.session()
    s.keep_alive = False
    postheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36','Content-Type': 'application/x-www-form-urlencoded; Charset=UTF-8','Accept': '*/*','Accept-Language': 'zh-cn','Referer': 'https://weibo.com/'}
    response = s.get(url,headers=postheader,cookies=cookie)
    value = response.text
    soup = BeautifulSoup(value)

    mydivs = soup.findAll("p", {"class": "from"})
    res = []
    for p in mydivs:
        uu = "https:" + p.findAll("a")[0]['href'] + "?type=comment"
        # print(uu)
        res.append(uu)
    return res
def commentwb(text,cookie,url,uid):
    posturl = url
    # cookie = eval(cookie)
    s = requests.session()
    s.keep_alive = False
    postheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36','Content-Type': 'application/x-www-form-urlencoded; Charset=UTF-8','Accept': '*/*','Accept-Language': 'zh-cn','Referer': 'https://weibo.com/'}
    response = s.get(url,headers=postheader,cookies=cookie)
    value = response.text
    # print(value)
    mid = ''.join(re.search(r'&mid=(.+?)&',value).group(1))
    # print(mid)
    posttime = gettimestr()
    text = urllib.parse.quote(text)
    posturl = "https://weibo.com/aj/v6/comment/add?ajwvr=6&__rnd=" + posttime
    
    postdata = "act=post&mid=" + mid + "&uid=" + uid + "&forward=0&isroot=0&content=" + text + "&location=page_100505_single_weibo&module=bcommlist&pdetail=1005051496952253&_t=0"
    print(postdata)
    response = requests.post(posturl,data=postdata,headers=postheader,cookies=cookie)
    # print(response.json())


def main():
    global cookie
    cookie = unquote(cookie)
    cookie = extract_cookies(cookie)
    # print(cookie)
    # url = "https://weibo.com/6762528334/HfRnwe7yJ?type=comment"

    searchurl = "https://s.weibo.com/weibo/%25E5%2581%25A5%25E5%25BA%25B7?topnav=1&wvr=6&b=1"

    urllist = getCommentUrl(searchurl, cookie)
    i = 0
    for ul in urllist:
        postwb(postwebstr,cookie)
        print("commenting on url : " + ul)
        commentwb(commentstr, cookie, ul, "7518466219")
        # time.sleep(40)
        # print(i);
    

if __name__ == "__main__":
    main()
