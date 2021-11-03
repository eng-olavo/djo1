from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=128)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return self.nome
        #return f'{self.nome} {self.estoque}'


class Cliente(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('L', 'LGBTQIA+')
    )

    ESTADO_CIVIL_CHOICES = (
        ('S', 'Solteiro'),
        ('C', 'Casado'),
        ('U', 'União Estável'),
        ('D', 'Divorciado'),
        ('V', 'Viúvo'),
    )

    nome = models.CharField('Nome', max_length=128)
    sobrenome = models.CharField('Sobrenome', max_length=128)
    email = models.EmailField('e-mail', max_length=128)
    dtnasc = models.DateField('Data de Nascimento')
    sexo = models.CharField('Sexo', max_length=12, choices=SEXO_CHOICES)
    estadocivil = models.CharField('Estado Civil', max_length=12, choices=ESTADO_CIVIL_CHOICES)
    ativo = models.BooleanField('ativo', default=True)
    dtcriacao = models.DateTimeField('Data de criação', auto_now=True)


    def __str__(self):
        return self.nome
        #return f'{self.nome} {self.sobrenome}'

