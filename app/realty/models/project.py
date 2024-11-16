from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    description = models.TextField(verbose_name="Описание")

    class Meta:
            verbose_name = "Проект"
            verbose_name_plural = "Проекты"
    
    def __str__(self) -> str:
        return self.name
