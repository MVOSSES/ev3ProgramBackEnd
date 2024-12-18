from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#clase categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    #falta metodo str
    def __str__(self):
        return self.nombre
#clase producto
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

