# Generated by Django 4.2.11 on 2024-05-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_picture_date_added_picture_description_picture_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Description of the picture'),
        ),
    ]
