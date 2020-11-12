#coding:utf-8
import requests
import re
import json
from selenium import webdriver
import time
from bs4 import BeautifulSoup

## 配置
## cookie
str_cookie='BDUSS=5wSk5renQzUUxaUndXSHRmVHMzTThvSnZEMXBPZDBvbVNrNmwxV1NBMXVoOU5mRVFBQUFBJCQAAAAAAAAAAAEAAAAVIz5QZG9udEZlYXJNZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG76q19u-qtfc0; TIEBAUID=d2f4fc2a021d07a39121ea85; STOKEN=53b9eea2ec3fd8c99773335e0e3a43c928c16ca0a9cdcc9de6e8ae336790956c; H_PS_PSSID=1456_32854_32946_33060_32972_32723_32962; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; delPer=0; PSINO=3; wise_device=0; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1605154792; st_data=bcbca91533f30945b46ac2de00bd71c55830b06562f5963902269aca3f56c951de6b0dd70cd1dd3b186c46d7c67a3a15d6209fca7d142a0c92fe357b773d409906f6e3bc1cf9072ab1e71b4602ce24872d938f65674c9c841a84d392f03a4507cb366b90f7cc5b8df48e8a3a94c03ce56cb1a9ca7b8ca1f4d09618a6c0cf9280; st_key_id=17; st_sign=9966c54f'
## 健康吧的搜索结果
weburl = "https://tieba.baidu.com/f?ie=utf-8&kw=%E5%81%A5%E5%BA%B7&fr=search"


