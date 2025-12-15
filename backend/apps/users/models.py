from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Opções para o campo de cargo
    class Role(models.TextChoices):
        MANAGER = 'MANAGER', 'Gerente'
        OPERATOR = 'OPERATOR', 'Operador'

    email = models.EmailField(unique=True, verbose_name='E-mail')
    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.OPERATOR,
        verbose_name='Cargo'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
