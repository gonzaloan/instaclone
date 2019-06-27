""" Posts models """

# Django
from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

class Post(models.Model):
    """Post model."""

    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='posts/photos')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # Hay que referenciar el post con nuestro user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        """Return title and username"""
        return '{} by @{}'.format(self.title, self.user.username)

