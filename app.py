"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for
import datetime

videos = [
 u'7XwKnk16Zbs',
 u'-ZX1QMTdAC4',
 u'e4cpBBDVGGU',
 u'yzHcIzIVRKw',
 u'1ARPjekZPJw',
 u'TCoywIXVhgo',
 u'nntuDmKS6SM',
 u'3-th5SrJ1rQ',
 u'RSE95NF4eVc',
 u'Ol0r8lUqB-Q',
 u'Rcauv7ePD_0',
 u'UY31J5BeKrg',
 u'8bc6Jq6b0Ig',
 u'qmyEgk0zNPc',
 u'tJoTVVZadUs',
 u'WAYqWzQAjHo',
 u'2iiKibqIQ20',
 u'hzozw2Aso3M',
 u'vYTHwlV78y4',
 u'5nlarY4AdQw',
 u'UpLUCrq-JdM',
 u'yt8JteQMAag',
 u'fkPLnVU1KOo',
 u'pN-Vvk7QMNk',
 u'XEXFcPClb9Q',
 u'H4nWPeyDfNM',
 u'gCOXvGfWd8M',
 u'14Y-MU4o0ws',
 u'SaeAvGh6gkg',
 u'zSB9whpaSVI',
 u'TZtQ1hP0zFY'
]

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""

    context = {}

    day = datetime.datetime.today().day
    day -= 1

    if 'day' in request.args.keys():
        day = int( request.args['day'] )
        day = min( max( day, 0 ), len( videos ) - 1 )

    context['day']      = day
    context['video']    = videos[day]

    return render_template('home.html', **context)


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
