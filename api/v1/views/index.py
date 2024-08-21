#!/usr/bin/python3
""" module containing the status route """
from . import app_views
from flask import jsonify
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.user import User


@app_views.route("/status")
def status():
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def stats():
    """ handler for the stats view """
    return jsonify({"amenities": storage.count(cls=Amenity),
                    "cities": storage.count(cls=City),
                    "places": storage.count(cls=Place),
                    "reviews": storage.count(cls=Review),
                    "states": storage.count(cls=State),
                    "users": storage.count(cls=User)})
