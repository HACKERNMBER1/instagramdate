from flask import Flask,request
import requests
app =	Flask('app')
@app.route('/')
def home():
	return 'BY: @APISFREE'
	
@app.route('/api/instagram/info/',methods=['GET'])
def index():
	user =	str(request.args.get('user'))
	url = 'https://www.instagram.com/'+str(user)+'/?__a=1'
	headers =	{
'Host': 'www.instagram.com',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,de-DE;q=0.6,de;q=0.5',
'cookie': 'mid=YZkPjQABAAER3b51Z8ah-YVxu-xm',
'cookie': 'ig_did=BEB7DE0C-FD7B-4ABB-A6C1-8A522CEA34DC',
'cookie': 'ig_nrcb=1',
'cookie': 'csrftoken=wM6BVNacm7VTF40daho2bwgYqInjifuo',
'cookie': 'ds_user_id=51709139961',
'cookie': 'sessionid=51709139961%3AMbTXsYBElAevDn%3A11'
	}
	response =	requests.get(url,headers=headers).text
	return response
app.run(host='0.0.0.0',port=8080)
