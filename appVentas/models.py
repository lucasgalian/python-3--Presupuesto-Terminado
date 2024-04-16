from django.db import models
from django.utils import timezone

class Cliente(models.Model):
     nombre = models.CharField(max_length=20)
     apellido = models.CharField(max_length=30, null= True)
     correo = models.EmailField()
     celular= models.IntegerField()
 
     def __str__(self):
          return self.nombre
class Presupuesto(models.Model):
       titulo = models.CharField(max_length=50 )
       materiaPrima = models.CharField(max_length= 50)
       manoDeObra = models.IntegerField()
       fecha = models.DateTimeField(blank=True, null=True, default=timezone.now)
       precio = models.FloatField(verbose_name='PrecioTotal')
       estado=models.BooleanField(default=False, verbose_name='Confirmar Presupuesto')
       usuario= models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
       
       def __str__(self):
        return self.titulo 
       
       def publico(self):
             self.fecha = timezone.now()
             self.save()

# Create your models here.
