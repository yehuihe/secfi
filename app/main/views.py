from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import main
from .. import db


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/remove', methods=['GET', 'POST'])
@login_required
def remove():
    current_user.remove()
    db.session.commit()
    flash('You are no longer exist')
    return redirect(url_for('.index'))