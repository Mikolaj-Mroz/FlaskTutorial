from app import app
from flask import render_template
import requests

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/name/<name>')
@app.route('/name')
def name(name = ""):
    return render_template('hi.html', name=name)


@app.route('/dog')
def dog():
    dog = requests.get('https://random.dog/woof.json').json()['url']
    video = False

    if dog[len(dog) -1] == "4":
        video = True

    return render_template('dog.html', dog=dog, video=video)