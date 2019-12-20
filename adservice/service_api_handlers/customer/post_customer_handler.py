from adservice.db.ad_management.dao.customer import create_customer
from adservice.db.ad_management.dao.category import get_category_list
from adservice.utils.utility_functions import get_datetime_object_from_string


def handle_request(request_data):
    first_name = request_data["firstName"]
    last_name = request_data["lastName"]
    date_of_birth = get_datetime_object_from_string(request_data["dateOfBirth"])
    preference_list = request_data.get("preferences")
    category_list = []
    if preference_list:
        category_list = get_category_list(preference_list)
    resp = create_customer(first_name, last_name, category_list, date_of_birth)
    return resp
