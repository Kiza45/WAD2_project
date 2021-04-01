from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    follows = models.ManyToManyField('self', related_name='follower', symmetrical=False)

    def count_followers(self):
        return self.follows.count()

    def count_following(self):
        return UserProfile.object.filter(follows=self).count()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=25, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos')
    thumbnail = models.ImageField(upload_to='thumbnails', blank=False)
    date = models.DateField(auto_now=False, auto_now_add=True)
    views = models.IntegerField(default=0)

    like_react = models.IntegerField(default=0)
    dislike_react = models.IntegerField(default=0)
    haha_react = models.IntegerField(default=0)
    love_react = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    video_page = models.ForeignKey(Page, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    comment = models.CharField(max_length=350, unique=False)

    def __str__(self):
        return self.comment
