# from django.db import models
from django.contrib.auth.models import User
from djongo import models

class Archivo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    NOMBRE = models.CharField(max_length=255)  # Nombre del archivo
    archivo = models.FileField(upload_to='archivos/')  # Ruta de subida
    FECHA_SUBIDA = models.DateTimeField(auto_now_add=True)  # Fecha de subida
    plagio_percentage = models.FloatField(default=0.0)  # Porcentaje de plagio (opcional)

    class Meta:
        db_table = "archivos"  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.nombre} ({self.usuario.username})"


