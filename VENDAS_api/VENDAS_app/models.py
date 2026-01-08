from django.db import models
from decimal import Decimal


# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_criacao = models.DateTimeField(auto_now_add=True)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.PROTECT)
    produto = models.ForeignKey('Produto', on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    data_venda = models.DateTimeField(auto_now_add=True)
    valortotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        # calcula valor total automaticamente
        self.valortotal = self.produto.preco * Decimal(self.quantidade)
        super().save(*args, **kwargs)

        def __str__(self):
            return f"Venda #{self.id} - {self.cliente.nome}"


class Itenvenda(models.Model):
    venda = models.ForeignKey('Venda', on_delete=models.PROTECT)
    produto = models.ForeignKey('Produto', on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.preco_unitario * Decimal(self.quantidade)
        super().save(*args, **kwargs)