# Generated by Django 3.2.6 on 2021-08-14 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='category',
            field=models.CharField(max_length=200, verbose_name='category'),
        ),
    ]
