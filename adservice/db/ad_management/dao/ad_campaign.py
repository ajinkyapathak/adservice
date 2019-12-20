from adservice.db.ad_management.models import AdCampaign, Category
from datetime import datetime, timedelta


def create_ad_campaign(name, picture_url, description, created_by, category, expiry_duration, location, min_age, max_age, click_action, redirection_url):
    campaign = AdCampaign()
    campaign.name = name
    campaign.picture_url = picture_url
    campaign.description = description
    campaign.expiry_date = datetime.now() + timedelta(days=expiry_duration)
    campaign.click_action = click_action
    campaign.created_by = created_by
    campaign.type = category
    campaign.location = location
    campaign.min_age = min_age
    campaign.max_age = max_age
    campaign.redirection_url = redirection_url

    campaign.save()
    return campaign.id


def get_matching_ads(preference_categories, age, location):
    if preference_categories:
        ads = AdCampaign.objects.filter(type__in=preference_categories, min_age__lte=age, max_age__gte=age, location=location, status="CREATED", expiry_date__gte=datetime.now())
    else:
        ads = AdCampaign.objects.filter(min_age__lte=age, max_age__gte=age,
                                        location=location, status="CREATED", expiry_date__gte=datetime.now())

    return ads


def get_ad(ad_id):
    return AdCampaign.objects.get(id=ad_id)
