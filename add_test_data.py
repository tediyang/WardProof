#!/usr/bin/python3
""" Add data into the base for testing """
from sqlalchemy import create_engine
from dotenv import find_dotenv, load_dotenv
from os import getenv


path = find_dotenv('wardproof.env')
load_dotenv(path)

user = getenv('WARDPROOF_USER')
pwd = getenv('WARDPROOF_PWD')
host = getenv('WARDPROOF_HOST')
db = getenv('WARDPROOF_DB')

engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}',
                       format(user, pwd, host, db))

with open('setup_mysql_db_test.sql', 'r') as sql_file:
    query = sql_file.read()
    engine.execute(query)
