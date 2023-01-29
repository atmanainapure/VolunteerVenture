from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    '''get_user_model() is a function in Django that returns the current user model being used in the project. In Django, a user model is a Python class that defines the fields and methods for storing and interacting with user data, such as username, email, and password. By default, Django uses its own built-in user model, called django.contrib.auth.models.User.
    The get_user_model() function is useful because it allows you to obtain the current user model without having to hardcode the import path or worry about whether a custom user model is being used.'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    #This code creates an ImageField in the models that stores profile images and sets the default image to 'blank-profile-picture.png' which is by default stored in the media file.
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    #Returns the username of the user associated with the object in the admin panel instead of showing object 1 and object 2.
    def __str__(self):
        return self.user.username

#Once we make a new model, make sure to migrate it and register it on the admin panel
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user