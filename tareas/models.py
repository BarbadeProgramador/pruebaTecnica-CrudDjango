from django.db import models

class Tarea(models.Model):
    PRIORIDAD_CHOICES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField()
    prioridad = models.CharField(
        max_length=5,
        choices=PRIORIDAD_CHOICES,
        default='Media'
    )

    class Meta:
        ordering = ['-fecha_creacion']