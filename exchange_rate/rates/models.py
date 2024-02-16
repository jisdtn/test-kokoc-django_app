from django.db import models

class Currency(models.Model):
    """Model so we can store rates in DB"""
    charcode = models.CharField(max_length=10)
    date = models.DateField()
    rate = models.IntegerField()

    def __str__(self):
        return f"{self.charcode} - {self.date}: {self.rate}"

