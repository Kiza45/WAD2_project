from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

class UserProfile(models.Model):
    picture = models.ImageField(upload_to='profile_images', blank=True)
    video = EmbedVideoField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=25, unique=True)
    #on_delete set to do nothing-we want a category to exist
    #even when user deletes the account
    creator = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=30, unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video = EmbedVideoField()
    date = models.DateField(auto_now=False, auto_now_add=True)
    views = models.IntegerField()

    def __str__(self):
        return self.title

class Comment(models):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    video_page = models.ForeignKey(Page, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    comment = models.CharField(max_length=350, unique=False)

    def __str__(self):
        return self.comment
