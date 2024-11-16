import os

from django.db import models
from django.core.exceptions import ValidationError

class Project(models.Model):

    def upload_to(instance, filename):
        valid_extensions = ['.jpg', '.jpeg', '.png']
        ext = os.path.splitext(filename)[1].lower()
        if ext not in valid_extensions:
            raise ValidationError(f"Поддерживаются только следующие форматы: {', '.join(valid_extensions)}")
        
        project_name = str(instance.name)

        return os.path.join('photos/', project_name, filename)
    
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to=upload_to, verbose_name="Изображение") # "photos/project/%Y/%m/%d/"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
    
    def __str__(self) -> str:
        return self.name
