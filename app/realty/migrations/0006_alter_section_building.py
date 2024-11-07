# Generated by Django 4.2.16 on 2024-11-07 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0005_section_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realty.building', verbose_name='Id дома'),
        ),
    ]
