from adservice.utils.resource import Resource
from adservice.utils.response_utils import ok_response
from adservice.utils.error_handler import ErrorHandler
from flask import current_app as app
from adservice.service_api_handlers.ad_campaign import post_ad_handler
from adservice.utils.logger_utils import get_logger
from flask import request

logger = get_logger()


class AdCampaign(Resource):
    @ErrorHandler("POST ad creation", app)
    def post(self):
        request_body = request.get_json(force=True)
        logger.info("Received ad campaign creation request with data {}".format(request_body))
        resp = post_ad_handler.handle_request(request_body)
        return ok_response({"adCampaignId": resp})
