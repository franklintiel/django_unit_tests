from django.contrib import admin
from .models import *

admin.site.site_header = 'POST'
admin.site.site_title = 'POST'
admin.site.index_title = 'POST'

@admin.register(Publicar_Post)
class Publicar_Post_admin(admin.ModelAdmin):
    list_display = ('creador', 'comentarios', 'fecha_publicacion', 'correo', 'id')

