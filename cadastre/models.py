from django.db import models 
from django.contrib import admin 

class Dclientes(models.Model): 
    nome=models.CharField(max_length=100) 
    cpf=models.CharField(max_length=50) 
    endereco=models.TextField() 
    tipo_CHOICES=( 
        ('F', 'Pessoa Física'), 
        ('P', 'Pessoa Jurídica'), 
    ) 
    tipo=models.CharField(max_length=1, choices=tipo_CHOICES) 

    def __str__(self):
        return f'{self.nome}'

class Dproduto(models.Model): 
    nomep=models.CharField(max_length=20) 
    valor_produto= models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.nomep}'

class Dpedidos(models.Model):
    status_CHOICES=(
        ('PP', 'pedido em processo'),
        ('PR', 'pedido realizado'),
        ('PE', 'pedido entregue'),
    )
    data_pedido=models.DateField()
    valor_pedido=models.FloatField()
    cliente=models.ForeignKey(Dclientes, on_delete=models.CASCADE)
    produto=models.ForeignKey(Dproduto, on_delete=models.CASCADE)
    status=models.CharField(max_length=2, choices=status_CHOICES)
    quantidade_pedido=models.IntegerField()