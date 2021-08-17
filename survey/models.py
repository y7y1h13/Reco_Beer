from django.db import models
from django.urls import reverse


class Survey(models.Model):
    category = models.CharField(max_length=100, verbose_name='category')
    ABV1 = models.DecimalField(max_digits=2, decimal_places=1)
    ABV2 = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    sugar = models.PositiveIntegerField()
    sanmi = models.PositiveIntegerField(null=True)

    def __self__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('survey:survey_result')