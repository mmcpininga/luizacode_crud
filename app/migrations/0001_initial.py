# Generated by Django 3.2.7 on 2021-09-22 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj_cmp', models.CharField(max_length=150)),
                ('nomeemp_cmp', models.CharField(max_length=100)),
                ('enderecoemp_cmp', models.CharField(max_length=150)),
                ('cep_cmp', models.IntegerField()),
                ('emailemp_cmp', models.CharField(max_length=100)),
                ('telemp_cmp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigopdt_cmp', models.IntegerField()),
                ('nomepdt_cmp', models.CharField(max_length=100)),
                ('descpdt_cmp', models.CharField(max_length=100)),
            ],
        ),
    ]