from flask import render_template, jsonify, json, request, current_app
from ..models import Queries
from . import deposits

@deposits.route('/deposits/edit/deposits_edit_submit', methods=['POST'])
def deposits_edit_submit():

    deposit_id = request.json['deposit_id']
    deposit_name = request.json['deposit_name']
    aliases = request.json['aliases']
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    database_name = request.json['database_name']
    production = request.json['production']
    grade = request.json['grade']
    geologic_unit = request.json['geologic_unit']
    ore_type = request.json['ore_type']
    discovery_year = request.json['discovery_year']

    ref_ids = request.json['ref_ids']
    mine_type = request.json['mine_type']
    commodities = request.json['commodities']

    district_ids = request.json['district_ids']
    country_id = request.json['country_id']
    state_id = request.json['state_id']
    county_id = request.json['county_id']


    #Query to get the inputs from referenc table
    Queries().deposits_edit_submit(deposit_id, deposit_name, aliases, latitude, longitude, database_name, production, grade, geologic_unit, ore_type, discovery_year, country_id, state_id, county_id, ref_ids, mine_type, commodities)

    Queries().deposits_edit_submit_districts(deposit_id, district_ids)

    return '0'

@deposits.route('/deposits/edit/deposit_SJM_new', methods=['POST'])
def deposits_new():

    #deposit_id = request.json['deposit_id']
    deposit_name = request.json['deposit_name']
    aliases = request.json['aliases']
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    database_name = request.json['database_name']
    production = request.json['production']
    grade = request.json['grade']
    geologic_unit = request.json['geologic_unit']
    ore_type = request.json['ore_type']
    discovery_year = request.json['discovery_year']
    country_id = request.json['country_id']
    state_id = request.json['state_id']
    county_id = request.json['county_id']
    ref_ids = request.json['ref_ids']
    mine_type = request.json['mine_type']
    commodities = request.json['commodities']

    district_ids = request.json['district_ids']

    #Query to get the inputs from referenc table
    #deposit_id_new = Queries().deposits_edit_new(deposit, source, filename, url, yn)
    rows = Queries().deposits_edit_sjmNew(deposit_name, aliases, latitude, longitude, database_name, production, grade, geologic_unit, ore_type, discovery_year, country_id, state_id, county_id, ref_ids, mine_type, commodities, district_ids)

    #deposit_id = '36669'
    #rows = {'deposit_id':deposit_id}
    jsonStr = json.dumps(rows)
    j = jsonify(myData=jsonStr)
    return j
    #return '0'

@deposits.route('/deposits/edit/deposits_delete', methods=['POST'])
def deposits_delete():

    deposit_id = request.json['deposit_id']
    #print("deposit_id ", deposit_id)

    #Query to delete the current reference
    Queries().deposits_edit_delete(deposit_id)
    return '0'

@deposits.route('/deposits/edit/deposits_edit_load_districts/<deposit_id>')
def deposits_edit_load_districts(deposit_id):
    #Query to get the inputs from deposit table
    rows = Queries().districts_by_deposit(deposit_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Load=jsonStr)
    return j

@deposits.route('/deposits/edit/deposits_edit_load_country/<deposit_id>')
def deposits_edit_load_country(deposit_id):
    #Query to get the inputs from deposit table
    rows = Queries().country_by_deposit(deposit_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Load=jsonStr)
    return j

@deposits.route('/deposits/edit/deposits_edit_load/<deposit_id>')
def deposits_edit_load(deposit_id):
    #Query to get the inputs from referenc table
    rows = Queries().deposits_edit_load(deposit_id)
    #print('In edit load view2 rows', rows)
    jsonStr = json.dumps(rows)
    j = jsonify(Load=jsonStr)
    return j

@deposits.route('/deposits/deposits_edit/<deposit_id>')
def deposits_edit(deposit_id):
    return render_template('deposits/edit.html', deposit_id=deposit_id)

@deposits.route('/deposits/deposits_by_database/<string:database_name>')
def deposits_by_database(database_name):
    rows = Queries().deposits_by_database(database_name)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    return j

@deposits.route('/deposits/deposits_by_district/<district_id>')
def deposits_by_district(district_id):
    rows = Queries().deposits_by_district(district_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    return j


@deposits.route('/deposits/deposits_search/<id>')
def deposits_search(id):
    #print('In deposits_search', id)
    rows = Queries().deposits_search(id)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    return j

# PUT THIS AT BOTTOM!
@deposits.route('/deposits_home')
def deposits_home():
    return render_template('deposits/deposits_home.html')
