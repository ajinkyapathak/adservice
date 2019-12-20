from django.contrib.auth.models import User


def get_user(user_id):
    return User.objects.get(id=user_id)


def create_user(first_name, last_name):
    user = User()
    user.is_active = True
    user.first_name = first_name
    user.last_name = last_name
    user.username = first_name + "." + last_name
    user.is_staff = True
    user.save()
    return user.id
