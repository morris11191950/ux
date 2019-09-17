
from flask import render_template, jsonify, json, request, current_app
from ..models import Queries
from . import maps

@maps.route('/maps/deposits_sjm')
def deposits_sjm():
    #print('I am here1')
    rows = Queries().deposits_sjm()
    #print('I am here2')
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    return j

@maps.route('/maps/deposits_by_district/<int:district_id>')
def deposits_by_district(district_id):
    rows = Queries().deposits_by_district(district_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    return j

@maps.route('/maps/deposits_by_county/<int:county_id>/<int:state_id>')
def deposits_by_county(county_id, state_id):
    rows = Queries().deposits_by_county(county_id, state_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    return j

@maps.route('/maps/deposits_by_country/<int:country_id>')
def deposits_by_country(country_id):
    rows = Queries().deposits_by_country(country_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    return j

@maps.route('/maps/deposit_by_deposit/<string:selected_id>')
def deposit_by_deposit(selected_id):
    print('In maps routes: deposit_by_deposit:selected_id:  ', selected_id)
    row = Queries().deposit_by_deposit(selected_id)
    #print('I am here4')
    print('row:', row)
    jsonStr = json.dumps(row)
    j = jsonify(Deposit=jsonStr)
    print('j', j)
    return j

@maps.route('/maps_home')
def maps_home():
    cesium_api_key = current_app.config['CESIUM_API_KEY']
    return render_template('maps/maps_home.html', CESIUM_API_KEY=cesium_api_key)
