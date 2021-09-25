from django.db import models

# Create your models here.
class Empresas(models.Model):
  cnpj_cmp = models.CharField(max_length=150)
  nomeemp_cmp = models.CharField(max_length=100)
  enderecoemp_cmp = models.CharField(max_length=150)
  cep_cmp = models.IntegerField()
  emailemp_cmp = models.CharField(max_length=100)
  telemp_cmp = models.IntegerField()

class Produtos(models.Model):
  codigopdt_cmp = models.IntegerField()
  nomepdt_cmp = models.CharField(max_length=100)
  descpdt_cmp = models.CharField(max_length=100)
  nomeemppdt_cmp = models.CharField(max_length=100)
  precopdt_cmp = models.IntegerField()

