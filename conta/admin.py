from django.contrib import admin
from conta import models

class Titular_admin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'sobrenome', 'email', 'telefone', 'data_criacao']


class Conta_admin(admin.ModelAdmin):
    list_display = ['titular', 'numero_conta', 'agencia', 'nome_banco' ,'saldo', 'ativo']
    search_fields = ['titular', 'numero_conta']

admin.site.register(models.Titular, Titular_admin)
admin.site.register(models.Conta, Conta_admin)