from django.db import models
from django.urls import reverse


class Survey(models.Model):
    category1 = models.CharField(max_length=20, null=True)
    category2 = models.CharField(max_length=20, null=True)
    category3 = models.CharField(max_length=20, null=True)
    category4 = models.CharField(max_length=20, null=True)
    ABV1 = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    ABV2 = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    sugar = models.PositiveIntegerField(null=True)
    sanmi = models.PositiveIntegerField(null=True)

    def __self__(self):
        return self.category1

    def get_absolute_url(self):
        return reverse('survey:survey_result')