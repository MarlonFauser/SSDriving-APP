from django.db import models


# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()


class Company(models.Model):
    name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14)
    phone = models.IntegerField()
    adress = models.CharField(max_length=200)


class Take(models.Model):
    date = models.DateTimeField('date published')
    adress = models.CharField(max_length=200)
    cod = models.IntegerField()


class Delivery(models.Model):
    date = models.DateTimeField('date published')
    adress = models.CharField(max_length=200)
    cod = models.IntegerField()


class Invoice(models.Model):
    cod = models.IntegerField()

