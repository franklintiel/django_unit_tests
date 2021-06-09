from django.db import models
from django.contrib.auth.models import User
import datetime

class Created_Update_Class(models.Model):
    created_at = models.DateField(auto_now_add = True, editable= False)
    update_at = models.DateField(auto_now = True , editable= True)

    class Meta:
        abstract = True

class Posts(Created_Update_Class):
    #id = models.IntegerField(auto_created = True,primary_key = True, editable= False)
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=300)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Publication(Created_Update_Class):
    #id = models.IntegerField(auto_created=True, primary_key=True,editable= False)
    start_at = models.DateField(null=False, editable= True)
    end_at = models.DateField(null=False, editable= True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(Created_Update_Class):
    #id = models.IntegerField(auto_created=True, primary_key=True, editable= False)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    response = models.CharField(max_length=150)

class Image(Created_Update_Class):
    #id = models.IntegerField(auto_created=True, primary_key=True, editable= False)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)