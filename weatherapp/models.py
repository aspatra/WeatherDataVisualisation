from django.db import models

from django.utils.encoding import python_2_unicode_compatible
# Create your models here. 



class weatherinfo(models.Model):
      temperature = models.FloatField(max_length = 20)
      month = models.CharField(max_length = 15)
      year  = models.CharField(max_length =5)

      def __str__(self):
             return self.weatherinfo
