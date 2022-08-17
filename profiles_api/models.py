from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

""" Above are the 2 classes imported if we need to override the default
User model.
"""

# Create your models here.

class UserProfileManager(BaseUserManager):

    def create_user(self,email,name,password=None):

        """Create a New user profile"""
        if not email:
            raise ValueError("Email Field cant be empty")
        email=self.normalize_email(email) #Tomake sure the domain.com to be lowercase. bbefore @ is case sensitive. post that is all lowercase we are mannually doinng that to get rid of errors
        user=self.model(email=email,name=name)
        user.set_password(password) #by default django hashes n stores the encrypted password
        user.save(using=self._db) #default django DB. Need to change as per our needs

        return user

    def create_superuser(self,email,name,password):
        """create a new admin with  the given details"""
        user=self.create_user(email,name,password)
        user.is_staff=True
        user.is_superuser=True #Django sepcific field to set this user as Admin
        user.save(using=self._db)

        return user




class UserModel(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the System"""

    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True) #By default making account active.
    is_staff=models.BooleanField(default=False)  #To set Admin Field.

    objects=UserProfileManager() #To Manage user creation we create the class
    USERNAME_FIELD='email'  #Overrride the default username to email
    REQUIRED_FIELDS=['name']#Mandatory columns to be entered is name


    """To return full nn short names ifany. By default returning name itself"""
    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        """Return String representationn of user"""
        return self.email
