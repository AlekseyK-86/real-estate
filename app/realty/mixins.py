import os

from django.db import models
from django.core.exceptions import ValidationError

class UploadToMixin(models.Model):
    class Meta:
        abstract = True

    def valid_extensions(instance, filename):
        VALID_EXTENSIONS  = ['.jpg', '.jpeg', '.png']
        ext = os.path.splitext(filename)[1].lower()
        if ext not in VALID_EXTENSIONS:
            raise ValidationError(f"Поддерживаются только следующие форматы: {', '.join(VALID_EXTENSIONS)}")

