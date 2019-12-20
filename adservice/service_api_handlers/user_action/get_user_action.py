from adservice.db.ad_management.dao.user_action import get_user_action_by_customer_id, get_user_action_by_ad_id
from adservice.db.ad_management.dao.customer import get_customer
from adservice.db.ad_management.dao.ad_campaign import get_ad
from adservice.utils.utility_functions import get_str_datetime


def handle_request(request_body):
    request_type = request_body["requestType"]
    user_actions = None
    if request_type == "CUSTOMER":
        customer_id = request_body["customerId"]
        customer = get_customer(customer_id)
        user_actions = get_user_action_by_customer_id(customer)
    elif request_type == "AD":
        ad_id = request_body["adCampaignId"]
        ad = get_ad(ad_id)
        user_actions = get_user_action_by_ad_id(ad)

    user_actions_list = []
    for user_action in user_actions:
        user_actions_list.append(transform_response(user_action))
    return user_actions_list


def transform_response(user_action):
    user_action_dict = {
        "customer": user_action.user.id,
        "ad": user_action.ad.id,
        "action": user_action.action,
        "createdOn": get_str_datetime(user_action.created_on)
    }
    return user_action_dict