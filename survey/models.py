from django.db import models
from django.urls import reverse


class Survey(models.Model):
    category = models.CharField(max_length=200, verbose_name='category')
    ABV = models.DecimalField(max_digits=2, decimal_places=1)
    sugar = models.PositiveIntegerField()

    def __self__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('survey:survey_result')