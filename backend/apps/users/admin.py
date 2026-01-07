from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    # Mostra o cargo na lista (tabela) de usuários
    list_display = ("email", "username", "role", "is_staff")

    # Corrigido: Usando desempacotamento (*) em vez de soma (+)
    fieldsets = (
        *UserAdmin.fieldsets,
        ("Informações Profissionais", {"fields": ("role",)}),
    )

    # Corrigido: Usando desempacotamento (*) em vez de soma (+)
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (None, {"fields": ("role",)}),
    )


# Registra o User com a nossa configuração customizada
admin.site.register(User, CustomUserAdmin)
