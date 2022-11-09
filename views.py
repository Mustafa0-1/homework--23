from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from bulider import build_query
from models import BatchRequestParams

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        params = BatchRequestParams().load(request.json)
    except ValidationError as e:
        return e.messages, 400

    res = None
    for query in params["queries"]:
        res = build_query(
            cmd=query["cmd"],
            param=query['value'],
            data=res
        )

    return jsonify(res)