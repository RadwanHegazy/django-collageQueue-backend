from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class Manager (BaseUserManager) : 
    def create_user(self,email,password,**other):
        user = self.model(**other)
        user.email = self.normalize_email(email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,**fields):
        fields['is_staff'] = True
        fields['is_superuser'] = True
        return self.create_user(**fields)


class User (AbstractUser) : 
    objects = Manager()
    
    first_name = None
    last_name = None
    username = None

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)
    full_name = models.CharField(max_length=225)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self) -> str:
        return self.full_name

