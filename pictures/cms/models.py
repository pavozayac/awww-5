from django.db import models
from django.contrib.auth.models import User


class Picture(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField('Name of the picture')
    description = models.TextField('Description of the picture', blank=True, default='')
    height = models.PositiveIntegerField('Height of the picture')
    width = models.PositiveIntegerField('Width of the picture')
    date_added = models.DateField('Date the picture was added')
    tags = models.TextField('String of space-separated tags related to the picture', default='')

    editors = models.ManyToManyField(User)


class Rectangle(models.Model):
    id = models.BigAutoField(primary_key=True)
    x = models.PositiveIntegerField('Position in the X coordinate')
    y = models.PositiveIntegerField('Position in the Y coordinate')
    height = models.PositiveIntegerField('Height of the rectangle')
    width = models.PositiveIntegerField('Width of the rectangle')
    fill = models.CharField('Fill color of the rectangle', max_length=30)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE,
                                related_name='rectangles')
