"""tests funcionalities in the db_access module
"""
import sys
import os.path
import pytest
here_folder = os.path.dirname(__file__)
sys.path.insert(0, here_folder + '/..')
import db_access
from db_access import DB_Exception
from pprint import pprint
from pdb import set_trace as bp


@pytest.fixture(autouse=True)
def clear_users():
    """deletes all users
    """
    db_access.delete_all_users()


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
    """create and then deletes a user
    """
    user = {"name": "jean-louis"}
    inserted = db_access.create_user(user)
    assert inserted
    read = db_access.get_user(inserted)
    assert read
    db_access.delete_user(inserted)
    read = db_access.get_user(inserted)
    assert not read


def test_delete_error():
    """try to delete a non existing document
    """
    with pytest.raises(DB_Exception):
        db_access.delete_user("mille")


def test_delete_all():
    """insert two users and delete both at once
    """
    user1 = {"name": "jean-louis"}
    user2 = {"name": "jean-michel"}
    db_access.create_user(user1)
    db_access.create_user(user2)
    users = db_access.get_all_users()
    assert len(users) > 0
    db_access.delete_all_users()
    users = db_access.get_all_users()
    print "users after"


def test_get_all_users():
    """insert two users and get the list of them
    """
    user1 = {"name": "jean-louis"}
    user2 = {"name": "jean-michel"}
    db_access.create_user(user1)
    db_access.create_user(user2)
    users = db_access.get_all_users()
    assert len(users) == 2

if __name__ == '__main__':
    test_get_all_users()
