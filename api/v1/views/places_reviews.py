#!/usr/bin/python3
""" Review view module for RESTful API """
from flask import Flask, request, jsonify, abort
from models import storage
from models.review import Review
from models.review import Review
from models.user import User
from . import app_views


@app_views.route('/cities/<review_id>/reviewss',
                 methods=['GET'], strict_slashes=False)
def get_reviews(city_id):
    """ Retrieves the list of all Review objects """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify([review.to_dict() for review in city.reviews])


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """ Retrieves a Review object """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """ Deletes a Review object """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    del review
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def create_review(place_id):
    """ Creates a Review object """
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, description="Missing name")
    if 'user_id' not in data:
        abort(400, description="Missing user_id")
    if not storage.get(Place, data['place_id']):
        abort(400)
    data['city_id'] = city_id
    new_review = Review(**data)
    storage.new(new_review)
    storage.save()
    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    """ Updates a Review object """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at', 'user_id']:
            setattr(review, key, value)
    storage.save()
    return jsonify(review.to_dict()), 200
