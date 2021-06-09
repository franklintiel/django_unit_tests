from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creator')
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-id']

