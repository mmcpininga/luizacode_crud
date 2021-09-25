from django.shortcuts import render, redirect
from app.models import Empresas, Produtos
from app.forms import EmpresasForm, ProdutosForm

def home(request):
  return render(request, 'index.html')


#'View Menu empresa'
def menu_empresa(request):
  data={}
  search = request.GET.get('search')
  if search:
    data['empresas'] = Empresas.objects.filter(nomeemp_cmp__icontains = search)
  else:
    data['empresas'] = Empresas.objects.all()
  return render(request, 'mnuempresa.html', data)
  # data['empresas'] = Empresas.objects.all()
  # return render(request, 'mnuempresa.html',data)

#'View cadastro empresa'
def cadastro_empresa(request):
  data = {}
  form = EmpresasForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('menu_empresa')
  data['form'] = form
  return render(request, 'cdtempresa.html' , data)

def edit_empresas(request, pk):
  data = {}
  data['empresas'] = Empresas.objects.get(pk = pk)
  data['form'] = EmpresasForm(instance = data['empresas'])
  return render(request, 'cdtempresa.html', data)

def update_empresas(request, pk):
  data = {}
  data['empresas'] = Empresas.objects.get(pk = pk)
  form = EmpresasForm(request.POST or None, instance = data['empresas'])
  if form.is_valid():
    form.save()
    return redirect('menu_empresa')

def delete_empresas(request, pk):
  empresas = Empresas.objects.get(pk = pk)
  empresas.delete()
  return redirect('menu_empresa')


#'View Menu produto'
def menu_produto(request):
  data={}
  search = request.GET.get('search')
  if search:
    data['produtos'] = Produtos.objects.filter(nomepdt_cmp__icontains = search)
  else:
    data['produtos'] = Produtos.objects.all()
  return render(request, 'mnuproduto.html', data)

#'View cadastro produto'
def cadastro_produto(request):
  data = {}
  form = ProdutosForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('menu_produto')
  data['form'] = form
  return render(request, 'cdtproduto.html' , data)

def edit_produtos(request, pk):
  data = {}
  data['produtos'] = Produtos.objects.get(pk = pk)
  data['form'] = ProdutosForm(instance = data['produtos'])
  return render(request, 'cdtproduto.html', data)

def update_produtos(request, pk):
  data = {}
  data['produtos'] = Produtos.objects.get(pk = pk)
  form = ProdutosForm(request.POST or None, instance = data['produtos'])
  if form.is_valid():
    form.save()
    return redirect("menu_produto")
  
def delete_produtos(request, pk):
  produtos = Produtos.objects.get(pk = pk)
  produtos.delete()
  return redirect("menu_produto")
