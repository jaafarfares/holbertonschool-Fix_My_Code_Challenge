#!/usr/bin/python3
""" Index file that handles the sucses code
"""
from flask import jsonify

from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ the web server status code string
    """
    return  jsonify({"status": "OK"})
