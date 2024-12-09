from django.contrib import admin
from gestorProductos.models import Categoria, Producto

# Register your models here.
#clase categoría
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

#clase producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'categoria_id', 'user_id')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)