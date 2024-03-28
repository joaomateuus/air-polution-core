from django.db import models

class Estado(models.Model):
    nome = models.CharField(
        max_length=100,
        db_column='tx_nome',
        null=False,
        blank=False,
        verbose_name = 'Nome'
    )
    latitude = models.CharField(
        max_length=100,
        db_column='tx_latitude',
        null=False,
        blank=False,
        verbose_name = 'Latitude'
    )
    longitude = models.CharField(
        max_length=100,
        db_column='tx_longitude',
        null=False,
        blank=False,
        verbose_name = 'Longitude'
    )
    imagem_url = models.CharField(
        max_length=300,
        db_column='tx_img_url',
        null=True,
        blank=True,
        verbose_name = 'Imagem Url'
    )

    class Meta:
        managed = True
        db_table = 'tb_estados'


class NivelPoluicao(models.Model):
    class Status(models.TextChoices):
        POBRE = 'P', ('Pobre')
        MUITO_POBRE = 'MP', ('Muito Pobre')
        BOM = 'B', ('Bom')
        MODERADO = 'M', ('Moderado')
        RAZOAVEL = 'R', ('Razoavel')

    estado = models.ForeignKey(
        'Estado',
        on_delete=models.CASCADE,
        db_column='id_estado',
        db_index=False,
        null=False,
        blank=False,
        related_name='nivelpoluicao_estado',
        verbose_name='Estado'
    )
    concentracao_co2 = models.FloatField(
        db_column='nb_co2',
        null=False,
        blank=False,
        verbose_name='Nivel'
    )
    concentracao_no = models.FloatField(
        db_column='nb_nol',
        null=False,
        blank=False,
        verbose_name='Nivel'
    )
    concentracao_no2 = models.FloatField(
        db_column='nb_nivel',
        null=False,
        blank=False,
        verbose_name='Nivel'
    )
    status = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        choices=Status.choices,
        verbose_name='Order Status'
    )

    class Meta:
        managed = True
        db_table = 'tb_nivel_poluicao'

