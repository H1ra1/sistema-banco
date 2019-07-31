from django.db import models

class Titular(models.Model):
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

    email = models.EmailField(
        max_length = 255,
        verbose_name = 'E-mail',
    )

    senha = models.CharField(
        max_length = 255,
        verbose_name = 'Senha',
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
        Titular,
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