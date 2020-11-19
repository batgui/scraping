import requests,time,csv
csv_file = open('./message.csv','a',newline='',encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(['店名','地址','电话'])
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'uuid=4bd920e3f9a346718440.1598617935.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=174350de4690-0bed7d91373c57-3323766-144000-174350de46ac8; PHPSESSID=odaua245sjgp825n4e89p563q0; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1598618012; Hm_lpvt_f66b37722f586a240d4621318a5a6ebe=1598618012; __utma=211559370.2009033232.1598618012.1598618012.1598618012.1; __utmc=211559370; __utmz=211559370.1598618012.1.1.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmcct=zt_search; __utmb=211559370.1.10.1598618012; mtcdn=K; userTicket=FgAlgrjxBoRRfiFVfkPPdtMrQfxSKiVtWQYyXVJO; u=146486958; n=%E6%83%B3%E7%99%BD%E5%90%83%E7%99%BD%E5%96%9D%E7%9A%84%E9%98%BF%E7%B3%96; lt=_5dNYExEpu-rZJTIsUwTPY_CzKsAAAAAcwsAAMHWPwnkis7QDzXsve6N6ON7ZSVYDrmVDg6X6R7SqPcSxyC4Je3NTST1q91ClJUnqQ; mt_c_token=_5dNYExEpu-rZJTIsUwTPY_CzKsAAAAAcwsAAMHWPwnkis7QDzXsve6N6ON7ZSVYDrmVDg6X6R7SqPcSxyC4Je3NTST1q91ClJUnqQ; token=_5dNYExEpu-rZJTIsUwTPY_CzKsAAAAAcwsAAMHWPwnkis7QDzXsve6N6ON7ZSVYDrmVDg6X6R7SqPcSxyC4Je3NTST1q91ClJUnqQ; lsu=; token2=_5dNYExEpu-rZJTIsUwTPY_CzKsAAAAAcwsAAMHWPwnkis7QDzXsve6N6ON7ZSVYDrmVDg6X6R7SqPcSxyC4Je3NTST1q91ClJUnqQ; unc=%E6%83%B3%E7%99%BD%E5%90%83%E7%99%BD%E5%96%9D%E7%9A%84%E9%98%BF%E7%B3%96; ci=1; rvct=1%2C1283; firstTime=1598619429563; _lxsdk_s=174350de474-c5b-39-757%7C%7C159',
    'Host': 'apimobile.meituan.com',
    'Origin': 'https://bj.meituan.com',
    'Referer': 'https://bj.meituan.com/s/%E8%B6%85%E5%B8%82/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
}
msg_list = []
for i in range(30):
    url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/50?uuid=4bd920e3f9a346718440.1598617935.1.0.0&userid=-1&limit=32&offset={}&cateId=-1&q=脱发'.format(i*32)
    print(url)
    res = requests.get(url,headers=headers).json()
    mes_list = res["data"]["searchResult"]
    time.sleep(1)
    for x in range(len(mes_list)):
        name = mes_list[x]["title"]
        addr = mes_list[x]["address"]
        phone_number = mes_list[x]["phone"]
        print("name:",name,"address:",addr,"phone_number:",phone_number,)
        msg_list.append([name,addr,phone_number])
for row in msg_list:
        writer.writerow(row)
csv_file.close()
