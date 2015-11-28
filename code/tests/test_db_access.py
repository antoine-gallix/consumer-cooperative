"""tests funcionalities in the db_access module
"""
import sys
import os.path
here_folder = os.path.dirname(__file__)
sys.path.insert(0, here_folder + '/..')
import db_access
from pdb import set_trace as bp


def test_create_user():
    """create a user with only one name, assert something is returned
    """
    user = {"name": "jean-louis"}
    inserted = db_access.create_user(user)
    assert inserted


def test_get_user():
    """create and then get a user
    """
    user = {"name": "jean-louis"}
    inserted = db_access.create_user(user)
    assert inserted
    read = db_access.get_user(inserted)
    assert read


def test_delete_user():
    """create and then get a user
    """
    user = {"name": "jean-louis"}
    inserted = db_access.create_user(user)
    assert inserted
    read = db_access.get_user(inserted)
    assert read
    db_access.delete_user(inserted)
    read = db_access.get_user(inserted)
    assert not read


if __name__ == '__main__':
    test_delete_user()
