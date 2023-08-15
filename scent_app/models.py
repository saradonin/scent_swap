from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

CONCENTRATIONS = (
    ('Eau Fraiche', 'Eau Fraiche'),
    ('Eau de Cologne', 'Eau de Cologne'),
    ('Eau de Toilette', 'Eau de Toilette'),
    ('Eau de Parfum', 'Eau de Parfum'),
    ('Parfum', 'Parfum')
)


class Brand(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


class Note(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Perfume(models.Model):
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    concentration = models.CharField(max_length=64, choices=CONCENTRATIONS)
    perfumer = models.ManyToManyField(Perfumer)
    category = models.ManyToManyField(Category)
    top_notes = models.ManyToManyField(Note, related_name="perfumes_top_note")
    middle_notes = models.ManyToManyField(Note, related_name="perfumes_middle_note")
    base_notes = models.ManyToManyField(Note, related_name="perfumes_base_note")
    year = models.SmallIntegerField(null=True)

    class Meta:
        unique_together = ('name', 'brand', 'concentration')


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
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
