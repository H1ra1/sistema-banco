from django.contrib import admin
from conta import models

admin.site.register(models.Titular)
admin.site.register(models.Conta)