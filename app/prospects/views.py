from flask import render_template
from . import prospects

@prospects.route('/prospects/the_prospects')
def the_prospects():
    return render_template('/prospects/the_prospects.html')

@prospects.route('/prospects/GVMS')
def GVMS():
    return render_template('/prospects/GVMS.html')
