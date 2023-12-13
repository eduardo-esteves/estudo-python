from django.db import models

# Create your models here.
from stdimage.models import StdImageField


class Base(models.Model):
    created_at = models.DateField('Data de Inserção', auto_now_add=True)
    update_at = models.DateField('Data de Atualização', auto_now=True)
    is_active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Services(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )

    service = models.CharField('Serviço', max_length=200)
    description = models.TextField('Descrição')
    icone = models.CharField('Icone', max_length=50, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.service

class Position(Base):
    job_title = models.CharField('Cargo', max_length=200)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.job_title


class Team_Members(Base):
    professional = models.CharField('Nome', max_length=100)
    job_title = models.ForeignKey('fusion.Position', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=250)
    img = StdImageField(
        'Imagem',
        upload_to='team',
        variations={
            'thumb': (480, 480),
        }
    )
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.professional
