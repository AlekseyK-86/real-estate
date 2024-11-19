import os

from django.db import models
from django.core.exceptions import ValidationError

from realty.constants import VALID_EXTENSIONS_FOR_UPLOAD_IMAGES


class UploadToMixin(models.Model):  
    def valid_extensions(self, filename):
        ext = os.path.splitext(filename)[1].lower()
        if ext not in VALID_EXTENSIONS_FOR_UPLOAD_IMAGES:
            raise ValidationError(
                f"Для загрузки поддерживаются следующие форматы изображений:\
                {', '.join(VALID_EXTENSIONS_FOR_UPLOAD_IMAGES)}"
                )
    
    class Meta:
        abstract = True
