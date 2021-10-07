import os
from flask import Flask, send_from_directory
import os
import urllib.request
import requests
from flask import Flask, request, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv


app = Flask(__name__, static_folder='./build/static')

load_dotenv(find_dotenv())


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
import models


@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)


@app.route('/Twitterapi', methods=['POST'])
def twitteruser():
        username = request.json['username']
        
        url='https://api.twitter.com/2/users/by/username/' + username
        headers = {'Authorization': "Bearer "+os.getenv('TWITTER_TOKEN') }

        id_r = requests.get(url,headers=headers)
        response_id = id_r.json()
        print(response_id['data']['id'])
        url2='https://api.twitter.com/2/users/'+response_id['data']['id']+'/tweets'

        tweets_r=requests.get(url2,headers=headers)
        print(tweets_r.json())
	
        return('ok')

if __name__ == "__main__":
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
