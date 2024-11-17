import os
import hashlib
from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from .building import Building
from .flatcategory import FlatCategory
from .floor import Floor
from .section import Section
from realty.mixins import UploadToMixin

class Flat(UploadToMixin, models.Model):

    def upload_to(instance, filename):
        UploadToMixin.valid_extensions(instance, filename)

        flat_rooms = str(instance.rooms)
        building_number = str(instance.building.number)
        project_name = str(instance.building.project.name)
        flat_description = instance.description.replace(" ", "_")

        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")        
        short_hash = hashlib.md5(str(flat_description + current_time).encode()).hexdigest()[:8]

        return os.path.join('photos/', project_name, building_number, flat_rooms, short_hash, filename)
    
    ON_SALE = 'On sale'
    SOLD = 'Sold'

    STATUS_CHOICES = [(ON_SALE, "В продаже"), (SOLD, "Продана")]

    square = models.FloatField(
        verbose_name="Общая площадь", validators=[MinValueValidator(limit_value=0)]
    )
    living_space = models.FloatField(
        verbose_name="Жилая площадь", validators=[MinValueValidator(limit_value=0)]
    )
    kitchen_area = models.FloatField(
        verbose_name="Площадь кухни", validators=[MinValueValidator(limit_value=0)]
    )
    rooms = models.PositiveSmallIntegerField(verbose_name="Количество комнат")
    status = models.CharField(
        max_length=7, choices=STATUS_CHOICES, default=ON_SALE, verbose_name="Статус"
    )
    price = models.PositiveBigIntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to=upload_to, verbose_name="Изображение")
    floor = models.ForeignKey(Floor, on_delete=models.PROTECT, verbose_name="Этаж")
    category = models.ForeignKey(FlatCategory, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Класс квартиры')
    section = models.ForeignKey(Section, null=True, on_delete=models.PROTECT, verbose_name="Секция")
    building = models.ForeignKey(Building, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Дом")

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
    
    def __str__(self):
        return self.description