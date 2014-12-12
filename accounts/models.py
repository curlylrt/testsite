# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an User Name.')
        if not email:
            raise ValueError('Users must have an email address.')
        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password):
        user = self.create_user(username,email,password)
        user.is_admin = True;
        user.is_staff = True;
        user.is_superuser = True    
        user.save(using=self._db)
        return user




class User(AbstractBaseUser,PermissionsMixin):
    alphanumeric = validators.RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allow.')
    username = models.CharField(unique=True, max_length=20,validators=[alphanumeric])
    email = models.EmailField(unique=True, verbose_name='email address',max_length=255)
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, null=False)
    is_admin = models.BooleanField(default=False, null=False)
    is_staff = models.BooleanField(default=False,null=False)

    #own field
    user_bio = models.TextField(verbose_name='自我介绍')
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = MyUserManager()

    def get_short_name(self):
        return self.first_name
    def get_username(self):
        return self.username
    def __unicode__(self):
        return self.username



