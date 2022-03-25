from tkinter import CASCADE
from django.db import models
import uuid

from matplotlib.pyplot import cla
# Create your models here.


class Burger(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class Salad(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class MainDish(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    salads = models.ManyToManyField(Salad)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


# We will create an intermediary table
class MainDishTag(models.Model):
    maindish = models.ForeignKey(MainDish, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)


class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.name
