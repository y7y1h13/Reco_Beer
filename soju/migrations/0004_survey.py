# Generated by Django 3.2.6 on 2021-08-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soju', '0003_rename_bear_beer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, verbose_name='category')),
                ('ABV', models.DecimalField(decimal_places=1, max_digits=2)),
                ('sugar', models.PositiveIntegerField()),
            ],
        ),
    ]
