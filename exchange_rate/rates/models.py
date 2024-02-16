from django.db import models


class Currency(models.Model):
    """Model so we can store rates in DB"""
    objects = models.Manager()
    charcode = models.CharField(max_length=3)
    date = models.DateField()
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.charcode} - {self.date}: {self.rate}"
