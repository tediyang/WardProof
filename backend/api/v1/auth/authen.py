#!/usr/bin/python3
"""
    Authentication for parent and school
"""
from flask import abort, jsonify, request
from ..auth import auth_parent
from ..auth import auth_school
from models.school import School
from models.parent import Parent
from models import storage
from flask_bcrypt import check_password_hash
from flask_jwt_extended import create_access_token
from flasgger.utils import swag_from
from sqlalchemy.exc import IntegrityError
from ..errors import UnauthorizedError
import datetime


# Signup
@auth_school.route('/signup', methods=['POST'], strict_slashes=False)
@swag_from('docs/authen/school_signup.yml', methods=['POST'])
def school_signup():
    """
    signup - function that handles signup for school.

    Returns:
        json: school id
    """
    try:
        body = request.get_json()

        new_school = School(**body)
        id = new_school.id
        storage.new(new_school)
        storage.save()

    except IntegrityError:
        abort(400, description='Email address already exists')
    except Exception as e:
        abort(400, description=f'An error occurred: {str(e)}')

    finally:
        storage.close()

    return jsonify({'id': id}), 201


@auth_parent.route('/signup', methods=['POST'], strict_slashes=False)
@swag_from('docs/authen/parent_signup.yml', methods=['POST'])
def parent_signup():
    """
    signup - function that handles signup for parent.

    Returns:
        json: parent id
    """
    try:
        body = request.get_json()

        new_parent = Parent(**body)
        id = new_parent.id
        storage.new(new_parent)
        storage.save()

    except IntegrityError:
        abort(400, description='Email address already exists')
    except Exception as e:
        abort(400, description=f'An error occurred: {str(e)}')

    finally:
        storage.close()

    return jsonify({'id': id}), 201


# Login
@auth_school.route('/login', methods=['POST'], strict_slashes=False)
@swag_from('docs/authen/school_login.yml', methods=['POST'])
def school_login():
    """
    login - function that handles login session for school.

    Returns:
        json: access token
    """
    try:
        body = request.get_json()
        school = storage.validate(School, {'email': body.get('email')})

        authorized = check_password_hash(school.password, body.get('password'))
        if not authorized:
            raise UnauthorizedError

        expires = datetime.timedelta(days=3)
        access_token = create_access_token(identity=school.id,
                                        expires_delta=expires)

    except AttributeError:
        abort(400, description='No account registered to this email')
    except UnauthorizedError:
        abort(401, description='Email or password invalid')
    except Exception as e:
        abort(400, description=f'An error occurred: {str(e)}')

    return jsonify({'token': access_token}), 200


@auth_parent.route('/login', methods=['POST'], strict_slashes=False)
@swag_from('docs/authen/parent_login.yml', methods=['POST'])
def parent_login():
    """
    login - function that handles login session for parent.

    Returns:
        json: access token
    """
    try:
        body = request.get_json()
        parent = storage.validate(Parent, {'email': body.get('email')})

        authorized = check_password_hash(parent.password, body.get('password'))
        if not authorized:
            raise UnauthorizedError

        expires = datetime.timedelta(days=3)
        access_token = create_access_token(identity=parent.id,
                                            expires_delta=expires)
    except AttributeError:
        abort(400, description='No account registered to this email')
    except UnauthorizedError:
        abort(401, description='Email or password invalid')
    except Exception as e:
        abort(400, description=f'An error occurred: {str(e)}')

    return jsonify({'token': access_token}), 200
