import requests, json
#from requests_html import HTMLSession
from datetime import datetime
from bs4 import BeautifulSoup

session = requests.Session()
#session = HTMLSession()


time = int(datetime.now().timestamp())
# NEEDS
BaseUrl = 'https://www.instagram.com/'
LogUrl = 'https://www.instagram.com/accounts/login/ajax/'
MefastUrl = 'https://addmefast.com/login'

def loginIG():
	headers = {
		'user-agent' : 'Mozilla/5.0 (Linux; Android 9; SM-J3300) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'
	}
	Host = session.get(BaseUrl, headers=headers)
	print ('[ CONNECTINH WITH HOST ] > ',Host.ok)
	x_csrf_token = Host.cookies['csrftoken']
	headers.update({'x-csrftoken' : x_csrf_token })
	headers.update({'x-requested-with' : 'XMLHttpRequest'})
	headers.update({'referer' : 'https://www.instagram.com/accounts/login/'})
	
	payload = {
		'username' : 'Kada______',
		'enc_password' : f'#PWD_INSTAGRAM_BROWSER:0:{time}:'+'Doctorghost7',
		'queryParams' : {},
		'optIntoOneTap' : 'false'
	}
	login = session.post(LogUrl, headers=headers, data=payload)
	print ('[ LOGIN TO INSTAGRAM ] > ',login.text)
	
def loginAddFast():
	headers = {
		'user-agent' : 'Mozilla/5.0 (Linux; Android 9; SM-J3300) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
		'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'referer' : 'https://addmefast.com/login'
	}
	payload = {
		'email' : '8dtrapnation@gmail.com',
		'remember' : '1',
		'password' : 'Lbriztlfaza0@',
		'login_button' : 'Login'
	}
	
	LoginMe = session.post(MefastUrl, headers=headers, data=payload)
	print ('[ LOGIN TO ADDMEFAST ACCOUNT ] > ',LoginMe.ok)
	headers = {
		'user-agent' : 'Mozilla/5.0 (Linux; Android 9; SM-J3300) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
		'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'referer' : 'https://addmefast.com/free_points/instagram_likes?act=getLinksList&network=32&page=1'
	}

	LikesUrl = 'https://addmefast.com/free_points/instagram_likes?act=getLinksList&network=32&page=1'
	LikesData = session.get(LikesUrl, headers=headers)
	print ('[ DUMP LIKES LIST ] > ',LikesData.ok)
	print (LikesData.next)
	

	headers = {
		'user-agent' : 'Mozilla/5.0 (Linux; Android 9; SM-J3300) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
		'accept' : '*/*',
#		'content-length' : '52',
		'content-type' : 'application/x-www-form-urlencoded',
		'x-requested-with' : 'XMLHttpRequest',
		'referer' : 'https://addmefast.com/free_points/instagram_likes?act=getLinksList&network=32&page=1',
		'timsend' : str(LikesData.cookies['timsenf'])
#		'accept-encoding' : 'gzip, deflate, br',
#		'content-type' : 'text/html; charset=utf-8'
	}
	
	payload = {
		'act' : 'getLinksList',
		'network' : '32',
		'page' : '1'
	}
	FindUrl = 'https://addmefast.com/includes/ajax.php'
	FindData = session.post(FindUrl, headers=headers, data=payload)
	print (FindData.status_code)
	print (FindData.text)



loginAddFast()