ss=requests.session()
def solve_bsk(tbs_str):
    driver = webdriver.Firefox()
    bsk_js_1="""
function bsk_solver(tbs_str) {
var MAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/<$+-%>{:* \\,}[^=_~&](")';
var IN=tbs_str;  // this is tbs

var OUT={};

function encodeStr(str) {
    var res = [];
    for (var i = 0; i < str.length; i++) {
        res.push(3 + (5 ^ str.charCodeAt(i)) ^ 6)
    }
    return res
}

function decodeCharCode(code) {
    return (6 ^ code) - 3 ^ 5
}

function toCharCodeArr(str) {
    var res = [];
    for (var i = 0; i < str.length; i++) {
        res.push(str.charCodeAt(i))
    }
    return res
}

function decodeChar(code) {
    return String.fromCharCode(decodeCharCode(code))
}

function decodeStr(arr) {
    return map(flatten(arr), decodeChar).join('')
}

function fromCharCodes(charCodes) {
    return String.fromCharCode.apply(null, charCodes)
}

function map(arr, func) {
    var res = [];
    for (var i = 0; i < arr.length; i++) {
        res.push(func(arr[i], i))
    }
    return res
}

function isArr(wtf) {
    return wtf.push && 0 === wtf.length || wtf.length
}

function flatten(arr) {
    return isArr(arr) ? [].concat.apply([], map(arr, flatten)) : arr
}

function genRes(arr, map) {
    for (var i = 0; i < arr.length; i++) {
        arr[i] = decodeCharCode(arr[i]);
        arr[i] = arr[i] ^ map[i % map.length]
    }
    return arr
}

function nextFunc(funcs) {
    var index = Math.floor(Math.random() * funcs.length);
    return funcs.splice(index, 1)[0]
}





function startRun() {
    var isNodejs = false;
    try {
        isNodejs = Boolean(global.process || global.Buffer)
    } catch (n) {
        isNodejs = false
    }
    if (isNodejs) {
        var wtf = decodeStr(toCharCodeArr(MAP)); // bug: quote isn't escaped
        func = function () {
            var [key, func] = nextFunc(funcs);
            return `"${key}":""${wtf}"` // bug: duplicate quotes
        }
    } else {
        func = function () {
            var [key, func] = nextFunc(funcs);
            try {
                var res = func();
                if (res && res.charCodeAt) {
                    res = res.replace(/"/g, encodeStr('\\"')); // bug: encoded twice
                    return `"${key}":"${res}"`;
                } else return `"${key}": ${res.toString()}`
            } catch (n) {
                return `"${key}": 20170511`
            }
        }
    }
    var length = funcs.length;
    var str = `{${Array.from({length}).map(func).join()}}`;
    console.log(str);
    if (!isNodejs) {
        var charCodes = genRes(encodeStr(str), [94, 126, 97, 99, 69, 49, 36, 43, 69, 117, 51, 95, 97, 76, 118, 48, 106, 103, 69, 87, 90, 37, 117, 55, 62, 77, 103, 38, 69, 53, 70, 80, 81, 48, 80, 111, 51, 73, 68, 125, 117, 51, 93, 87, 100, 45, 42, 105, 73, 40, 95, 52, 126, 80, 56, 71]);
        var data = btoa(fromCharCodes(charCodes));
        OUT.data = data
    } else OUT.data = btoa(fromCharCodes(str))
    //console.log(OUT);
}
var funcs = [['p1', function () {
    return window.encodeURIComponent(window.JSON.stringify(IN))
}], ['u1', function () {
    return "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}], ['l1', function () {
    return "en-US"
}], ['s1', function () {
    return 1080
}], ['s2', function () {
    return 1920
}], ['w1', function () {
    return "NULL"
}], ['w2', function () {
    return "NULL"
}], ['a1', function () {
    return 1920
}], ['a2', function () {
    return 1040
}], ['s3', function () {
    return true
}], ['l2', function () {
    return true
}], ['i1', function () {
    return true
}], ['a3', function () {
    return false
}], ['p2', function () {
    return "Win32"
}], ['d1', function () {
    return "NULL"
}], ['c1', function () {
    return true
}], ['a4', function () {
    return false
}], ['p3', function () {
    return false
}], ['n1', function () {
    return 20170511
}], ['w3', function () {
    return false
}], ['e1', function () {
    return 20170511
}], ['n2', function () {
    return 20170511
}], ['n3', function () {
    return 20170511
}], ['r1', function () {
    return "function random() { [native code] }"
}], ['t1', function () {
    return "function toString() { [native code] }"
}], ['w4', function () {
    return "stop,open,alert,confirm,prompt,print,requestAnimationFrame,cancelAnimationFrame,requestIdleCallback,cancelIdleCallback,captureEvents,releaseEvents,getComputedStyle,matchMedia,moveTo,moveBy,resizeTo,resizeBy,getSelection,find,getMatchedCSSRules"
}], ['t2', function () {
    return Math.floor(Date.now() / 1000)
}], ['m1', function () {
    return 'basilisk_aLv0jg'
}]];
startRun();

return OUT.data
}


return bsk_solver('""" 

    bsk_js_full=bsk_js_1+tbs_str+"')"

    BSK_=driver.execute_script(bsk_js_full)
    driver.quit()
    return BSK_

def extract_cookies(cookie):
    """从浏览器或者request headers中拿到cookie字符串，提取为字典格式的cookies"""
    cookies = dict([l.split("=", 1) for l in cookie.split("; ")])
    return cookies

