import django
django.setup()
from adservice.db.ad_management.models import Category

category_list = ["category1", "category2", "category3", "category4", "category5"]

for c in category_list:
    print(Category.objects.get_or_create(preference=c))
