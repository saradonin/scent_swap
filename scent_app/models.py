from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)


class Perfumer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Note(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Perfume(models.Model):
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    perfumer = models.ManyToManyField(Perfumer, null=True)
    category = models.ManyToManyField(Category)
    notes = models.ManyToManyField(Note, null=True)
    year = models.SmallIntegerField(null=True)


class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True)
    perfumes = models.ManyToManyField(Perfume, through='Collection')


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    looking_for = models.BooleanField(default=False)
    to_exchange = models.BooleanField(default=False)
