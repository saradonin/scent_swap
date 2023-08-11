from django.db import models


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
    CONCENTRATIONS = (
        ('Eau Fraiche', 'Eau Fraiche'),
        ('Eau de Cologne', 'Eau de Cologne'),
        ('Eau de Toilette', 'Eau de Toilette'),
        ('Eau de Parfum', 'Eau de Parfum'),
        ('Parfum', 'Parfum')
    )
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    concentration = models.CharField(max_length=32, choices=CONCENTRATIONS)
    perfumer = models.ManyToManyField(Perfumer, null=True)
    category = models.ManyToManyField(Category)
    notes = models.ManyToManyField(Note, null=True)
    year = models.SmallIntegerField(null=True)

    @property
    def name(self):
        return "{} {}".format(self.brand.name, self.name)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    perfumes = models.ManyToManyField(Perfume, through='UserPerfume')


# not sure about how the swap request model
class UserPerfume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    volume = models.SmallIntegerField()
    status = models.CharField(max_length=255)
    to_exchange = models.BooleanField(default=False)


class SwapOffer(models.Model):
    requested_perfume = models.ForeignKey(UserPerfume, related_name='requested_perfume', on_delete=models.CASCADE)
    offering_perfume = models.ForeignKey(UserPerfume, related_name='offering_perfume', on_delete=models.CASCADE)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
