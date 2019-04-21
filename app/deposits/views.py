from flask import render_template, jsonify, json, request, current_app
from ..models import Queries
from . import deposits

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
