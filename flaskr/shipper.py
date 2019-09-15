from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for

from flaskr.db import get_db
from werkzeug.exceptions import abort

bp = Blueprint('shipper', __name__)

@bp.route('/')
def shipper():
    return render_template('shipper.html')
