from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
# class Users(models.Model):
#     firstName = models.CharField(max_lenght=50)
#     lastName = models.CharField(max_lenght=50)
#     email =

# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_lenght=50)
#     last_name = models.CharField(max_lenght=50)
#     USERNAME_FIELD = ['email']
#     REQUIRED_FIELDS = ['email','first_name','last_name']