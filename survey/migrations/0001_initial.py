# Generated by Django 3.2.6 on 2021-08-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('흑맥주', '흑맥주'), ('밀맥주', '밀맥주'), ('과일맥주', '과일맥주'), ('수제맥주', '수제맥주')], max_length=200, verbose_name='category')),
                ('ABV', models.DecimalField(decimal_places=1, max_digits=2)),
                ('sugar', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
            ],
        ),
    ]
