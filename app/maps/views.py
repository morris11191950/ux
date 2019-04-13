
from flask import render_template, jsonify, json, request, current_app
from ..models import Queries
from . import maps

@maps.route('/deposits_by_district/<int:district_id>')
def deposits_by_district(district_id):
    rows = Queries().deposits_by_district(district_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    #print('j in views ', rows)
    return j

@maps.route('/deposits_by_county/<int:county_id>/<int:state_id>')
def deposits_by_county(county_id, state_id):
    #print('county_id in views ', county_id)
    #print('state_id in views ', state_id)
    rows = Queries().deposits_by_county(county_id, state_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    #print('j in views ', rows)
    return j

@maps.route('/maps_home')
def maps_home():
    cesium_api_key = current_app.config['CESIUM_API_KEY']
    return render_template('maps/maps_home.html', CESIUM_API_KEY=cesium_api_key)
    #return render_template('maps/maps_home.html',)
