from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('create_cli/', views.create_cli, name ="create_cli"),
    path('create_pres/', views.create_pres, name ="create_pres"),
    path('listaPres/', views.listaPres, name="listaPres"),
    path('clientes/', views.clientes, name="clientes"),
    path('updateCli/<int:id>/', views.updateCli, name="updateCli"),
    path('updatePres/<int:id>/', views.updatePres, name="updatePres"),
    path('detalle/<int:id>/', views.detalle, name='detalle'),
    path('deletePres/<int:id>/', views.deletePres, name='deletePres'),
    path('deleteCli/<int:id>/', views.deleteCli, name='deleteCli'),
    ]