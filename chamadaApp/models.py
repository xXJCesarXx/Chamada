from django.db import models
import PIL

# Create your models here.

class Telefone(models.Model):
    id_telefone = models.AutoField(primary_key=True)
    numero_telefone = models.CharField(max_length=200, null=False)
    tipo_telefone = models.CharField(max_length=200, null=False)


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=200, null=False)


class Plano(models.Model):
    id_plano = models.AutoField(primary_key=True)
    nome_plano = models.CharField(max_length=200, null=False)
    valor_plano = models.CharField(max_length=200, null=False)


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=200, blank=True, null=True)
    foto_cliente = models.ImageField(blank=True, null=True)
    cpf_cliente = models.CharField(max_length=200, null=False)
    email_cliente = models.CharField(max_length=200, null=True)
    id_telefone = models.ForeignKey(Telefone, models.DO_NOTHING, db_column='id_telefone', blank=True, null=False)
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=False)
    id_plano = models.ForeignKey(Plano, models.DO_NOTHING, db_column='id_plano', blank=True, null=False)