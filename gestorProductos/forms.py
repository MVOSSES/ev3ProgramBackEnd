from django import forms
from gestorProductos.models import Categoria, Producto

#formulario editar categoría
class CategoriaForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()  

#formulario insertar categoría
class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField()
    descripcion = forms.CharField()  

    class Meta:
        model = Categoria
        fields = '__all__'

#formulario editar producto
class ProductoForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    categoria_id = forms.ModelChoiceField(queryset=Categoria.objects.all())

#formulario insertar producto
#El campos categoria se selecciona entre categorias previamente creadas
#el mapo creador se llena automaticamente al crear el producto con el id del usuario como clave foranea
class ProductoForm(forms.ModelForm):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    categoria_id = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        label="Categoría",
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    class Meta:
        model = Producto
        fields = '__all__'