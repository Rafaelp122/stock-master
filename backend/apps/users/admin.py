from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    # Mostra o cargo na lista (tabela) de usuários
    list_display = ('email', 'username', 'role', 'is_staff')
    
    # Adiciona o campo 'role' no formulário de edição de usuário
    # Estamos pegando os fieldsets padrão e somando uma nova seção
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Profissionais', {'fields': ('role',)}),
    )

    # Adiciona o campo 'role' na tela de criação de usuário (add form)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

# Registra o User com a nossa configuração customizada
admin.site.register(User, CustomUserAdmin)
