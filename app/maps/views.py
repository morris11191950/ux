
from flask import render_template, jsonify, json, request, current_app
from ..models import Queries
from . import maps

@maps.route('/deposits_by_district/<int:district_id>')
def deposits_by_district(district_id):
    rows = Queries().deposits_by_district(district_id)

    #print('maps views: rows ', rows, type(rows))
    # rows.append({'deposit_id': 999999, 'deposit_name': 'Standard Tunnel', 'latitude': 38.18719, 'longitude': -109.25929, 'state': 'Utah', 'country': 'United States', 'county': 'San Juan', 'district_name': 'Lisbon Valley District', 'pounds_u3o8': None, 'grade': None, 'database_name': 'sjm'})
    jsonStr = json.dumps(rows)
    #print('maps views: jsonStr ', jsonStr, type(jsonStr))
    j = jsonify(Deposits=jsonStr)
    #print('maps views: j ', j, type(j))
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

# @maps.route('/deposits_by_deposit/<int:deposit_id>')
# def deposits_by_deposit(deposit_id):
#     rows = Queries().deposits_by_deposit(deposit_id)
#     jsonStr = json.dumps(rows)
#     j = jsonify(Deposits=jsonStr)
#     #print('rows in views ', rows)
#     return j

@maps.route('/deposits_by_deposit/<string:selected_id_str>')
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
    #print('In Views: maps home 2')
    return render_template('maps/maps_home.html', CESIUM_API_KEY=cesium_api_key)
    #return render_template('maps/maps_home.html',)
