from adservice.db.ad_management.models import UserAction


def create_user_action(user, ad, action):
    user_action = UserAction()
    user_action.user = user
    user_action.ad = ad

    if action == "signup":
        user_action.action = user_action.SIGNUP
    elif action == "click":
        user_action.action = user_action.CLICK
    else:
        user_action.action = user_action.VIEW
    user_action.save()


def get_user_action_by_customer_id(customer):
    user_actions = UserAction.objects.filter(user=customer)
    return user_actions


def get_user_action_by_ad_id(ad):
    user_actions = UserAction.objects.filter(ad=ad)
    return user_actions
