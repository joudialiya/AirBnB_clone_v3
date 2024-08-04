#!/usr/bin/python3
"""blueprint module"""

from api.v1.views import app_view


@app_view.route("/status", strict_slashes=False)
def status_handler():
    """returns status"""
    return {
        "status": "ok"
    }
