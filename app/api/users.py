from flask import jsonify, request, g, current_app, url_for

from .decorators import permission_required
from .errors import forbidden
from .. import db
from ..models import User, Permission
from . import api
from .authentication import auth


@api.route('/users/<int:id>')
@auth.login_required
def get_user(id):
    user = User.query.get_or_404(id)
    if g.current_user != user and \
            not g.current_user.can(Permission.ADMIN):
        return forbidden('Insufficienet permissions')
    return jsonify(user.to_json())


@api.route('/users/', methods=['POST'])
@auth.login_required
@permission_required(Permission.ADMIN)
def new_user():
    user = User.from_json(request.json)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 201, \
        {'Location': url_for('api.get_user', id=user.id)}


@api.route('/users/<int:id>', methods=['PUT'])
@auth.login_required
def edit_user(id):
    user = User.query.get_or_404(id)
    if g.current_user != user and \
            not g.current_user.can(Permission.ADMIN):
        return forbidden('Insufficient permissions')
    user.username = request.json.get('username', user.username)
    user.password = request.json.get('password')
    user.first_name = request.json.get('first_name', user.first_name)
    user.last_name = request.json.get('last_name', user.last_name)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json())


@api.route('/users/', methods=['DELETE'])
@auth.login_required
def delete_user():
    g.current_user.remove()
    db.session.commit()
    return jsonify({'Message': 'deleted'})
