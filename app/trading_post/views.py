from flask import render_template
from . import trading_post

@trading_post.route('/the_trading_post')
def the_trading_post():
    return render_template('trading_post/the_trading_post.html')
