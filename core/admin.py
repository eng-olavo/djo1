from django.contrib import admin
from .models import Produto, Cliente, Teste1, Teste2


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


class Teste1Admin(admin.ModelAdmin):
    list_display = ('Test1', 'TipoCharField', 'TipoEmail', 'TipoTextField')


class Teste2Admin(admin.ModelAdmin):
    list_display = ('Test2', 'TipoIntegerField', 'TipoDecimalField', 'TipoFloatField', 'TipoBooleanFieldTrue', 'TipoBooleanFieldFalse')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Teste1, Teste1Admin)
admin.site.register(Teste2, Teste2Admin)

