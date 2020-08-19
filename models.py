from django.db import models

# Create your models here.
class Program(models.Model):
    ##Fields
    name = models.CharField(max_length=200)
    offered = models.CharField(max_length=50)
    teacher = models.CharField(max_length=200)
    price = models.IntegerField()
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

class Instructor(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.CharField(max_length=500)

class QuestionAnswer(models.Model):
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=500)

class HomePageMessage(models.Model):
    text = models.CharField(max_length=1000)