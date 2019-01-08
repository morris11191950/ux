from flask import render_template, current_app
from . import maps

@maps.route('/maps_home')
def maps_home():
    cesium_api_key = current_app.config['CESIUM_API_KEY']
    return render_template('maps/maps_home.html', CESIUM_API_KEY=cesium_api_key)
