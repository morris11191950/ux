from flask import render_template
from . import prospects

@prospects.route('/the_prospects')
def the_prospects():
    return render_template('prospects/the_prospects.html')
