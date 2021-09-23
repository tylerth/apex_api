from flask import Flask
from flask import request
import requests
from apex import *

#python3 -m pip install flask
api_key = "Wd6slHMRDXFFpSF7UQro"
app = Flask(__name__)
app.debug = True

@app.route("/")
def hello_world():
    return "<p>Usage:</p><p></p>"

@app.route("/<platform>/<user>")
def get_user_data(user=None,platform=None,api_key=api_key):
    player_data = player_request(user=user, platform=platform, api_key=api_key)

    return get_player_data(player_data)

@app.route("/map_rotations")
def get_map_rotation(api_key=api_key):
    map_data = map_request(api_key)

    return get_all_map_rotation_data(map_data)

@app.route("/<platform>/<user>/legends")
def get_legends_data(user=None,platform=None,legend=None,api_key=api_key):
    player_data = player_request(user=user, platform=platform, api_key=api_key)
    
    return get_all_legends_data(player_data)

@app.route("/<platform>/<user>/<legend>")
def get_legend_data(user=None,platform=None,legend=None,api_key=api_key):
    player_data = player_request(user=user, platform=platform, api_key=api_key)

    body = {}

    body['legend'] = legend
    
    try:
        legend_data = player_data['legends']['all'][legend]['data']
        tracker_1_name, tracker_1_value = legend_data[0]['name'], legend_data[0]['value']
        tracker_2_name, tracker_2_value = legend_data[1]['name'], legend_data[1]['value']
        tracker_3_name, tracker_3_value = legend_data[2]['name'], legend_data[2]['value']

        body[tracker_1_name] = tracker_1_value
        body[tracker_2_name] = tracker_2_value
        body[tracker_3_name] = tracker_3_value

    except:
        body['data'] = 'Missing data for {}'.format(legend)
    
    return body