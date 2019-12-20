from adservice.utils.resource import Resource
from adservice.utils.response_utils import ok_response
from adservice.utils.error_handler import ErrorHandler
from flask import current_app as app
from adservice.service_api_handlers.customer import post_customer_handler, get_matching_ads_for_customer
from adservice.utils.logger_utils import get_logger
from flask import request

logger = get_logger()


class Customer(Resource):
    @ErrorHandler("POST customer creation", app)
    def post(self):
        request_body = request.get_json(force=True)
        logger.info("Received customer creation request with data {}".format(request_body))
        resp = post_customer_handler.handle_request(request_body)
        return ok_response({"customerId": resp})

    @ErrorHandler("GET customer matching ads", app)
    def get(self):
        request_data = request.args.to_dict()
        response = get_matching_ads_for_customer.handle_request(request_data)
        return ok_response(response)
