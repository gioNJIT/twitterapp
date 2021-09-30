import os
from flask import Flask, send_from_directory
import os
import urllib.request
from flask import Flask, request, redirect, render_template, jsonify
app = Flask(__name__, static_folder='./build/static')


@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)


@app.route('/Twitterapi', methods=['POST'])
def twitteruser():
        username = request.json['username']
        print("testing@@@@@@@@@@@@@@@@@@@")
        print(username)
	    	
        return('ok')

if __name__ == "__main__":
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
