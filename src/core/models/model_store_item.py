from django.db import models

class StoreItem(models.Model):
    name = models.CharField('Nome', max_length=100)
    cost = models.PositiveIntegerField('Custo')
    image = models.CharField('Imagem', max_length=100)

    class Meta:
        verbose_name = 'Item da Loja'
        verbose_name_plural = 'Itens da Loja'

    def __str__(self):
        return self.name
