import requests
import random 
from rich.panel import Panel as nel
from rich import print as cetak
import os
from user_agent import generate_user_agent
import time
from hashlib import md5
import requests,re,random,os,sys
from rich import print as g
from rich.panel import Panel
from threading import Thread
q=0
w=0
e=0
M=0
ids=[]
token=input('Enter Token : ')
ID=input('Enter ID : ')
os.system('clear')

gre = '\033[2;32m'
red = '\033[1;31m'
red = '\033[1;31m'
yel = '\033[1;33m'
gre = '\033[2;32m'
wh = "\033[1;97m"
ble = '\033[2;36m'
blu = '\033[1;34m' 
F = '\033[1;32m'
Z = '\033[1;31m'
def ali(user):
	cc = user
	global q,w,e,M
	cookies = {
	    'mkt': 'ar-XA',
	    'MicrosoftApplicationsTelemetryDeviceId': 'b8e93f81-51f6-4af4-a498-689fefcf697b',
	    'MUID': 'c6b087823f134e1493964328c7f5f6f6',
	    '_pxvid': 'dfd131fe-6555-11ef-91a5-7e5bf9c5b607',
	    'MSFPC': 'GUID=7ac3f3a7af3646c8ab1d8b530c2de4a3&HASH=7ac3&LV=202408&V=4&LU=1724860499803',
	    'PPLState': '1',
	    'MSPAuth': 'Disabled',
	    'MSPProf': 'Disabled',
	    'NAP': 'V=1.9&E=1dd5&C=b38nDbCIrXFiv1ttn3NRdyQlLvxKzkpUMcuX1NxsrHi4FO-xUtmCMw&W=2',
	    'ANON': 'A=DCCF1D43DA061B07E595D1C5FFFFFFFF&E=1e2f&W=2',
	    'WLSSC': 'EgAdAgMAAAAMgAAAngABXuzCGL4f0PpsOtz7Qf5Kf0LYy0w01DhiUF3aogqw2V3XFScNcXMnUF5NMnt9oh0IvleLeu7Npt+Q2bzVW1/g1l5vopQoKYdi9LftrLea38zKZIQsa7R6bJRPY++kpN0qZt6Bd35J+TXVz7cs0ihqpe7M7s31JReWMFkPV4crg/5cAyDUBQyPf6daJPQ0fmDMCbmhS634jxsvoAWgTjZKuNtqXt2VF1y4h+uorLf239dUf74hSGIX1gmpuj1yuNx6lDsxb1kFTKXhj1PemxxA279pjO1Nq0hZP21psYys6slSTB+85WAEGqbqIqouLPi8lgtYAMWjKEUA4E2sRz3+FQwBfgAMAf9/AwCfnuaEQaHRZiOh0WYQJwAAChGggBARAHF6dGlAb3V0bG9vay5jb20AVgAAHXF6dGklb3V0bG9vay5jb21AcGFzc3BvcnQuY29tAAAAAklRAAAAAAAASAECAACPK1VAAAZDAAZvdGhtYW4ABW9zYW1hAAAAAAAAAAAAAAAAAAAAAAAAW3tSwX2XVVsAAEGh0WYjSEhnAAAAAAAAAAAAAAAADQAzNy43Ny43My4xNjYABAEAAAAAAAAAAAAAAAABBAAAAAAAAAAAAAAAAAAAAKyUcWOctFTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAA==',
	    'mkt1': 'ar-XA',
	    'amsc': 'EpCg8JCltNqb2wHTh6pjVnHR8oS+xxaajROXrI+X7VUdvC0yntrLQWPB0ur1A0zEuyNbx/vbLlcsN3RtkSe1NhzzrCdRnhx/GNtqeBBd7Fp8cCqiPgnNNwEs2T7ikHGA9SFEu2J39W9EAIpXzkSm0hASrVWyYNjTYMwzdVHcKwdBdicaROxb/X1xHEUdo3V3xMzS3kT2yO3xdweob16YZjgk7DMOYL793YatJU6v+Qd1uvpjcDBftyT6UdMPmJ877d5oi/FW2QNFMO02UUfQni7ql5wfVXnifiueUr2c42U=:2:3c',
	    'ai_session': 'sxQF6BJLjQD88h5fvKaAmr|1725122525589|1725122525589',
	    'fptctx2': 'taBcrIH61PuCVH7eNCyH0OPzOrGnaCb%252f7mTjN%252fuIW2u6glvqA%252fKfSqD2a9o4tB%252fFkiiupzRfyi00Bt%252b%252bkZ9b%252bMRAA7iwUIlRuDJGqdwTq3DX%252b7t40VnUsPb%252be15Gn6GYxmOqNv7NYOe5UkudAfs2TOcHai1AMIXBi9pTZiwNdtN91gyiuZPsmExji%252fSNsG5NquDwQXEw4fQU8NL0NdacDgT9lPNy7v9S6JQnuKahqzmyRFp4RQb6w7N6LDW5Ye5oAFsR4DMJ8vvZ2hNTFAfgTGviKW4BNzH8zgCkRTEAjH8QxrQZWiCaRuQDZV2ucgRb8Zw7mu1VTB%252ft3Gxw7VpPLA%253d%253d',
	    '_px3': 'dc246be551772557eb62d5538721f003bad9ee59cc222286abe8768155293663:QA0Hg92Jm1lCcHZOx+2mKn6VgsQZXiPBUsWra3EM8EAMN/5ggXDwKgdB65H2H5APLNbWkzLQO7jIEdQyV9QU+g==:1000:tpFXakwXXv2U9mcY1BLh0nDhIl+JaHaQn3NXrdYxjyGwbCAiFt4F5vX546E6I/IhAIMf5gaZRnaJrKri3UkfSVYl8BQDN35UVR5pmdvMhgttTUFIK/kDeYl15h7v8ULDo7Tb/YAp/VjxLJI6L7m4bZgkXnZn5T5gZRpp75Q9mIqxGbkqQir0mHc31mg2BN93jvmY8IoF9NXl6Ayy1G+iSJk7Ay9uYVsLs3dajzALHO0=',
	    '_pxde': '2eca33a4c257840966acbd7f1d5bbe536aa73500fe322b2d966ee8b83c9e0061:eyJ0aW1lc3RhbXAiOjE3MjUxMjI1MzIyMjcsImZfa2IiOjAsImlwY19pZCI6W119',
	}
	
	headers = {
	    'authority': 'signup.live.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'canary': 'JEGXeqFSR1u019PYQrMhQG6Kgp/YdLFbngWCBpti/ZyU/37Bp5q6EztWPjFKDihJZmZszZwiqkXNEV5DDLy2atVidRFq5rc6aUq3K5xUGRsZUZi/TErGqfRei2ZaC5vp80sfG7qjjM5lFxoLkWc1S9d6u/dHU6Ff15zVZMWxUA3KpmuoCkTn2u5UiQI6oRAGhm5i7Mxv6BFiKfnnnea0KoB0+4NtckMn/Ocb2upDRhAicMg3hg7jQ98lk5qg8rwd:2:3c',
	    'client-request-id': '5574f494a9144c6e9fc10bb3dc5f9253',
	    'content-type': 'application/json; charset=utf-8',
	    'correlationid': '5574f494a9144c6e9fc10bb3dc5f9253',
	    'hpgact': '0',
	    'hpgid': '200225',
	    'origin': 'https://signup.live.com',
	    'referer': 'https://signup.live.com/signup?mkt=ar-xa&lic=1',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': generate_user_agent(),
	}
	
	params = {
	    'mkt': 'ar-xa',
	    'lic': '1',
	}
	
	json_data = {
	    'includeSuggestions': True,
	    'signInName': f'{cc}@hotmail.com',
	    'uiflvr': 1001,
	    'scid': 100118,
	    'uaid': '5574f494a9144c6e9fc10bb3dc5f9253',
	    'hpgid': 200225,
	}
	
	re = requests.post(
	    'https://signup.live.com/API/CheckAvailableSigninNames',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	).text
	if '"isAvailable":true' in re:
		q+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''									
{red}[ {gre}𝗩𝟭𝟮 {red}]{gre}Done  ➪  {M}      		
{red}[ {gre}𝗩𝟭𝟮 {red}]{wh}Good Hotmail  ➪  {q}         		    
{red}[ {gre}𝗩𝟭𝟮 {red}]{yel}Bad Instagram  ➪  {w}          			    
{red}[ {gre}𝗩𝟭𝟮 {red}]{red}Bad Hotmail  ➪  {e}   
{red}[ {gre}𝗩𝟭𝟮 {red}]{ble}Email  ➪  {cc}@hotmail.com    

