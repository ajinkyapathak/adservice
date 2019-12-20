from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from os.path import dirname, abspath
import django

django.setup()

from adservice.utils.logger_utils import get_logger
from adservice.service_apis.customer import Customer
from adservice.service_apis.ad_campaign import AdCampaign
from adservice.service_apis.user_action import UserAction

logger = get_logger()
app = Flask("adservice")
CORS(app)

app.root_dir = dirname(dirname(abspath(__file__)))
api = Api(app, prefix='/adservice/')

logger.info("Setting up Resources")

api.add_resource(Customer, "customer/")
api.add_resource(AdCampaign, "adcampaign/")
api.add_resource(UserAction, "useraction/")

if __name__ == '__main__':
    app.logger.info("app {} started..".format(app))
    app.run(host="0.0.0.0", debug=True, port=7000)
