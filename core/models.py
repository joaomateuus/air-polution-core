from django.db import models

class Bairro(models.Model):
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

    class Meta:
        managed = True
        db_table = 'tb_bairros'


class NivelPoluicao(models.Model):
    class Status(models.TextChoices):
        RUIM = 'R', ('Ruim')
        BOM = 'B', ('Bom')
        MODERADO = 'M', ('Moderado')

    bairro = models.ForeignKey(
        'Bairro',
        on_delete=models.CASCADE,
        db_column='id_bairro',
        db_index=False,
        null=False,
        blank=False,
        related_name='nivelpoluicao_bairros',
        verbose_name='Bairro'
    )
    nivel = models.IntegerField(
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

    def save(self, *args, **kwargs):
        if self.nivel >= 70:
            self.status = self.Status.RUIM
        elif self.nivel >= 30:
            self.status = self.Status.MODERADO
        else:
            self.status = self.Status.BOM
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'tb_nivel_poluicao'

