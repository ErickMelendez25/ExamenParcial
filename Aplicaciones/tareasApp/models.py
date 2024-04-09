from django.db import models

# Create your models here.

class Tarea(models.Model):
    nombre=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=80)
    fecha_fin=models.DateField()
    responsable=models.CharField(max_length=50)
    estado = models.CharField(max_length=20, default='En progreso')
    
    def __str__(self):
        texto="{0} ({1}) ({2}) ({3})"
        return texto.format(self.nombre,self.descripcion,self.fecha_fin,self.responsable)
    
    