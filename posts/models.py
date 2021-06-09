from django.db import models


class Publicar_Post(models.Model):
    creador = models.CharField(max_length=50)
    comentarios = models.TextField(max_length=500)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    correo = models.EmailField(max_length=250)

    class Meta:
        verbose_name = 'Publicar_Post'
        verbose_name_plural = 'Publicar_Posts'
        ordering = ['id']

    def __str__(self):
        return self.creador

