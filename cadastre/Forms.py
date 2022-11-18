from django import forms
from .models import Dclientes, Dproduto, Dpedidos

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Dclientes
        fields=['nome', 'cpf', 'endereco', 'tipo']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Dproduto
        fields=['nomep', 'valor_produto']

class PedidoForm(forms.ModelForm):
    class Meta:
            model = Dpedidos
            fields=['valor_pedido', 'cliente', 'produto', 'status', 'quantidade_pedido']