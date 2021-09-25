from django.forms import ModelForm
from app.models import Empresas, Produtos

class EmpresasForm(ModelForm):
  class Meta:
    model = Empresas
    fields = ['cnpj_cmp', 'nomeemp_cmp', 'enderecoemp_cmp' , 'cep_cmp', 'emailemp_cmp', 'telemp_cmp' ]

class ProdutosForm(ModelForm):
  class Meta:
    model = Produtos
    fields = ['codigopdt_cmp', 'nomepdt_cmp', 'descpdt_cmp', 'nomeemppdt_cmp', 'precopdt_cmp']