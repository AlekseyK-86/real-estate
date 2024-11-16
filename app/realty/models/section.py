from django.db import models
from .building import Building


class Section(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название секции")
    number = models.PositiveSmallIntegerField(db_index=True, verbose_name="Номер секции")
    
    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"

    def __str__(self):
        return self.name
