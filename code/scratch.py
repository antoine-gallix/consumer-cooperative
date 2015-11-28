"""tests funcionalities in the db_access module
"""
import sys
import os.path
here_folder = os.path.dirname(__file__)
sys.path.insert(0, here_folder + '/..')
import db_access


def test_create_user():
    user = {"name": "jean-louis"}
    inserted = db_access.create_user(user)
    print inserted

test_create_user()
