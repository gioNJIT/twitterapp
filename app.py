import os
from flask import Flask, send_from_directory
import os
import urllib.request
import requests
from flask import Flask, request, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


app = Flask(__name__, static_folder='./build/static')

load_dotenv(find_dotenv())


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
import models


@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)

#twitter api call
@app.route('/Twitterapi', methods=['POST'])
def twitteruser():
        
        #what we're getting from react page
        username = request.json['username']
        
        #setting up the url and headers
        url='https://api.twitter.com/2/users/by/username/' + username
        headers = {'Authorization': "Bearer "+os.getenv('TWITTER_TOKEN') }
        
        #sending and receiving data from twitter to get the user id #
        id_r = requests.get(url,headers=headers)
        response_id = id_r.json()
        
        #making another call to twitter with the user id # in order to get the tweets
        url2='https://api.twitter.com/2/users/'+response_id['data']['id']+'/tweets'
        tweets_r=requests.get(url2,headers=headers)
        tweetdata=tweets_r.json()
        tweetsAnd_ids={}
        #creating a loop to extract the tweets and the ids associated with them
        
        for x in range(len(tweetdata['data'])):
            tweetsAnd_ids[tweetdata['data'][x]['id']]=tweetdata['data'][x]['text']
            print(tweetdata['data'][x]['text'])
        
        
        #MICROSOFT API   
        micro_key=os.getenv('MICROKEY')
        endpoint='https://twitter-bot.cognitiveservices.azure.com/'
        
        #creatiing credentials to be used when accessing microsoft API
        ta_credential = AzureKeyCredential(micro_key)
        text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
        
        
        # testing out "key phrase extraction" function in the text analytics api.
        try:
            documents = [tweetdata['data'][x]['text']]

            response = text_analytics_client.extract_key_phrases(documents = documents)[0]

            if not response.is_error:
                print("\tKey Phrases:")
                for phrase in response.key_phrases:
                    print("\t\t", phrase)
            else:
                print(response.id, response.error)

        except Exception as err:
            print("Encountered exception. {}".format(err))

        
	
        return('ok')

if __name__ == "__main__":
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
