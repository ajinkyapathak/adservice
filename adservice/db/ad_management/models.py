from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(User):
    ad_preferences = models.ManyToManyField("Category")
    date_of_birth = models.DateField(null=True, blank=True)


class Category(models.Model):
    choices = (
        ("category1", "category1"),
        ("category2", "category2"),
        ("category3", "category3"),
        ("category4", "category4"),
        ("category5", "category5")
    )
    preference = models.CharField(max_length=64, choices=choices, db_index=True)
    is_archived = models.BooleanField(default=False)


class AdCampaign(models.Model):
    SIGNUP = "SIGNUP"
    REDIRECT = "REDIRECT"
    action_type_choices = (
        (SIGNUP, "SIGNUP"),
        (REDIRECT, "REDIRECT")
    )
    status_choices = (
        ("CREATED", "CREATED"),
        ("BLOCKED", "BLOCKED"),
        ("ARCHIVED", "ARCHIVED")
    )
    name = models.CharField(max_length=32)
    picture_url = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=50, db_index=True)
    min_age = models.IntegerField(default=0, db_index=True)
    max_age = models.IntegerField(default=100, db_index=True)
    status = models.CharField(max_length=32, choices=status_choices, default="CREATED", db_index=True)
    click_action = models.CharField(max_length=32, choices=action_type_choices)
    redirection_url = models.CharField(max_length=128)


class UserAction(models.Model):
    SIGNUP = "SIGNUP"
    VIEW = "VIEW"
    CLICK = "CLICK"
    action_type_choices = (
        (SIGNUP, "SIGNUP"),
        (VIEW, "VIEW"),
        (CLICK, "CLICK")
    )
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ad = models.ForeignKey(AdCampaign, on_delete=models.CASCADE)
    action = models.CharField(max_length=32, choices=action_type_choices)
    created_on = models.DateTimeField(auto_now_add=True)