postheader = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:82.0) Gecko/20100101 Firefox/82.0','Content-Type': 'application/x-www-form-urlencoded; Charset=UTF-8','Accept': '*/*','Accept-Language': 'zh-cn','Referer': 'https://weibo.com/'}

def getCommentUrl(url, cookie):

    s = requests.session()
    s.keep_alive = False
    response = s.get(url,headers=postheader,cookies=cookie)
    value = response.text
    soup = BeautifulSoup(value)
    # print(value)
    tid = re.findall(r'href=\"/p/(.+?)\"',value)
    # print(tid)

    res = []
    for t in tid:
        res.append(t)
    return res


reg='([\s\S]*?)=([\s\S]*?);'
dict_cookie={}
for c in  re.findall(reg,str_cookie):
   dict_cookie[c[0]]=c[1]
res = getCommentUrl(weburl, extract_cookies(str_cookie))
# print(res)
user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400'
    ]
header={}
import random
dict_data={
'ie':'utf-8',
'kw':'中华城市',
'fid':'429477',
'tid':'5063074699',
'floor_num':'2',
# 'quote_id':'106047109156',
'rich_text':'1',
'tbs':'1d2e70d051724ba01491647010',
'content':'啦啦啦',
# 'lp_type':'0',
# 'lp_sub_type':'0',
# 'new_vcode':'1',
# 'tag':'11',
# 'repostid':'106047109156',
# 'anonymous':'0',
"__type__":'reply',
'basilisk':'1',
'files':'[]',
'geetest_success':'0',
'_BSK' : "",
'mouse_pwd_isclick':"1",

}   
resp = ss.get("http://tieba.baidu.com/dc/common/tbs")
tbs = json.loads(resp.text)['tbs']
print(tbs)
resp = ss.get("http://tieba.baidu.com/f/commit/share/fnameShareApi?ie=utf-8&fname=健康")
fid = json.loads(resp.text)['data']['fid']
print(fid)
dict_data['kw']='健康'  #吧名
dict_data['fid']=str(fid)        #fid是贴吧什么时候建的
dict_data['tbs']=tbs  
dict_data['tid']='7080734612'    ##tid指的是主题帖子的id
dict_data['floor_num']='1'    
dict_data['content']='啊这'  
#获取fid的接口 ，http://tieba.baidu.com/f/commit/share/fnameShareApi?ie=utf-8&fname=%E6%B5%A0%E6%B0%B4%E4%BA%8C%E4%B8%AD
# print(dict_data)

i=0

for t in res[4:]:
    i=i+1
    dict_data['mouse_pwd_t'] = str(int(time.time()))
    mouse_pwd = dict_data['mouse_pwd_t'] + '0'
    mouse_pwd='88,88,76,81,84,87,81,88,105,81,76,80,76,81,76,80,76,81,76,80,76,81,76,80,76,81,76,80,105,81,87,80,81,84,105,81,89,82,80,76,81,80,88,80,'+mouse_pwd

    dict_data['mouse_pwd'] = mouse_pwd
    dict_data['tid'] = t.encode("ascii")
    # print(t)
    url = "https://tieba.baidu.com/p/" + t
    response = ss.get(url,headers=postheader,cookies=extract_cookies(str_cookie))
    value = response.text
    # soup = BeautifulSoup(value)
    # tbs:'011dd547532d9c611605152377'
    tbs = re.findall(r"tbs:'(.+?)'", value)
    # print(value)
    # print("sadadawsdadadsa")
    print(tbs)
    dict_data['tbs'] = tbs[0]
    dict_data['_BSK'] = solve_bsk(dict_data['tbs'])

    try:
        header['User-Agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:82.0) Gecko/20100101 Firefox/82.0"  ##习惯性的学爬虫来个随机换user-agent,但贴吧和知乎 这种都是基于账号追踪的，换ua和代理ip是没有任何作用的，逃避不了被识别为机器人
        header['Connection']='close'
        header.update({ 'Host':'tieba.baidu.com','Origin':'http://tieba.baidu.com','Referer':'http://tieba.baidu.com/p/5065229106'})

        # dict_data['content']='哈哈哈哈'+str(i)

        res=ss.post('http://tieba.baidu.com/f/commit/post/add',cookies=dict_cookie,data=dict_data,headers=header)   
        res_content=res.content
        res_text=res.text
        # print(res.text)
        # print(res.content)
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'  ',json.dumps(json.loads(res_content),ensure_ascii=False)) ###这样可以清楚的看到json里面的\u xxxx之类的对应的中文。

    except Exception as e:
        #i=i-1
        print(e)
    time.sleep(10)                   ##每隔10秒回帖
