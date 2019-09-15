from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for

from flaskr.db import get_db
from werkzeug.exceptions import abort

bp = Blueprint('farmer', __name__)

@bp.route('/test')
def farmer():
    return trender_template('farmer.html')
