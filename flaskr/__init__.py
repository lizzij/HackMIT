import os
import pymongo

from flask import Flask, request, url_for, redirect, render_template, g

uri = 'mongodb://hackmit:FPj59IerX8J4Yk570tJKYK6S1GkDeXPdvIH7cUmqJVFYwwJHqCkr7mPcSLzY4N6VitcgMIvrr7bTOHqotEaQQg==@hackmit.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'
client = pymongo.MongoClient(uri)
db = client['freshdetect']
dbcol = db['readings']


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/db')
    def db():
        return dbcol

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/farmer')
    def farmer():
        return render_template('farmer.html')

    @app.route('/shipper')
    def shipper():
        return render_template('shipper.html')

    @app.route('/buyer')
    def buyer():
        return render_template('buyer.html')

    @app.route('/comingSoon')
    def coming_soon():
        return render_template('comingSoon.html')

    return app
