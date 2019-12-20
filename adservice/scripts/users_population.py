import django
django.setup()
from django.contrib.auth.models import User


user, create = User.objects.get_or_create(username="system.user")
user.is_active = True
user.first_name = "system"
user.last_name = "user"
user.is_staff = True
user.save()
print(user.id)
