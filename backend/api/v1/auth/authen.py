#!/usr/bin/python3
"""
    Authentication for parent and school
"""
from flask import jsonify, request
from ..auth import auth_parent
from ..auth import auth_school
from models.school import School
from models.parent import Parent
from models import storage
from flask_bcrypt import check_password_hash
from flask_jwt_extended import create_access_token
import datetime


# Signup
@auth_school.route('/signup', methods=['POST'], strict_slashes=False)
def signup():
    """
    signup - function that handles signup for school.

    Returns:
        json: school id
    """
    body = request.get_json()
    school = storage.first(School, {'email': body.get('email')})

    # if school is true return email already used.
    if school:
        return jsonify({'error': 'Email address already exists'})

    new_school = School(**body)
    id = new_school.id
    storage.new(new_school)
    storage.save()
    storage.close()

    return jsonify({'id': id}), 200


@auth_parent.route('/signup', methods=['POST'], strict_slashes=False)
def signup():
    """
    signup - function that handles signup for parent.

    Returns:
        json: parent id
    """
    body = request.get_json()
    parent = storage.first(Parent, {'email': body.get('email')})

    # if parent is true return email already used.
    if parent:
        return jsonify({'error': 'Email address already exists'}), 401

    new_parent = Parent(**body)
    id = new_parent.id
    storage.new(new_parent)
    storage.save()
    storage.close()

    return jsonify({'id': id}), 200


# Login
@auth_school.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """
    login - function that handles login session for school.

    Returns:
        json: access token
    """
    body = request.get_json()
    school = storage.first(School, {'email': body.get('email')})
    if not school:
        return jsonify({'error': 'No account registered to this email'}), 401

    authorized = check_password_hash(school.password, body.get('password'))
    if not authorized:
        return jsonify({'error': 'Email or password invalid'}), 401

    expires = datetime.timedelta(days=3)
    access_token = create_access_token(identity=school.id,
                                       expires_delta=expires)

    return jsonify({'token': access_token}), 200


@auth_parent.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """
    login - function that handles login session for parent.

    Returns:
        json: access token
    """
    body = request.get_json()
    parent = storage.first(Parent, {'email': body.get('email')})
    if not parent:
        return jsonify({'error': 'No account registered to this email'}), 401

    authorized = check_password_hash(parent.password, body.get('password'))
    if not authorized:
        return jsonify({'error': 'Email or password invalid'}), 401

    expires = datetime.timedelta(days=3)
    access_token = create_access_token(identity=parent.id,
                                       expires_delta=expires)

    return jsonify({'token': access_token}), 200
