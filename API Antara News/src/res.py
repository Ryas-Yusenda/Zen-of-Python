from flask import make_response, jsonify


def success(values):
    res = {
        "post": values
    }
    return make_response(jsonify(res), 200)
