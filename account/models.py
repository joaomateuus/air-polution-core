from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.urls import reverse
from account import managers

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    email = models.CharField(
        max_length=256,
        db_column='tx_email',
        null=False,
        unique=True,
    )
    password = models.CharField(
        max_length=104,
        db_column='tx_password',
        null=False
    )
    full_name = models.CharField(
        max_length=256,
        db_column='tx_name',
        null=False
    )
    last_login = models.DateTimeField(
        db_column='dt_last_login',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )
    is_superuser = models.BooleanField(
        db_column='cs_superuser',
        null=True,
        default=False
    )
    is_staff = models.BooleanField(
        db_column='cs_staff',
        null=True,
        default=False
    )

    objects = managers.UserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.id})
    
    class Meta:
        managed = True
        db_table = 'tb_auth_user'

