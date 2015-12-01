"""contains the database access object
"""
import pymongo
from pdb import set_trace as bp

# get a connection to the database
client = pymongo.MongoClient()
# collection
users = client.coop.users


class DB_Exception(Exception):
    """Error within this module
    """
    pass


def get_user(user_id):
    """gets a user from the database by its user id
    """
    return users.find_one({"_id": user_id})


def create_user(user):
    """creates a user in the database
    """
    return users.insert_one(user).inserted_id


def delete_user(user_id):
    """deletes a user from the database by its user id. raise DB_Exception if the deletion havent been performed
    """
    result = users.delete_one({"_id": user_id})
    if result.deleted_count == 0:
        raise DB_Exception
