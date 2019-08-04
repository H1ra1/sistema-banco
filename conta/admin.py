from django.contrib import admin
from .models import User, Perfil, Conta

class Titular_admin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'sobrenome', 'telefone', 'data_criacao']


class Conta_admin(admin.ModelAdmin):
    list_display = ['titular', 'numero_conta', 'agencia', 'nome_banco' ,'saldo', 'ativo']
    search_fields = ['titular', 'numero_conta']

admin.site.register(Perfil, Titular_admin)
admin.site.register(Conta, Conta_admin)
admin.site.register(User)
# admin.site.register(Perfil)
