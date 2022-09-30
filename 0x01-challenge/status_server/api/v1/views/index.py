#!/usr/bin/python3
""" the file that handles the sucses return
"""
from flask import jsonify

from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ show the web server status
    """
    return  jsonify({"status": "OK"})
