from pyquery import PyQuery as pq
import threading
import queue
import time
from urllib.parse import urlparse
from openpyxl import load_workbook
from openpyxl import Workbook
import time
import gc
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import random
import requests
import re
import json
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
# from pykeyboard import PyKeyboard

cookie_list = ['BAIDUID=6531978BB2BB941C95B2726F2570CCDA:FG=1; BIDUPSID=6531978BB2BB941C4A8341D7A2D3B94D; PSTM=1600685192; TIEBA_USERTYPE=a320d01d15d44ff5877d6fae; bdshare_firstime=1605105966189; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1605105966; BDUSS=5wSk5renQzUUxaUndXSHRmVHMzTThvSnZEMXBPZDBvbVNrNmwxV1NBMXVoOU5mRVFBQUFBJCQAAAAAAAAAAAEAAAAVIz5QZG9udEZlYXJNZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG76q19u-qtfc0; TIEBAUID=d2f4fc2a021d07a39121ea85; STOKEN=53b9eea2ec3fd8c99773335e0e3a43c928c16ca0a9cdcc9de6e8ae336790956c; H_PS_PSSID=1456_32854_32946_33060_32972_32723_32962; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; delPer=0; PSINO=3; wise_device=0; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1605323807; st_data=bcbca91533f30945b46ac2de00bd71c55830b06562f5963902269aca3f56c951de6b0dd70cd1dd3b186c46d7c67a3a15d6209fca7d142a0c92fe357b773d409906f6e3bc1cf9072ab1e71b4602ce24872d938f65674c9c841a84d392f03a45079a1ffa58a338e71358dd7413af7d5df859a1d6ac95b6252211074734ec5806b7; st_key_id=17; st_sign=81c66016',
                ]


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
        res.append("https://tieba.baidu.com/p/" + t)
    return res

def get_driver(chromedriver_path,chrome_path,ua):
    ua = ua
    option = Options()
    option.add_argument("user-agent=" + ua)
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--disable-gpu")
    option.add_argument("--disable-features=NetworkService")
    option.add_argument("--disable-features=VizDisplayCompositor")
    option.add_argument('log-level=3') 
    option.add_argument('--ignore-certificate-errors-spki-list') 
    option.add_argument('-ignore -ssl-errors') 
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    No_Image_loading = {"profile.managed_default_content_settings.images": 1}
    option.add_experimental_option("prefs", No_Image_loading)
    option.add_argument("--disable-blink-features")
    option.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=option, chrome_options=option)
    return driver


# 获得所有账号cookie
def get_cookie():
    global cookie_list
    return cookie_list


# 字符串cookie转为字典
def to_dict(cookie_str):
    cookie = {}
    lists = cookie_str.split(";")
    for i in lists:
        j = i.strip()
        j = j.split("=")
        cookie[j[0]] = j[1]
    return cookie


# 自动登录
def auto_login(cookie_dict):
    num = user_name = 0
    teiba_index = "https://tieba.baidu.com/"
    driver.get(teiba_index)
    driver.delete_all_cookies()
    for k, v in cookie_dict.items():
        driver.add_cookie({'name':k, "value": v})
    try:
        driver.get(teiba_index)  
        navs = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, "com_userbar"))
        )
        li_list = driver.find_elements_by_css_selector("#com_userbar > ul > li")
        li_classnames = [li.get_attribute("class") for li in li_list]
        if 'u_username' in li_classnames:
            num = 1
            user = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#j_u_username > div.u_menu_item.u_menu_username > a > span"))
            )
            user_name = user.text
    except Exception as e:
        print('登陆过程异常',e)
    else:
        pass
    finally:
        return num,user_name


def huifu(tie_url,content):
    try:
        driver.get(tie_url)
        # 人为滚动一下
        driver.execute_script(js)
        # 加载关注按钮
        guanzhu = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, "j_head_focus_btn"))
        )
        ActionChains(driver).move_to_element(guanzhu).perform()
        input_content = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "ueditor_replace")))
        button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "ueditor_replace")))
        huifu_first = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "p_reply_first")))
        ActionChains(driver).move_to_element(guanzhu).move_to_element(huifu_first).perform()
        huifu_first.click()
        while True:
            js_to_bottom = 'var height = document.documentElement.scrollHeight-document.documentElement.scrollTop-document.documentElement.clientHeight;return(height)'
            to_bottom = driver.execute_script(js_to_bottom)
            if int(to_bottom) == 0:
                break
        print('页面到达底部,需额外等10s')
        js_content_position = "document.getElementById('ueditor_replace').click();"
        driver.execute_script(js_content_position)
        js_content = """document.getElementById('ueditor_replace').innerText='{0}'""".format(content)
        driver.execute_script(js_content)
        time.sleep(10)

        button_js = 'document.querySelector("#tb_rich_poster > div.poster_body.editor_wrapper > div.poster_component.editor_bottom_panel.clearfix > div > a").click()'
        driver.execute_script(button_js)
    except Exception as e:
        print(e,'回复异常')
    else:
        return 1


def main(tie_urls,contents,cookie_list,time1,time2):
    for cookie in cookie_list:
        try:
            cookie_dict = to_dict(cookie)
            num_auto,user_name = auto_login(cookie_dict) 
            if num_auto == 1:
                print(user_name,'自动登录成功')
            else:
                print('自动登录失败')
                continue
        except Exception as e:
            print(e, '未顺利登录')
        else:
            for tie in tie_urls:
                content = random.choice(contents)
                num = huifu(tie,content)
                if num == 1:
                    print(tie,'--回复成功')
                else:
                    print(tie,'--回复失败')
                time.sleep(random.randint(time1,time2))
        finally:
                time.sleep(random.randint(time1,time2))
                driver.delete_all_cookies()

weburl = "https://tieba.baidu.com/f?ie=utf-8&kw=%E5%81%A5%E5%BA%B7&fr=search"
def extract_cookies(cookie):
    """从浏览器或者request headers中拿到cookie字符串，提取为字典格式的cookies"""
    cookies = dict([l.split("=", 1) for l in cookie.split("; ")])
    return cookies

if __name__ == "__main__":

    js = 'window.scrollBy(0,{0})'.format('document.body.scrollHeight')
    
    ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    # 全局变量
    driver = get_driver()

    cookie_list = get_cookie()
    # 回复内容
    contents = ["上网搜搜吧"]
    # 要回复的贴
    tie_urls = getCommentUrl(weburl, extract_cookies(cookie_list[0]))[:4]

    print(tie_urls)
    sleep_min, sleep_max = 60, 70
    main(tie_urls,contents,cookie_list,sleep_min,sleep_max)
    driver.quit()
