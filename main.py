from flask import Flask, render_template
import json
import requests
app = Flask(__name__)




@app.route("/")
def home():
	url = 'http://hackerearth.0x10.info/api/one-push?type=json&query=list_websites'
	response = requests.get(url).content
	response = json.loads(response)
	kwargs = locals()
	return render_template('home.html', **kwargs)

if __name__ == '__main__':
	app.run(port=8000, debug=True)