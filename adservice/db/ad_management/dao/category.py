from adservice.db.ad_management.models import Category


def get_category_list(categories):
    return Category.objects.filter(preference__in=categories)


def get_category_by_name(name):
    return Category.objects.get(preference=name)
