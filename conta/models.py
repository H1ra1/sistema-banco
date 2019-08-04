from django.db import models
import re
from django.core import validators
from django.contrib.auth.models import (PermissionsMixin, AbstractBaseUser,
    UserManager)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length = 255,
        unique = True,
        validators = [validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'O nome de usuário só pode conter letras, digitos ou outras paradas',
            'invalid',
        )],
        verbose_name = 'Nome de usuário',
    )
    
    email = models.EmailField(
        max_length = 255,
        unique = True,
        verbose_name = 'E-mail',
    )

    is_active = models.BooleanField(
        default = True,
        blank = True,
        verbose_name = 'Ativo',
    )

    is_staff = models.BooleanField(
        default = False,
        blank = True,
        verbose_name = 'Staff',
    )

    date_joined = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Data de entrada',
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Perfil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
    )

    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    )

    nome = models.CharField(
        max_length = 255,
        verbose_name = 'Nome',
    )

    sobrenome = models.CharField(
        max_length = 255,
        verbose_name = 'Sobrenome',
    )

    data_nascimento = models.CharField(
        max_length = 255,
        verbose_name = 'Data de nascimento',
    )

    cpf = models.CharField(
        max_length = 255,
        verbose_name = 'CPF',
    )

    telefone = models.CharField(
        max_length = 255,
        verbose_name = 'Telefone',
    )

    genero = models.CharField(
        max_length = 255,
        verbose_name = 'Genero',
        choices = GENEROS,
    )

    data_criacao = models.DateField(
        auto_now_add = True,
    )

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Conta(models.Model):
    titular = models.OneToOneField(
        Perfil,
        on_delete = models.CASCADE,
    )

    saldo = models.FloatField(
        default = 0.0,
        verbose_name = 'Saldo',
    )

    numero_conta = models.CharField(
        max_length = 255,
        verbose_name = 'Numero da conta',
    )

    agencia = models.CharField(
        max_length = 255,
        default = '235',
        verbose_name = 'Agencia',
    )

    nome_banco = models.CharField(
        max_length = 255,
        default = 'LiraBank',
        verbose_name = 'Nome do banco',
    )

    ativo = models.BooleanField(
        default = True,
    )

    def __str__(self):
        return f'{self.numero_conta}'