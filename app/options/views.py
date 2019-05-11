from flask import render_template, jsonify, json, request, session
from ..models import Queries
from . import options

# PUT THIS AT BOTTOM!
@options.route('/options_home', methods=(['GET','POST']))
def options_home():

    if request.method == 'GET':
        usrDatabases = session.get('usrDatabases')
        usrMapLabels_yn = session.get('usrMapLabels_yn')

        if usrMapLabels_yn is None:
            usrMapLabels_yn = 'n'

        if usrDatabases is None:
            usrDatabases = ['SJM']

        session['usrMaplabels_yn'] = usrMapLabels_yn
        session['usrDatabases'] = usrDatabases

        options = {"usrDatabases": usrDatabases, "usrMapLabels_yn" : usrMapLabels_yn}
        #print('options_home GET options: ', options, type(options))

        return jsonify(options)

    if request.method == 'POST':

        data = request.get_json()
        usrDatabases = data['usrDatabases']
        usrMapLabels_yn = data['usrMapLabels_yn']

        session['usrDatabases'] = usrDatabases
        session['usrMapLabels_yn'] = usrMapLabels_yn

        resp = jsonify(success=True)
        return resp
