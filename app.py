from flask import Flask,request

import requests

app = Flask('app')

@app.route('/')

def home():

 return 'BY: @C_Y_L'

dewx = str(request.args.get('user'))

headers = {

    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

    'accept-encoding': 'gzip, deflate, br',

    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',

    'cookie': f'csrftoken={secrets.token_hex(8)*2}; sessionid={secrets.token_hex(8)*2};',

    'user-agent': generate_user_agent(),

    }

url = f'https://www.instagram.com/{dewx}/?__a=1'

req = rs.get(url,headers=headers).json()

dady= str(req['logging_page_id']).split('_')[1]

lord = f'https://o7aa.pythonanywhere.com/?id={dady}'

dadyx = rs.get(lord)

dewtools = dadyx.json()

datee = dewtools['data']

return jsonify(date=datee, user=user, Telegram="@Extracttt")
