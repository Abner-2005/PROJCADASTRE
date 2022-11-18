from django.shortcuts import render, redirect
from .models import Dclientes, Dpedidos, Dproduto
from .Forms import ClienteForm, PedidoForm, ProdutoForm

# Funções da tabela Dclientes:
def listar_clientes(request):
    clientes=Dclientes.objects.all()
    return render(request, 'listar_clientes.html', {'clientes':clientes})

def listar_clientes_id(request, id):
    cliente = Dclientes.objects.get(id=id)
    return render(request, 'listar_cliente.html',{'cliente' : cliente})

def inserir_clientes(request):
    if request.method== 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request,'inserir_clientes.html', {'form':form})
            
def editar_cliente(request, id):
    cliente=Dclientes.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance =cliente)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request,'inserir_clientes.html', {'form':form})

def remover_cliente(request, id):
    cliente=Dclientes.objects.get(id=id)
    if request.method =='POST':
        cliente.delete()
        return redirect ('listar_clientes')
    return render(request, 'remover_clientes.html', {'cliente':cliente})

#Funções da tabela Dproduto

def listar_produtos(request):
    produtos=Dproduto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos':produtos})

def listar_produto_id(request, id):
    produto = Dproduto.objects.get(id=id)
    return render(request, 'listar_produto.html',{'produto' : produto})

def inserir_produto(request):
    if request.method== 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produto')
    else:
        form = ProdutoForm()
    return render(request,'inserir_produtos.html', {'form':form})
            
def editar_produto(request, id):
    produto=Dproduto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance =produto)
    if form.is_valid():
        form.save()
        return redirect('listar_produtos')
    return render(request,'inserir_produtos.html', {'form':form})

def remover_produto(request, id):
    produto=Dproduto.objects.get(id=id)
    if request.method =='POST':
        produto.delete()
        return redirect ('listar_produtos')
    return render(request, 'remover_produtos.html', {'produto':produto})

#Pedidos

def listar_pedidos_id(request, id):
    pedidos = pedidos.objects.get(id=id)
    return render(request, 'listar_pedidos.html',{'pedidos' : pedidos})

def inserir_pedidos(request):
    if request.method== 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = ProdutoForm()
    return render(request,'inserir_pedidos.html', {'form':form})
            
def editar_pedidos(request, id):
    pedidos=pedidos.objects.get(id=id)
    form = pedidos(request.POST or None, instance =pedidos)
    if form.is_valid():
        form.save()
        return redirect('listar_pedidos')
    return render(request,'inserir_pedidos.html', {'form':form})

def remover_pedidos(request, id):
    pedidos=pedidos.objects.get(id=id)
    if request.method =='POST':
       pedidos.delete()
    return redirect ('listar_pedidos')
    return render(request, 'remover_pedidos.html', {'pedidos':pedidos})

