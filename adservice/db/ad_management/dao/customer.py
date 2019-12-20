from adservice.db.ad_management.models import Customer, Category
from datetime import datetime, timedelta


def create_customer(first_name, last_name, category_preferences, date_of_birth):
    customer = Customer()
    customer.username = first_name + "." + last_name
    customer.is_active = True
    customer.first_name = first_name
    customer.last_name = last_name
    customer.date_of_birth = date_of_birth
    customer.date_joined = datetime.now()
    customer.last_login = datetime.now()
    customer.save()
    customer.ad_preferences.add(*category_preferences)

    return customer.id


def get_customer(customer_id):
    return Customer.objects.get(id=customer_id)


def get_customer_preferences(customer_id):
    customer = Customer.objects.get(id=customer_id)
    return customer.ad_preferences.all()


def get_customer_age(customer_id):
    current_date = datetime.now()
    customer = get_customer(customer_id)
    if customer.date_of_birth:
        dob_obj = datetime(day=customer.date_of_birth.day, month=customer.date_of_birth.month, year=customer.date_of_birth.year)
        diff = current_date - dob_obj
        return int(diff.days/365)
    else:
        return 0
