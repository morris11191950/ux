from flask import render_template, jsonify, json, request, session
from ..models import Queries
from . import options

@options.route('/options_get_current_dbs')
def options_get_current_dbs():
    # print('I am here in get_current')
    usrDatabases = session.get('usrDatabases')
    #print('options_get_current_dbs usrDatabases', usrDatabases)
    #print('options_get_current_dbs usrDatabases TYPE: usrDatabases', type(usrDatabases))
    if usrDatabases is None:
         usrDatabases = ['SJM']
         #print('get_current y', y, ' ', type(y))
    session['usrDatabases'] = usrDatabases
    #print('options_get_current_db out usrDatabases', usrDatabases)
    #print('options_get_current_db out TYPE', type(usrDatabases))
    return jsonify(usrDatabases)

# PUT THIS AT BOTTOM!
@options.route('/options_home', methods=(['GET','POST']))
def options_home():

    if request.method == 'GET':
        #print('Views: Get')
        usrDatabases = session.get('usrDatabases')
        #print('options_home GET (usrDatabases)', usrDatabases)
        #print('options_home GET TYPE', type(usrDatabases))
        if usrDatabases is None:
            usrDatabases = ['SJM']
        # else:
        #     session['usrDatabases'] = json.dumps(usrDatabases)
        session['usrDatabases'] = usrDatabases
        #print('options_home GET usrDatabases: ', usrDatabases)
        #print('options_home TYPE ', type(usrDatabases))
        return jsonify(usrDatabases)

    if request.method == 'POST':
        req_data = request.get_json()
        #print('Views: 1', session['usrDatabases'])
        session['usrDatabases'] = req_data
        #print('options_home Views: post (session[usrDatabases])', session['usrDatabases'])
        #print('options_home Type: ', type(session['usrDatabases']))
        #I really have no idea why this works
        resp = jsonify(success=True)
        #print(resp, type(resp))
        return resp
