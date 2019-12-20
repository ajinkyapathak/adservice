from adservice.db.ad_management.dao.ad_campaign import create_ad_campaign
from adservice.db.ad_management.models import AdCampaign
from adservice.db.ad_management.dao.category import get_category_by_name
from adservice.db.ad_management.dao.user import get_user


def handle_request(request_body):
    name = request_body["name"]
    description = request_body.get("description", "")
    picture_url = request_body["pictureUrl"]
    click_action = request_body["clickAction"]
    if click_action == "signup":
        ca = AdCampaign.SIGNUP
    else:
        ca = AdCampaign.REDIRECT
    redirection_url = request_body["redirectionUrl"]
    category_type = request_body.get("type")
    category = get_category_by_name(category_type)
    location = request_body["location"]
    target_min_age = request_body.get("minAge", 0)
    target_max_age = request_body.get("maxAge", 100)
    user_id = request_body["userId"]
    user = get_user(user_id)
    expiry_duration = request_body.get("expiryDuration", 365)
    ad = create_ad_campaign(name=name, picture_url=picture_url, description=description, created_by=user,
                            category=category, expiry_duration=expiry_duration, location=location,
                            min_age=target_min_age, max_age=target_max_age, click_action=ca,
                            redirection_url=redirection_url)
    return ad
