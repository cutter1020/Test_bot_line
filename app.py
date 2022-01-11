from flask import Flask, request, abort
import requests
import json

app = Flask(__name__)
#Chanel_secret=0ad68e1a4b617c942a86145fe8994871
Line_Acees_Token=AuGyC3yQQYzA8iuoSt0G4epKlpneubvFF++mPezDYcd/poKjxryJbDt/l5J9T8e+d91WZQyS0iKnUcgIrscSaTpUpNouYaY8uJnwf4ocT5BkSNzqmq22/DFkAWmMjdcsa1HfqqTz3YKo9nzIXcMfpAdB04t89/1O/w1cDnyilFU=


@app.route('/webhook', methods=['POST','GET'])

def webhook():
    if request.method == 'POST':
        payload = request.json

        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        print(message)
        if 'หุ้น' in message :
            ITD = '1'
            Reply_messasge = 'ราคาหุ้น อิตาเลียนไทย ขณะนี้ : {}'.format(ITD)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(400)

@app.route('/')
def hello():
    return 'hello world book',200

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) ##ที่ยาวๆ
    #print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data =
    {
        "replyToken":Reply_token,
        "messages":
        [{
            "type":"text",
            "text":TextMessage
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200
