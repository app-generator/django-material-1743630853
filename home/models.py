# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Business(models.Model):

    #__Business_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    location = models.TextField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)

    #__Business_FIELDS__END

    class Meta:
        verbose_name        = _("Business")
        verbose_name_plural = _("Business")


class Businesstype(models.Model):

    #__Businesstype_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Businesstype_FIELDS__END

    class Meta:
        verbose_name        = _("Businesstype")
        verbose_name_plural = _("Businesstype")


class Revenuesource(models.Model):

    #__Revenuesource_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Revenuesource_FIELDS__END

    class Meta:
        verbose_name        = _("Revenuesource")
        verbose_name_plural = _("Revenuesource")


class Expensesource(models.Model):

    #__Expensesource_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Expensesource_FIELDS__END

    class Meta:
        verbose_name        = _("Expensesource")
        verbose_name_plural = _("Expensesource")



#__MODELS__END
