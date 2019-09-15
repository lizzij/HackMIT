import os

from flask import Flask, request, url_for, redirect, render_template, g
app = Flask(__name__)

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

