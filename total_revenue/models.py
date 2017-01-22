from __future__ import unicode_literals

from django.db import models

# Create your models here.
class OrdersSheet(models.Model):
    orders_url = models.CharField(max_length=250)

    def __str__(self):
        return self.orders_url