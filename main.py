from flask import Flask, render_template
from flask import session, redirect, url_for, escape, request, jsonify
import json
import requests
from firebase import firebase

app = Flask(__name__)




@app.route("/")
def home():
	url = 'http://hackerearth.0x10.info/api/one-push?type=json&query=list_websites'
	response = requests.get(url).content
	response = json.loads(response)
	fire = firebase.FirebaseApplication('https://topplrchallengesept18.firebaseio.com/', None)
	response = fire.get('/websites', None)
	kwargs = locals()
	return render_template('home.html', **kwargs)


@app.route("/new_profile", methods=["POST"])
def add_new_profile():
	fire = firebase.FirebaseApplication('https://topplrchallengesept18.firebaseio.com/', None)
	result = fire.get('/websites', None)
	temp = request.data
	result = fire.post('/websites', h)
	
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(port=8000, debug=True)
