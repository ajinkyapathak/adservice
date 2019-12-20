from adservice.db.ad_management.dao.user_action import create_user_action
from adservice.db.ad_management.dao.customer import get_customer
from adservice.db.ad_management.dao.ad_campaign import get_ad


def handle_request(request_body):
    customer_id = request_body["customerId"]
    ad_id = request_body["adCampaignId"]
    action = request_body["action"]
    customer = get_customer(customer_id)
    ad = get_ad(ad_id)
    res = create_user_action(customer, ad, action)
    return res
