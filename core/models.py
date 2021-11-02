from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=128)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return self.nome
        #return f'{self.nome} {self.estoque}'


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=128)
    sobrenome = models.CharField('Sobrenome', max_length=128)
    email = models.EmailField('e-mail', max_length=128)

    def __str__(self):
        return self.nome
        #return f'{self.nome} {self.sobrenome}'


class Teste1(models.Model):
    Test1 = models.CharField('Teste', max_length=128)
    TipoCharField = models.CharField('TipoCharField', max_length=128)
    TipoEmail = models.EmailField('TipoEmail', max_length=128)
    TipoTextField = models.TextField('TipoTextField', max_length=512)

    def __str__(self):
        return self.Test1


class Teste2(models.Model):
    Test2 = models.CharField('Test2', max_length=128)
    TipoIntegerField = models.IntegerField('TipoIntegerField')
    TipoDecimalField = models.DecimalField('TipoDecimalField', max_digits=8, decimal_places=2)
    TipoFloatField = models.FloatField('TipoFloatField', max_length=8)
    TipoBooleanFieldTrue = models.BooleanField('TipoBooleanFieldTrue', default=True)
    TipoBooleanFieldFalse = models.BooleanField('TipoBooleanFieldFalse', default=False)

    def __str__(self):
        return self.Test2
