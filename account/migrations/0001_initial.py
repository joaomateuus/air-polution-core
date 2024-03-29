# Generated by Django 5.0.3 on 2024-03-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(db_column='tx_email', max_length=256, unique=True)),
                ('password', models.CharField(db_column='tx_password', max_length=104)),
                ('full_name', models.CharField(db_column='tx_name', max_length=256)),
                ('last_login', models.DateTimeField(blank=True, db_column='dt_last_login', null=True)),
                ('is_active', models.BooleanField(db_column='cs_active', default=True)),
                ('is_superuser', models.BooleanField(db_column='cs_superuser', default=False, null=True)),
                ('is_staff', models.BooleanField(db_column='cs_staff', default=False, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'tb_auth_user',
                'managed': True,
            },
        ),
    ]
