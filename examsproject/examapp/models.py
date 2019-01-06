from django.db import models


# Create your models here.
class FirstQuestion(models.Model):
    username=models.CharField(max_length=50,default='sumanth')
    answer=models.IntegerField()
    marks=models.IntegerField(default=0)
class SecondQuestion(models.Model):
    username=models.CharField(max_length=50,default='sumanth')
    answer=models.IntegerField()
    marks=models.IntegerField(default=0)
class ThirdQuestion(models.Model):
    username=models.CharField(max_length=50,default='sumanth')
    answer=models.IntegerField()
    marks=models.IntegerField(default=0)
class FourthQuestion(models.Model):
    username=models.CharField(max_length=50,default='sumanth')
    answer=models.TextField()
    marks=models.IntegerField(default=0)
class FifthQuestion(models.Model):
    username=models.CharField(max_length=50,default='sumanth')
    answer=models.TextField()
    marks=models.IntegerField(default=0)
