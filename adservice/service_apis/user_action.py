from adservice.utils.resource import Resource
from adservice.utils.response_utils import ok_response
from adservice.utils.error_handler import ErrorHandler
from flask import  current_app as app
from adservice.service_api_handlers.user_action import post_user_action, get_user_action
from adservice.utils.logger_utils import get_logger
from flask import request

logger = get_logger()


class UserAction(Resource):
    @ErrorHandler("POST user action creation", app)
    def post(self):
        request_body = request.get_json(force=True)
        logger.info("Received user action creation request with data {}".format(request_body))
        resp = post_user_action.handle_request(request_body)
        return ok_response({"userActionId": resp})

    @ErrorHandler("GET user action", app)
    def get(self):
        request_data = request.args.to_dict()
        logger.info("Received GET user action request {}".format(request_data))
        response = get_user_action.handle_request(request_data)
        return ok_response(response)
