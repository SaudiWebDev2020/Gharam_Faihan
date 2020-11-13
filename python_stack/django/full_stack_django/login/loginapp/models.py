import re
import bcrypt
from django.db import models
from datetime import date

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User_Manager(models.Manager):
    def validate(self, postData):
        errors = {}
        print(postData)


    def login_validation(self, postData):
        errors = {}
        # print(postData)
        # errors['login'] = 'Error'

        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_format'] = "Invalid email address!"

        # Try if it is regestered or not =).
        try:
            user_temp = User.objects.get(email=postData['email'].lower())
        except User.DoesNotExist:
            user_temp = None

        if user_temp == None:
            errors['email_not_found'] = "The email is not regestered"

        return errors

    def basic_validator(self ,value):
        errors = {}
        if len(value['firstname'])<2:
            errors["firstname"] = "First Name should be at least 2 characters"
        if len(value['lastname'])<2:
            errors["lastname"] = "Last Name should be at least 2 characters"
        if len(value['email'])<10:
            errors['email']='Email not valid'
        if len(value['password'])<8:
            errors['password'] = 'Password shold be at least 8 characters'
        if len(value['password']) != len(value['confirm-pass']):
            errors['password'] = 'Password does not match '
        return errors


class User(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=User_Manager()
    def __str__(self):
        return f"<User object: First Name: {self.firstname}  Last Name : {self.lastname} Email: {self.email} password: {self.password} ({self.id})>\n"
