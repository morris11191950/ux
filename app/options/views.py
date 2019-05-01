from flask import render_template, jsonify, json, request, session
from ..models import Queries
from . import options

# def get_db():
#     if 'db' not in g:
#         g.db = 'SJM''
#
#     return g.db

# PUT THIS AT BOTTOM!
@options.route('/options_home', methods=(['GET','POST']))
def options_home():

    if request.method == 'GET':
        #print('Views: Get')
        usrDatabases = session.get('usrDatabase')
        #print('Views2: Get', usrDatabases)
        if usrDatabases is None:
            session['usrDatabases'] = json.dumps(['SJM'])
        else:
            session['usrDatabases'] = usrDatabases

        return session['usrDatabases']

    if request.method == 'POST':
        req_data = request.get_json()
        print('Views: Post', req_data)
        session['usrDatabases'] = req_data
        #I really have no idea why this works
        resp = jsonify(success=True)
        return resp
