from .models import Presupuesto, Cliente
from django. forms import ModelForm
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido', 'correo', 'celular']


class PresupuestoForm(ModelForm):
    class Meta:
        model = Presupuesto
        fields = ['titulo','materiaPrima', 'manoDeObra', 'fecha', 'precio','estado','usuario']
            