from django.contrib import admin
from .models import Presupuesto, Cliente
# Register your models here.
   #modeladmin/ORM 
class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ['titulo','materiaPrima','manoDeObra','fecha','precio','estado']
    search_fields = ['titulo','materiaPrima','manoDeObra','fecha','precio','estado']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','correo', 'celular']

admin.site.register(Presupuesto, PresupuestoAdmin)
admin.site.register(Cliente, ClienteAdmin)
# Register your models here.
# Register your models here.
