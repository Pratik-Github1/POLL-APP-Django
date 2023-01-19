from django.db import models
from django.contrib.auth.models import  UserManager , User

# class User(models.Model):
#     # id = models.AutoField(primary_key=True , null=False)
#     name = models.CharField(max_length=110)
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=50)
#     phone = models.IntegerField()
#     password = models.CharField(max_length=50)
#     password2 = models.CharField(max_length=50)
#     phone = models.IntegerField()
#     objects =  UserManager()


class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100)
    option_four = models.CharField(max_length=100)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)
    
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count
    
    
    
