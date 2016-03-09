from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Point(models.Model):
    """Point in map"""

    address = models.CharField(blank=True, max_length=500)
    lattitude = models.DecimalField(max_digits=20, decimal_places=10)
    altitude = models.DecimalField(max_digits=20, decimal_places=10)
