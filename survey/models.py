from django.db import models


class Survey(models.Model):
    CATEGORY = (
        ('흑맥주', '흑맥주'),
        ('밀맥주', '밀맥주'),
        ('과일맥주', '과일맥주'),
        ('수제맥주', '수제맥주')
    )
    SUGAR = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )
    category = models.CharField(max_length=200, verbose_name='category', choices=CATEGORY)
    ABV = models.DecimalField(max_digits=2, decimal_places=1)
    sugar = models.PositiveIntegerField(choices=SUGAR)

    def __self__(self):
        return self.category