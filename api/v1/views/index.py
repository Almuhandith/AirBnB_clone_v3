#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'])
def status():
    """ Returns JSON """
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'])
def get_stats():
    """ Returns the number of each instance type """
    stats = {}
    stats['amenities'] = storage.count('Amenity')
    stats['cities'] = storage.count('City')
    stats['places'] = storage.count('Place')
    stats['reviews'] = storage.count('Review')
    stats['states'] = storage.count('State')
    stats['users'] = storage.count('User')
    return jsonify(stats)
