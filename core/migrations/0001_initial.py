# Generated by Django 5.0.3 on 2024-03-19 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='tx_nome', max_length=100, verbose_name='Nome')),
                ('latitude', models.CharField(db_column='tx_latitude', max_length=100, verbose_name='Latitude')),
                ('longitude', models.CharField(db_column='tx_longitude', max_length=100, verbose_name='Longitude')),
            ],
            options={
                'db_table': 'tb_bairros',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NivelPoluicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.IntegerField(db_column='nb_nivel', verbose_name='Nivel')),
                ('status', models.CharField(choices=[('R', 'Ruim'), ('B', 'Bom'), ('M', 'Moderado')], max_length=2, verbose_name='Order Status')),
                ('bairro', models.ForeignKey(db_column='id_bairro', db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='nivelpoluicao_bairros', to='core.bairro', verbose_name='Bairro')),
            ],
            options={
                'db_table': 'tb_nivel_poluicao',
                'managed': True,
            },
        ),
    ]