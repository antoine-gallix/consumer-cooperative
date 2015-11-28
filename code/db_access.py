"""contains the database access object
"""
import pymongo
from pdb import set_trace as bp

# get a connection to the database
client = pymongo.MongoClient()
# collection
users = client.coop.users


def get_user(user_id):
    """get a user from the database by its user id
    """
    return users.find_one({"_id": user_id})


def create_user(user):
    """create a user in the database
    """
    return users.insert_one(user).inserted_id
