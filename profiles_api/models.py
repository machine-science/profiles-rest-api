from django.db import models

# Follwoing libraries required to overrriding or customizing
# the default django user model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

# We have created custom user model and custom user model Manager
# we can configure django project to use this as the default user model
# instead of the one that is provided by the django

# Set the user model in settings.py file of the project
# Add --> AUTH_USER_MODEL = 'profiles_api.UserProfile'

class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, password = None):
        """Creat a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email) #normalize_email is inherited method
        user = self.model(email = email, name = name)

        # Notice: we are not passing password as an argument to self.model method
        # to create an user. We need to set password separately. Since the
        # password is incrypted. We need to make sure that password is converted to
        # Hash and never stored as plain text
        user.set_password(password)

        # standard procedure to save objects in django
        user.save(using = self._db)

        return user


    def create_superuser(self, email, name, password):
        """Create and save new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        # is_superuser is automatically created by PermissionsMixin
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for the users in the system"""
    # define various fields that we want to provide on our model
    # This means we want email column in the database table
    # And that column should be email field with max length of 255 and it
    # should be unique in the system
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    # Model Manager
    objects = UserProfileManager()

    # Here we are overrriding the default name option with email
    USERNAME_FIELD = 'email' # By default it is a required field
    REQUIRED_FIELDS = ['name']

    # following funstion is to give django the ability to retrive the fullname

    def get_full_name(self):
        """Get full name of user"""
        return self.name

    def get_short_name(self):
        """"To retrive short name of the user"""
        return self.name

    # String representation of our model
    def __str__(self):
        """Return string representationof our user"""
        return self.email