''')
		cookies = {
		    'ig_did': 'A7300F6A-992A-4FE1-A566-B1F9504ED44C',
		    'ig_nrcb': '1',
		    'dpr': '2.25',
		    'mid': 'Zs-L8QABAAH1NylH3ZpGnt5ty8MK',
		    'datr': '8YvPZgfIhPj28BTHg4NrjVz3',
		    'rur': '"CLN\\05468922150988\\0541756658783:01f79c14c91d6cacd1ab722a7e6c8d9e578a22f907fb24bbf1c2c3205b52a5abe0409ce8"',
		    'csrftoken': 's45lRcAvHhEihwcvLpHZK9c5ZLbuS4n2',
		    'wd': '480x919',
		}
		
		headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/accounts/signup/email/',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-model': '"RMX3511"',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-ch-ua-platform-version': '"13.0.0"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': generate_user_agent(),
		    'x-asbd-id': '129477',
		    'x-csrftoken': 's45lRcAvHhEihwcvLpHZK9c5ZLbuS4n2',
		    'x-ig-app-id': '1217981644879628',
		    'x-ig-www-claim': 'hmac.AR2a_LRn8jhwcQzBk8rSlxnf_BlQ0_ayXqxe2HzBOTxeiU9k',
		    'x-instagram-ajax': '1016135666',
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		data = {
		    'email': f'{cc}@hotmail.com',
		}
		
		res = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', cookies=cookies, headers=headers, data=data)
		if "email_is_taken" in res.text:
			M+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'''									
{red}[ {gre}𝗩𝟭𝟮 {red}]{gre}Done  ➪  {M}      		
{red}[ {gre}𝗩𝟭𝟮 {red}]{wh}Good Hotmail  ➪  {q}         		    
{red}[ {gre}𝗩𝟭𝟮 {red}]{yel}Bad Instagram  ➪  {w}          			    
{red}[ {gre}𝗩𝟭𝟮 {red}]{red}Bad Hotmail  ➪  {e}   
{red}[ {gre}𝗩𝟭𝟮 {red}]{ble}Email  ➪  {cc}@hotmail.com    

