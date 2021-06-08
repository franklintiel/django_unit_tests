from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=True)
    # image...

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return u'{0} - ({1})'.format(self.user, self.published_date)

