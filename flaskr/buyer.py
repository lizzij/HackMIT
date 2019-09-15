from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for

from flaskr.db import get_db
from werkzeug.exceptions import abort

bp = Blueprint('buyer', __name__)

@bp.route('/')
def buyer():
    return render_template('buyer.html')
