from flask import render_template, jsonify, json, request
from . import literature
from ..models import Queries

@literature.route('/categories_all')
def categories_all():
    rows = Queries().categories_all()
    jsonStr = json.dumps(rows)
    j = jsonify(Categories=jsonStr)
    return j

@literature.route('/districts_all')
def districts_all():
    rows = Queries().districts_all()
    jsonStr = json.dumps(rows)
    j = jsonify(Districts=jsonStr)
    return j

@literature.route('/references_all')
def references_all():
    rows = Queries().references_all()
    jsonStr = json.dumps(rows)
    j = jsonify(Refs=jsonStr)
    return j

@literature.route('/references_by_category/<int:category_id>')
def references_by_category(category_id):
    rows = Queries().references_by_category(category_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Refs=jsonStr)
    return j

@literature.route('/references_by_district/<int:district_id>')
def references_by_district(district_id):
    rows = Queries().references_by_district(district_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Refs=jsonStr)
    return j

@literature.route('/literature/references_edit/<refid>')
def references_edit(refid):
    #print('refid ', refid)
    return render_template('literature/edit.html', refid=refid)

@literature.route('/references_search/<id>')
def references_search(id):
    rows = Queries().references_search(id)
    jsonStr = json.dumps(rows)
    j = jsonify(Refs=jsonStr)
    return j

@literature.route('/edit/references_edit_load/<refid>')
def references_edit_load(refid):
    #Query to get the inputs from referenc table
    rows = Queries().references_edit(refid)
    jsonStr = json.dumps(rows)
    j = jsonify(Load=jsonStr)
    return j

@literature.route('/edit/references_edit_load_districts/<refid>')
def references_edit_load_districts(refid):
    #Query to get the inputs from referenc table
    rows = Queries().districts_by_reference(refid)
    jsonStr = json.dumps(rows)
    j = jsonify(Load=jsonStr)
    return j

@literature.route('/edit/references_edit_load_categories/<refid>')
def references_edit_load_categories(refid):
    #Query to get the inputs from referenc table
    rows = Queries().categories_by_reference(refid)
    jsonStr = json.dumps(rows)
    j = jsonify(Load=jsonStr)
    return j

@literature.route('/edit/references_new', methods=['POST'])
def references_new():

    refid = request.json['refid']
    reference = request.json['reference']
    source = request.json['source']
    filename = request.json['filename']
    url = request.json['url']
    district_ids = request.json['district_ids']
    yn = request.json['yn']
    district_ids = request.json['district_ids']
    category_ids = request.json['category_ids']

    print('yn', yn)

    if yn == 'yes':
         yn = 'y'
    else:
         yn = 'n'

    #Query to get the inputs from referenc table
    refid_new = Queries().references_edit_new(reference, source, filename, url, yn)
    Queries().references_edit_submit_districts(refid_new, district_ids)
    Queries().references_edit_submit_categories(refid_new, category_ids)
    #print("refid_new ", refid_new)
    return refid_new

@literature.route('/edit/references_delete', methods=['POST'])
def references_delete():

    refid = request.json['refid']
    #print("refid ", refid)

    #Query to delete the current reference
    Queries().references_edit_delete(refid)

    return '0'

@literature.route('/edit/references_edit_submit', methods=['POST'])
def references_edit_submit():

    refid = request.json['refid']
    reference = request.json['reference']
    source = request.json['source']
    filename = request.json['filename']
    url = request.json['url']
    yn = request.json['yn']
    district_ids = request.json['district_ids']
    category_ids = request.json['category_ids']

    #print("district_ids: ", district_ids)

    if yn == 'yes':
         yn = 'y'
    else:
         yn = 'n'

    #Query to get the inputs from referenc table
    Queries().references_edit_submit(refid, reference, source, filename, url, yn)
    Queries().references_edit_submit_districts(refid, district_ids)
    Queries().references_edit_submit_categories(refid, category_ids)
    return '0'

@literature.route('/url_pdf/<id>')
def url_pdf(id):
    row = Queries().url_pdf(id)
    jsonStr = json.dumps(row)
    j = jsonify(Url=jsonStr)
    return j

# THIS MUST BE AT BOTTOM!
@literature.route('/literature')
def literature():
    return render_template('literature/literature.html')
