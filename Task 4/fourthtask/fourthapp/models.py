from django.db import models

# Create your models here.
class Currency(models.Model):
    currency_code = models.CharField('Currency Code', max_length=3)
    counts = models.IntegerField()
    def __str__(self):
        return self.currency_code