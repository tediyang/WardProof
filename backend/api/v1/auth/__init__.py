#!/usr/bin/python3
"""
  Blueprint for Authentication
"""
from flask import Blueprint

auth_parent = Blueprint('auth_parent', __name__, url_prefix='/auth/parent')
auth_school = Blueprint('auth_school', __name__, url_prefix='/auth/school')

from .authen import *