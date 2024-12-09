"""
URL configuration for inventarioVeterinariaMarceloOsses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import include
from gestorProductos.views import categoriaData, productoData, categoriaRegistro, productoRegistro, categoriaEliminar, productoEliminar, productoEditar, categoriaEditar
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('verCategorias/', categoriaData, name='categoriaData'),
    path('verProductos/', productoData, name='productoData'),
    path('registrarCategoria/', categoriaRegistro, name='categoriaRegistro'),
    path('regproducto/', productoRegistro, name='productoRegistro'),
    path('eliminarcategoria/<int:id>/', categoriaEliminar, name='categoriaEliminar'),
    path('eliminarproducto/<int:id>/', productoEliminar, name='productoEliminar'),
    path('editarproducto/<int:id>/', productoEditar, name='productoEditar'),
    path('editarcategoria/<int:id>/', categoriaEditar, name='categoriaEditar'),
    path('usuarios/', include("gestorUser.urls")),
    path('accounts/',include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="index.html"),name="home"),
]


