from django.db import models

from stdimage.models import StdImageField

# Signals
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    created_at = models.DateField('Data de Inserção', auto_now_add=True)
    update_at = models.DateField('Data de Atualização', auto_now=True)
    is_active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Product(Base):
    name = models.CharField('Nome', max_length=250)
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    stock = models.IntegerField('Estoque')
    img = StdImageField(
        'Imagem',
        upload_to='uploads',
        variations={
            'thumb': (120, 120),
            'medium': (300, 300),
            'large': (1000, 1000),
        }
    )
    url_slug = models.SlugField('Slug', max_length=250, blank=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'manage_products_products'


def product_pre_save(signal, instance, sender, **kwargs):
    instance.url_slug = slugify(instance.name)


signals.pre_save.connect(product_pre_save, sender=Product)
