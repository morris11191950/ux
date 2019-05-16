from flask import render_template, jsonify, json, request, current_app
from ..models import Queries
from . import deposits

@deposits.route('/edit/deposits_edit_submit', methods=['POST'])
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
    country = request.json['country']
    state = request.json['state']
    county = request.json['county']
    ref_ids = request.json['ref_ids']
    mine_type = request.json['mine_type']
    commodities = request.json['commodities']

    district_ids = request.json['district_ids']

    #Query to get the inputs from referenc table
    Queries().deposits_edit_submit(deposit_id, deposit_name, aliases, latitude, longitude, database_name, production, grade, geologic_unit, ore_type, discovery_year, country, state, county, ref_ids, mine_type, commodities)

    Queries().deposits_edit_submit_districts(deposit_id, district_ids)

    return '0'

@deposits.route('/edit/deposits_new', methods=['POST'])
def deposits_new():

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
    country = request.json['country']
    state = request.json['state']
    county = request.json['county']
    ref_ids = request.json['ref_ids']
    mine_type = request.json['mine_type']
    commodities = request.json['commodities']

    district_ids = request.json['district_ids']

    #Query to get the inputs from referenc table
    #deposit_id_new = Queries().deposits_edit_new(deposit, source, filename, url, yn)
    #Queries().deposits_edit_submit_districts(deposit_id_new, district_ids)
    #print("refid_new ", refid_new)
    return deposit_id_new

@deposits.route('/edit/deposits_edit_load_districts/<deposit_id>')
def deposits_edit_load_districts(deposit_id):
    #Query to get the inputs from deposit table
    rows = Queries().districts_by_deposit(deposit_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Load=jsonStr)
    return j

@deposits.route('/edit/deposits_edit_load/<deposit_id>')
def deposits_edit_load(deposit_id):
    #Query to get the inputs from referenc table
    rows = Queries().deposits_edit(deposit_id)
    #print('In edit load view2 rows', rows)
    jsonStr = json.dumps(rows)
    j = jsonify(Load=jsonStr)
    return j

@deposits.route('/deposits/deposits_edit/<deposit_id>')
def deposits_edit(deposit_id):
    #print('In edit view deposit_id', deposit_id)
    return render_template('deposits/edit.html', deposit_id=deposit_id)

@deposits.route('/databases_all')
def databases_all():
    rows = Queries().databases_all()
    jsonStr = json.dumps(rows)
    j = jsonify(Databases=jsonStr)
    return j

@deposits.route('/deposits_by_database/<string:database_name>')
def deposits_by_database(database_name):
    rows = Queries().deposits_by_database(database_name)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    return j

@deposits.route('/deposits_by_district/<district_id>')
def deposits_by_district(district_id):
    rows = Queries().deposits_by_district(district_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Deposits=jsonStr)
    return j

@deposits.route('/deposits_search/<id>')
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
