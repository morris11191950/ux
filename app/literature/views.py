from flask import render_template, jsonify, json, request, redirect, url_for
from . import literature
from ..models import Queries

@literature.route('/literature/databases_all')
def databases_all():
    rows = Queries().databases_all()
    jsonStr = json.dumps(rows)
    j = jsonify(Databases=jsonStr)
    return j

@literature.route('/literature/categories_all')
def categories_all():
    rows = Queries().categories_all()
    jsonStr = json.dumps(rows)
    j = jsonify(Categories=jsonStr)
    return j

@literature.route('/literature/specialCollections_all')
def specialCollections_all():
    #print('I made it to special collections')
    rows = Queries().specialCollections_all()
    jsonStr = json.dumps(rows)
    j = jsonify(SpecialCollections=jsonStr)
    return j

@literature.route('/literature/districts_all')
def districts_all():
    rows = Queries().districts_all()
    jsonStr = json.dumps(rows)
    j = jsonify(Districts=jsonStr)
    return j

@literature.route('/literature/countries_all')
def countries_all():
    rows = Queries().countries_all()
    jsonStr = json.dumps(rows)
    #print('countries rows ', rows)
    j = jsonify(Countries=jsonStr)
    return j

@literature.route('/literature/states_all')
def states_all():
    rows = Queries().states_all()
    jsonStr = json.dumps(rows)
    #print('states rows ', rows)
    j = jsonify(States=jsonStr)
    return j

@literature.route('/literature/counties_all')
def counties_all():
    rows = Queries().counties_all()
    jsonStr = json.dumps(rows)
    #print('counties rows ', rows)
    j = jsonify(Counties=jsonStr)
    return j

@literature.route('/literature/deposits_all')
def deposits_all():
    rows = Queries().deposits_all()
    jsonStr = json.dumps(rows)
    #print('deposits views ')
    j = jsonify(Deposits=jsonStr)
    return j

@literature.route('/literature/references_all')
def references_all():
    rows = Queries().references_all()
    jsonStr = json.dumps(rows)
    # print('rows ', rows)
    j = jsonify(Refs=jsonStr)
    return j

@literature.route('/literature/references_by_category/<int:category_id>')
def references_by_category(category_id):
    rows = Queries().references_by_category(category_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Refs=jsonStr)
    return j

@literature.route('/literature/references_by_specialCollection/<int:spcol_id>')
def references_by_specialCollection(spcol_id):
    #print('Views:references_by_specialCollection spcol_id', spcol_id)
    rows = Queries().references_by_specialCollection(spcol_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Refs=jsonStr)
    return j

@literature.route('/literature/references_by_district/<int:district_id>')
def references_by_district(district_id):
    rows = Queries().references_by_district(district_id)
    jsonStr = json.dumps(rows)
    j = jsonify(Refs=jsonStr)
    return j

@literature.route('/literature/references_edit/<refid>')
def references_edit(refid):
    #Get new reference id
    #print('references_edit1 in views, refid: ', refid)
    #print('type refid1 in views: ', type(refid))
    if refid == '0':
        #print('references_edit2 in views, refid: ', refid)
        refid = Queries().references_newRefid()
    #print('references_edit3 in views, refid: ', refid)
    return render_template('literature/edit.html', refid=refid)

@literature.route('/literature/references_search/<id>')
def references_search(id):
    rows = Queries().references_search(id)
    jsonStr = json.dumps(rows)
    j = jsonify(Refs=jsonStr)
    return j

##########################################################################
##########################################################################
# LITERATURE EDITS
##########################################################################
##########################################################################
@literature.route('/literature/edit/references_edit_load/<refid>')
def references_edit_load(refid):
    #Query to get the inputs from referenc table
    rows = Queries().references_edit(refid)
    jsonStr = json.dumps(rows)
    j = jsonify(Load=jsonStr)
    return j

@literature.route('/literature/edit/references_edit_load_districts/<refid>')
def references_edit_load_districts(refid):
    #Query to get the inputs from referenc table
    rows = Queries().districts_by_reference(refid)
    jsonStr = json.dumps(rows)
    j = jsonify(Load=jsonStr)
    return j

@literature.route('/literature/edit/references_edit_load_categories/<refid>')
def references_edit_load_categories(refid):
    #Query to get the inputs from referenc table
    rows = Queries().categories_by_reference(refid)
    jsonStr = json.dumps(rows)
    j = jsonify(Load=jsonStr)
    return j

@literature.route('/literature/edit/references_edit_load_specials/<refid>')
def references_edit_load_specials(refid):
    #Query to get the inputs from referenc table
    rows = Queries().specialCollections_by_reference(refid)
    jsonStr = json.dumps(rows)
    j = jsonify(Load=jsonStr)
    return j

@literature.route('/literature/edit/references_new', methods=['POST'])
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
    special_ids = request.json['special_ids']

    #print('yn', yn)

    if yn == 'yes':
         yn = 'y'
    else:
         yn = 'n'

    #Query to get the inputs from referenc table
    refid_new = Queries().references_edit_new(reference, source, filename, url, yn)
    #Queries().references_edit_submit_districts(refid_new, district_ids)
    #Queries().references_edit_submit_categories(refid_new, category_ids)
    #Queries().references_edit_submit_specials(refid_new, special_ids)
    #print("refid_new ", refid_new)
    return refid_new

@literature.route('/literature/edit/references_delete', methods=['POST'])
def references_delete():

    refid = request.json['refid']
    #print("refid ", refid)

    #Query to delete the current reference
    refid_new = Queries().references_edit_delete(refid)

    return refid_new

@literature.route('/literature/edit/references_edit_save', methods=['POST'])
def references_edit_save():

    refid = request.json['refid']
    reference = request.json['reference']
    source = request.json['source']
    filename = request.json['filename']
    url = request.json['url']
    yn = request.json['yn']
    district_ids = request.json['district_ids']
    category_ids = request.json['category_ids']
    special_ids = request.json['special_ids']

    if yn == 'yes':
         yn = 'y'
    else:
         yn = 'n'

    #Query to get the inputs from referenc table
    print("references_edit_save1 in views, refid: ", refid)
    Queries().references_edit_save(refid, reference, source, filename, url, yn)
    print("references_edit_save2 in views, refid: ", refid)
    Queries().references_edit_save_districts(refid, district_ids)
    print("references_edit_save3 in views, refid: ", refid)
    Queries().references_edit_save_categories(refid, category_ids)
    print("references_edit_save4 in views, refid: ", refid)
    Queries().references_edit_save_specials(refid, special_ids)
    return '0'

@literature.route('/literature/url_pdf/<id>')
def url_pdf(id):
    row = Queries().url_pdf(id)
    jsonStr = json.dumps(row)
    j = jsonify(Url=jsonStr)
    return j

# THIS MUST BE AT BOTTOM!
@literature.route('/literature')
def literature():
    return render_template('literature/literature.html')
