import requests,time,csv
import requests
import re
import json
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
import os

csv_file = open('./message.csv','a+',newline='')
writer = csv.writer(csv_file)
writer.writerow(['店名','地址','电话', '图片', '价格','评分','评论数','分类'])
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Cookie': 'uuid=4bd920e3f9a346718440.1598617935.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=174350de4690-0bed7d91373c57-3323766-144000-174350de46ac8; PHPSESSID=odaua245sjgp825n4e89p563q0; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1598618012; Hm_lpvt_f66b37722f586a240d4621318a5a6ebe=1598618012; __utma=211559370.2009033232.1598618012.1598618012.1598618012.1; __utmc=211559370; __utmz=211559370.1598618012.1.1.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmcct=zt_search; __utmb=211559370.1.10.1598618012; mtcdn=K; userTicket=FgAlgrjxBoRRfiFVfkPPdtMrQfxSKiVtWQYyXVJO; u=146486958; n=%E6%83%B3%E7%99%BD%E5%90%83%E7%99%BD%E5%96%9D%E7%9A%84%E9%98%BF%E7%B3%96; lt=_5dNYExEpu-rZJTIsUwTPY_CzKsAAAAAcwsAAMHWPwnkis7QDzXsve6N6ON7ZSVYDrmVDg6X6R7SqPcSxyC4Je3NTST1q91ClJUnqQ; mt_c_token=_5dNYExEpu-rZJTIsUwTPY_CzKsAAAAAcwsAAMHWPwnkis7QDzXsve6N6ON7ZSVYDrmVDg6X6R7SqPcSxyC4Je3NTST1q91ClJUnqQ; token=_5dNYExEpu-rZJTIsUwTPY_CzKsAAAAAcwsAAMHWPwnkis7QDzXsve6N6ON7ZSVYDrmVDg6X6R7SqPcSxyC4Je3NTST1q91ClJUnqQ; lsu=; token2=_5dNYExEpu-rZJTIsUwTPY_CzKsAAAAAcwsAAMHWPwnkis7QDzXsve6N6ON7ZSVYDrmVDg6X6R7SqPcSxyC4Je3NTST1q91ClJUnqQ; unc=%E6%83%B3%E7%99%BD%E5%90%83%E7%99%BD%E5%96%9D%E7%9A%84%E9%98%BF%E7%B3%96; ci=1; rvct=1%2C1283; firstTime=1598619429563; _lxsdk_s=174350de474-c5b-39-757%7C%7C159',
    'Host': 'apimobile.meituan.com',
    'Origin': 'https://bj.meituan.com',
    'Referer': 'https://bj.meituan.com/s/%E8%B6%85%E5%B8%82/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:83.0) Gecko/20100101 Firefox/83.0',
}
msg_list = []
k = 1
ss=requests.session()
postheader = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:82.0) Gecko/20100101 Firefox/82.0','Content-Type': 'application/x-www-form-urlencoded; Charset=UTF-8','Accept': '*/*','Accept-Language': 'zh-cn','Referer': 'https://weibo.com/'}
cookies = "ly_admin_think_language=zh-CN; PHPSESSID=enfrg9truh0iktk1q7bf4p3cmv; ly_main_nav_limit=10"

cookie = "_lxsdk_cuid=175ca9e5f7938-0838368f7a04f78-445e6d-13c680-175ca9e5f7ab; ci=1; rvct=1%2C10%2C50; uuid=d7cb27d8741d448a85c0.1606711126.1.0.0; userTicket=tuFwQsddZjMoeCVXOSmtoFQcDZcPVAcsPYGJEMnC; m=451420401%40qq.com; lsu=; firstTime=1607573194009; __mta=49034777.1606711206717.1607525029908.1607573194012.48; mtcdn=K; lt=tD-gf4eCUqb_eNdZS1sImgKxoNkAAAAARgwAAEQdAQiejH-yM6CUcT-rIW3hQOJS-DwBtvtS7Sp8K8hj0oykIdY3oHSpQe0mdS2n0w; u=3080278451; n=eMs850102202; token2=tD-gf4eCUqb_eNdZS1sImgKxoNkAAAAARgwAAEQdAQiejH-yM6CUcT-rIW3hQOJS-DwBtvtS7Sp8K8hj0oykIdY3oHSpQe0mdS2n0w; _lxsdk_s=1764ad44501-ae8-3ff-a33%7C%7C13; unc=eMs850102202"
headers["Cookie"] = cookie

dict_data= {

'id':246,
'avatar':'中华城市',
'name': "123",
'class_id': '10',#9 10 14
'doctor_brife':'429477',

}

idd = 100
def extract_cookies(cookie):
    """从浏览器或者request headers中拿到cookie字符串，提取为字典格式的cookies"""
    cookies = dict([l.split("=", 1) for l in cookie.split("; ")])
    return cookies
# for i in range(133, 140):
#     dict_data["id"] = i
#     dict_data["profess"] = "123"
#     res = ss.post('http://www.jiankangkang.vip/admin.php?s=/client/index/adddoctor.html',cookies=extract_cookies(cookies),data=dict_data,headers=postheader)   
    
#     print(i)

#     print(res)
# exit()


for j in [1, 10, 50]:
    prev = -1
    for i in range(10):
        # https://apimobile.meituan.com/group/v4/poi/pcsearch/10?uuid=d7cb27d8741d448a85c0.1606711126.1.0.0&userid=3080278451&limit=32&offset=0&cateId=-1&q=%E8%84%B1%E5%8F%91&token=wgu7nyPrqxLyPfAKeZD2ncGyTpQAAAAAJQwAAJo48Iqq6phCtLtih3U12qlRdBGRUFv0rnMmK5eDj3BI76Dxjd4vqSQrTDMR5OzgXQ&sort=default
        url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/' + str(j) +'?uuid=d7cb27d8741d448a85c0.1606711126.1.0.0&userid=3080278451&limit=32&offset=0&cateId=-1&q=体检&token=tD-gf4eCUqb_eNdZS1sImgKxoNkAAAAARgwAAEQdAQiejH-yM6CUcT-rIW3hQOJS-DwBtvtS7Sp8K8hj0oykIdY3oHSpQe0mdS2n0w&sort=rating'.format(i*32)
        print(url)
        # w = os.popen("curl " + url).read()
        jsonData = json.loads(requests.get(url,headers=headers).text)
        # jj = json.loads(w)
        # print(jj['data']["searchResult"])
        # res = requests.get(url,headers=headers).json()
        mes_list = jsonData["data"]["searchResult"]
        # print(mes_list)
        # print(len(msg_list))
        if (len(msg_list) == prev):
            break;
        # print(mes_list)
        time.sleep(1)
        prev = len(msg_list)
        #imageUrl 
        for x in range(len(mes_list)):
            idd = mes_list[x]['id']
            print(idd)
            # idd = 110935389
            name = mes_list[x]["title"]
            addr = mes_list[x]["address"]
            phone_number = mes_list[x]["phone"]
            img_number = mes_list[x]["imageUrl"]
            # print(type(mes_list[x]))
            price = mes_list[x].get("price", "null")
            avgscore = mes_list[x]["avgscore"]
            comments = mes_list[x]["comments"]
            backCateName =  mes_list[x]["backCateName"]
            s = requests.session()
            s.keep_alive = False
            response = s.get("https://www.meituan.com/jiankangliren/" + str(idd),headers=postheader,cookies=extract_cookies(cookie))
            
            value = response.text
            # print(response.text)
            soup = BeautifulSoup(value)
            mydd = soup.findAll("div", {"class": "info"})
            mydivs = soup.findAll("span", {"class": "combo-title-text"})
            mydivs2 = soup.findAll("img", {"class": "image"})
            dic = {}
            dic1 = {}
            dic2 = {}
            i = 0
            # print(mydd)
            # print(mydivs)
            # print(mydivs2)
            for m in mydivs:

                # print(m.text)
                dic1[i] = m.text
                i += 1
            i = 0
            for m in mydivs2:
                # print(m['src'])
                dic2[i] = "https:" + m["src"];
                i += 1

            # print(dic1)
            for i in dic1:
                dic[dic1[i]] = dic2[i]
            # print(dic1)
            # print(dic2)
            # print(dic)

            sellerPage = "https://www.meituan.com/ptapi/poi/getcomment?id=" + str(idd) + "&offset=0&pageSize=10&mode=0&sortType=1"
            # print(uu)
            # res2 = requests.get(sellerPage).text
            res2 = os.popen("curl " + sellerPage).read()

            # print(res2)
            commentData = json.loads(res2)
            tags = commentData['tags']
            tag = []
            if tags == None:
                tag = ["热情周到"]
            else:
                for t in tags:
                    tag.append(t['tag'])
            print(tag)
            print("name:",name,"address:",addr,"phone_number:",phone_number,"img:", img_number, "price:", price, "avgscore:", avgscore, "comments", comments, "backCateName:", backCateName)
            msg_list.append([name,addr,phone_number, img_number, price, avgscore, comments, backCateName])
            # r = requests.get(img_number,headers=headers)
            r = requests.head(img_number)
            # print(img_number)
            
            # print(r.content)
            k = 0
            print(img_number)
            print(r.status_code)
            if r.status_code == requests.codes.ok:
                if k == 10:
                    break
                k += 1
                img_number = mes_list[x]["imageUrl"]
                dict_data["id"] += 1
                dict_data["profess"] = backCateName
                dict_data["avatar"] = img_number
                dict_data["name"] = name
                # <a href="https://www.w3schools.com/">Visit W3Schools.com!</a>
                t = "<p> 店铺链接： <a href=\"" + "https://www.meituan.com/jiankangliren/" + str(idd) + "/\">https://www.meituan.com/jiankangliren/" + str(idd) + "</a></p>"
                print(t)
                dict_data["doctor_brife"] = t
                dict_data["doctor_brife"] += "<p>地址：" + addr +", " + "手机号： " + str(phone_number) + ", " + "评分： " +  str(avgscore) + ", " + "\n</p>评价： ";
                for t in tag:
                     dict_data["doctor_brife"] += t + '、'

                dict_data["doctor_brife"] += '<p></p>'
                print("提供的套餐：**********************")
                print(dic)
                if dic != None:
                    if len(dic) > 0:
                        dict_data["doctor_brife"] += '<p>提供的套餐如下：</p>'

                for d in dic:
                    print("******")
                    print(d)
                    dict_data["doctor_brife"] += "<p>"
                    dict_data["doctor_brife"] += d
                    dict_data["doctor_brife"] += '</p><p>'
                    print(dic[d])
                    dict_data["doctor_brife"] += '<img src="' + dic[d] + '"/>'
                    dict_data["doctor_brife"] += '</p>'

                # print(img_number)
                # print(r)
                res = ss.post('http://www.jiankangkang.vip/admin.php?s=/client/index/adddoctor.html',cookies=extract_cookies(cookies),data=dict_data,headers=postheader)   
                res_content=res.content
                # res_text=res.res_text
                print(res)
                time.sleep(1)
                # exit()
               




csv_file.close()
