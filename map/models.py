from __future__ import unicode_literals

from django.db import models
import json
# Create your models here.
class Point(models.Model):
    """Point in map"""

    address = models.CharField(blank=True, max_length=500)
    lat = models.DecimalField(max_digits=20, decimal_places=10)
    lng = models.DecimalField(max_digits=20, decimal_places=10)

    def deserialize(self,content):
        data = json.loads(content)

        self.address = data['address']
        self.lat = data['lat']
        self.lng = data['lng']

    def __str__ (self):
        return '%s : lng %.5f , lat %.5f'% (self.address,self.lng,self.lat)
