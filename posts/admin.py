from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    post=('created_at', 'update_at', 'title', 'content', 'image', 'creator', 'comment', 'response', 'end_at')