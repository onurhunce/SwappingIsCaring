from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    isbn = models.CharField(max_length=100, null=True)
    publisher = models.TextField(max_length=100, blank=False)
    categories = models.TextField(max_length=500, blank=False)
    language = models.TextField(max_length=30, blank=False)
    genre = models.TextField(max_length=200, blank=False)
    pub_year = models.DateTimeField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)


class Bookshelf(models.Model):
    id = models.IntegerField(primary_key = True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_status = models.TextField(max_length=20, blank=False)
    """
    Here we will have:
    1 -> request_sent
    2 -> request_accepted
    3 -> request_denied
    4 -> books_returned
    """
    current_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="current_reader"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    ff = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(max_length=520, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE, default="", related_name="library")


class ProfileSettings(models.Model):
    preferred_languages = models.TextField(max_length=500, blank=True)


class Review(models.Model):
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewee"
    )

    review_content = models.TextField(max_length=500, blank=False)


class Friend(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="relations_user_1"
    )
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="relations_user_2"
    )
