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
    """
    Represents a brand.

    Attributes:
        name (str): The name of the brand, limited to 64 characters. Must be unique.
        description (str): A description of the brand. Can be empty or null.
    """
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        """
        Return a string representation of the brand.
        """
        return self.name


class Perfumer(models.Model):
    """
    Represents a perfumer.

    Attributes:
        first_name (str): The first name of the perfumer, limited to 64 characters.
        last_name (str): The last name of the perfumer, limited to 64 characters.
    """
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    @property
    def name(self):
        """
        Get the full name of the perfumer.
        """
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        """
        Return a string representation of the perfumer.
        """
        return self.name


class Category(models.Model):
    """
    Represents a category for perfumes.

    Attributes:
        name (str): The name of the category, limited to 64 characters. Must be unique.
    """
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        """
        Return a string representation of the category.
        """
        return self.name


class Note(models.Model):
    """
    Represents a note used in perfumery.

    Attributes:
        name (str): The name of the note, limited to 64 characters. Must be unique.
    """
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        """
        Return a string representation of the note.
        """
        return self.name


class Perfume(models.Model):
    """
    Represents a perfume with various attributes.

    Attributes:
        name (str): The name of the perfume, limited to 64 characters.
        brand (Brand): The brand associated with the perfume.
        concentration (str): The concentration level of the perfume.
        perfumer (list of Perfumer): The perfumers associated with the perfume.
        category (list of Category): The categories associated with the perfume.
        top_notes (list of Note): The top notes of the perfume.
        middle_notes (list of Note): The middle notes of the perfume.
        base_notes (list of Note): The base notes of the perfume.
        year (int): The year of the perfume's release. Can be empty or null.
    """
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

    @property
    def full_name(self):
        """
        Get the full name of perfume.
        """
        return "{} {} ({})".format(self.brand, self.name, self.concentration)

    def __str__(self):
        """
        Return a string representation of perfume.
        """
        return self.full_name


# not sure about how the swap request model
class UserPerfume(models.Model):
    """
    Represents a perfume in user's collection with additional data.

    Attributes:
        user (User): The user owning the collection.
        perfume (Perfume): The perfume associated with the user.
        volume (int): The initial volume of the perfume owned by the user.
        status (str): The status of the user's perfume.
        to_exchange (bool): Indicates whether the perfume is available for exchange.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    volume = models.SmallIntegerField(null=True)
    status = models.CharField(null=True, max_length=255)
    to_exchange = models.BooleanField(default=False)

    @property
    def name(self):
        """
        Get the full name of perfume.
        """
        return "{} {} ({})".format(self.perfume.brand, self.perfume.name, self.perfume.concentration)

    def __str__(self):
        """
        Return a string representation of perfume.
        """
        return self.name


class SwapOffer(models.Model):
    """
    Represents an offer to swap perfumes between users.

    Attributes:
        offering_perfume (UserPerfume): The perfume being offered by the user initiating the swap.
        requested_perfume (Perfume): The perfume requested by the user initiating the swap.
        created_at (datetime): The date and time when the swap offer was created.
        is_accepted (bool): Indicates whether the swap offer has been accepted.
        is_completed (bool): Indicates whether the swap has been completed.
    """
    offering_perfume = models.ForeignKey(UserPerfume, related_name='offering_perfume', on_delete=models.CASCADE)
    requested_perfume = models.ForeignKey(Perfume, related_name='requested_perfume', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)


class Message(models.Model):
    """
    Represents a message between two users.

    Attributes:
        sender (User): The user who sent the message.
        receiver (User): The user who received the message.
        title (SwapOffer): The topic of the conversation.
        content (str): The content of the message.
        timestamp (datetime): The date and time when the message was sent.
        is_read (bool): Indicates whether the message has been read by the receiver.
    """
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    title = models.ForeignKey(SwapOffer, on_delete=models.SET("Deleted offer"))
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