''')
			cookies = {
			    'csrftoken': '0uZYzvtUhu6-U4CARhIaM3',
			    'ig_did': '394458D6-565A-48F0-BFBB-CB75FD177F49',
			    'ig_nrcb': '1',
			    'dpr': '2.25',
			    'mid': 'ZsqbPgABAAFrLhyT_amwiK59BNv4',
			    'datr': 'PpvKZjhMQN858xPWY13-suQ2',
			    'wd': '480x919',
			}
			
			headers = {
			    'authority': 'www.instagram.com',
			    'accept': '*/*',
			    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'referer': 'https://www.instagram.com/shbs/',
			    'sec-ch-prefers-color-scheme': 'dark',
			    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
			    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-model': '"RMX3511"',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-ch-ua-platform-version': '"13.0.0"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-origin',
			    'user-agent': str(generate_user_agent()),
			    'x-asbd-id': '129477',
			    'x-csrftoken': '0uZYzvtUhu6-U4CARhIaM3',
			    'x-ig-app-id': '1217981644879628',
			    'x-ig-www-claim': '0',
			    'x-requested-with': 'XMLHttpRequest',
			}
			
			params = {
			    'username': cc,
			}
			
			VV = response = requests.get(
			    'https://www.instagram.com/api/v1/users/web_profile_info/',
			    params=params,
			    cookies=cookies,
			    headers=headers,
			).json()		
			name = VV['data']['user']['full_name']
			bio = VV['data']['user']['biography']
			fols = VV['data']['user']['edge_followed_by']['count']
			flog = VV['data']['user']['edge_follow']['count']
			id = VV['data']['user']['id']
			pr = VV['data']['user']['is_private']
			op = response['data']['user']['edge_owner_to_timeline_media']['count']
			try:
				re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
				ree = re.json()
				data = ree['date']
			except:
				data="Not Data"
			ff = f'''
Dev | 𝗩𝟭𝟮
Ibn_Suleiman | @CM_V12
		
••••••••••••••••••••••••••••••••••••••••••••••
Name : {name}
User : {cc}
Email : {cc}@hotmail.com
Followers : {fols}
Following : {flog}
Data : {data} 
Post : {op} 
ID : {id}
Link : https://www.instagram.com/{cc}
••••••••••••••••••••••••••••••••••••••••••••••
							'''
			print(gre+ff)
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}''')
			i = requests.post(tlg)
		else:
			w+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'''									
{red}[ {gre}𝗩𝟭𝟮 {red}]{gre}Done  ➪  {M}      		
{red}[ {gre}𝗩𝟭𝟮 {red}]{wh}Good Hotmail  ➪  {q}         		    
{red}[ {gre}𝗩𝟭𝟮 {red}]{yel}Bad Instagram  ➪  {w}          			    
{red}[ {gre}𝗩𝟭𝟮 {red}]{red}Bad Hotmail  ➪  {e}   
{red}[ {gre}𝗩𝟭𝟮 {red}]{ble}Email  ➪  {cc}@hotmail.com    

''')
	else:
		e+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''									
{red}[ {gre}𝗩𝟭𝟮 {red}]{gre}Done  ➪  {M}      		
{red}[ {gre}𝗩𝟭𝟮 {red}]{wh}Good Hotmail  ➪  {q}         		    
{red}[ {gre}𝗩𝟭𝟮 {red}]{yel}Bad Instagram  ➪  {w}          			    
{red}[ {gre}𝗩𝟭𝟮 {red}]{red}Bad Hotmail  ➪  {e}   
{red}[ {gre}𝗩𝟭𝟮 {red}]{ble}Email  ➪  {cc}@hotmail.com    

''')

def rand_ids():  
  Id= str(random.randrange(128053904,438909537))
  if Id not in ids:
    ids.append(Id)
    return Id
  else:
    rand_ids()    
def username1():
  global check
  try:
    while True:      
      rnd=str(random.randint(150, 999))
      user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
      Id = rand_ids()
      lsd=''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(32))
      headers = {
    'accept': '*/*',
    'accept-language': 'en,en-US;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/cristiano/following/',
    'user-agent': user_agent,
    'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
    'x-fb-lsd': lsd,
}
      data = {
    'lsd': lsd,
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+str(Id)+'","username":"leomessi"}',
    'server_timestamps': 'true',
    'doc_id': '7717269488336001',
}
      response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
      user =response.json()['data']['user']['username'] 
      ali(user)  
  except :
  	username1()

for i in range(10):
  Thread(target=username1).start()