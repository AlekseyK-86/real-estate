import os

from django.db import models
from django.core.exceptions import ValidationError

from realty.mixins import UploadToMixin


class Project(UploadToMixin, models.Model):

    def upload_to(self, filename):
        self.valid_extensions(filename)
                
        project_name = str(self.name)

        return os.path.join('photos/', project_name, filename)
    
    

    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to=upload_to, verbose_name="Изображение")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
    
    def __str__(self) -> str:
        return self.name
