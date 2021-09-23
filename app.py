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
    return "<p><a href=\"https://github.com/tylerth/apex_api/blob/dev/README.md\">Click here</a> to view available endpoints and usage documentation.</p>"

@app.route("/<platform>/<user>")
def get_user_data(user=None,platform=None,api_key=api_key):
    player_data = player_request(user=user, platform=platform, api_key=api_key)

    return get_player_data(player_data)


@app.route("/<platform>/<user>/legends")
def get_legends_data(user=None,platform=None,legend=None,api_key=api_key):
    player_data = player_request(user=user, platform=platform, api_key=api_key)
    
    return get_all_legends_data(player_data)


@app.route("/<platform>/<user>/<legend>")
def get_legend_data(user=None,platform=None,legend=None,api_key=api_key):
    player_data = player_request(user=user, platform=platform, api_key=api_key)

    return get_indiv_legend_data(legend, player_data)


@app.route("/map_rotations")
def get_map_rotations(api_key=api_key):
    map_data = map_request(api_key)

    return get_all_map_rotation_data(map_data)


@app.route("/map_rotation/<gamemode>")
def get_map_rotation(gamemode=None,api_key=api_key):
    map_data = map_request(api_key)

    return get_indiv_map_rotation(gamemode, map_data)