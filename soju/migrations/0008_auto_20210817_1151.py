# Generated by Django 3.2.6 on 2021-08-17 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soju', '0007_auto_20210817_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='category',
            field=models.CharField(db_index=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='name',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]