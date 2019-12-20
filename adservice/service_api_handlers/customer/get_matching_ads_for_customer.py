from adservice.db.ad_management.dao.ad_campaign import get_matching_ads
from adservice.db.ad_management.dao.customer import get_customer_preferences, get_customer_age


def handle_request(request_body):
    customer_id = request_body["customerId"]
    customer_preferences = get_customer_preferences(customer_id)
    age = get_customer_age(customer_id)
    location = request_body["location"]
    ads = get_matching_ads(preference_categories=customer_preferences, age=age, location=location)
    ad_response_list = []
    for ad in ads:
        ad_response_list.append(transform_response(ad))
    return ad_response_list


def transform_response(ad):
    ad_response = {
        "name": ad.name,
        "description": ad.description,
        "pictureUrl": ad.picture_url,
        "clickAction": ad.click_action,
        "redirectionUrl": ad.redirection_url,
        "location": ad.location,
        "type": ad.type.preference
    }
    return ad_response
