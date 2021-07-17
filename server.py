from flask import Flask, Response, jsonify
import json
import os
import time
import requests
from datetime import datetime
from zipfile import ZipFile

api_key = "b5b78b88bc8fb7b55aa93b9cbef9c604"
lat = "37.7272"
lon = "-123.032"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

app = Flask(__name__)

@app.route("/servicio/v2/prediccion/24horas", methods=['GET'])
def hours_24():
    response = requests.get(url)
    data = json.loads(response.text)
    prediction = [
        {
            'hour': datetime.utcfromtimestamp(d['dt']).strftime('%Y-%m-%d %H:%M:%S'),
            'temp': d['temp'],
            'hum': d['humidity']
        } for d in data['hourly']
    ]
    response = Response(json.dumps(prediction[0:24]), status=200)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route("/servicio/v2/prediccion/48horas", methods=['GET'])
def hours_48():
    response = requests.get(url)
    data = json.loads(response.text)
    prediction = [
        {
            'hour': datetime.utcfromtimestamp(d['dt']).strftime('%Y-%m-%d %H:%M:%S'),
            'temp': d['temp'],
            'hum': d['humidity']
        } for d in data['hourly']
    ]
    response = Response(json.dumps(prediction[0:48]), status=200)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route("/servicio/v2/prediccion/72horas", methods=['GET'])
def hours_72():
    response = requests.get(url)
    data = json.loads(response.text)
    prediction = [
        {
            'hour': datetime.utcfromtimestamp(d['dt']).strftime('%Y-%m-%d %H:%M:%S'),
            'temp': d['temp'],
            'hum': d['humidity']
        } for d in data['hourly']
    ]
    response = Response(json.dumps(prediction[0:72]), status=200)
    response.headers['Content-Type'] = 'application/json'
    return response
