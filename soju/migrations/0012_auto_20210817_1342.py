# Generated by Django 3.2.6 on 2021-08-17 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soju', '0011_auto_20210817_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='ABV',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='beer',
            name='meta_description',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='re',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='s',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='sugar',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]