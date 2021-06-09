from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "creator", "update_at","created_at" ]

admin.site.register(Posts, UserAdmin)
admin.site.register(Publication)
admin.site.register(Comment)
admin.site.register(Image)
# Register your models here.
