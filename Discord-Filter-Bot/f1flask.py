from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello Maximus!"

def run():
  app.run(host='0.0.0.0',port=8080)

def acti_ve():
    t = Thread(target=run)
    t.start()