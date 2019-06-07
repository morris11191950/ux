
from flask import render_template, jsonify, json, request, current_app
from ..models import Queries
from . import maps

@maps.route('/maps/deposits_by_district/<int:district_id>')
def deposits_by_district(district_id):
    rows = Queries().deposits_by_district(district_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    #print('maps views: j ', j, type(j))
    return j

@maps.route('/maps/deposits_by_county/<int:county_id>/<int:state_id>')
def deposits_by_county(county_id, state_id):
    rows = Queries().deposits_by_county(county_id, state_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    #print('j in views ', rows)
    return j

@maps.route('/maps/deposits_by_deposit/<string:selected_id_str>')
def deposits_by_deposit(selected_id_str):
    #print('selected_id_str views ', selected_id_str)
    rows = Queries().deposits_by_deposit(selected_id_str)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    #print('rows in views ', rows)
    return j

@maps.route('/maps_home')
def maps_home():
    #print('In Views: maps home 1')
    cesium_api_key = current_app.config['CESIUM_API_KEY']
    return render_template('maps/maps_home.html', CESIUM_API_KEY=cesium_api_key)
