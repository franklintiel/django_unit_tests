from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    def __str__(self):
        return u'{0} - {1}'.format(self.user, self.published.date)    


class image(models.Model):
    image = models.ImageField(upload_to ='uploads/')
    post = models.ManyToManyField(Post, blank=True)

class comment(models.Model):
    comment = models.CharField(max_length=255)
    response = models.CharField(max_length=255)
    post = models.ManyToManyField(Post, blank=True)
class publication(models.Model):
    end_at = models.DateTimeField(auto_now_add=False)    
    post = models.ManyToManyField(Post, blank=True)