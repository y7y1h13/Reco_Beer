# Generated by Django 3.2.6 on 2021-08-17 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soju', '0008_auto_20210817_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userstar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ABV', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='star_ABV', to='soju.beer')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='star_category', to='soju.beer')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='star_name', to='soju.beer')),
                ('s', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='star_s', to='soju.beer')),
                ('sanmi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='star_sanmi', to='soju.beer')),
                ('star', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='star_star', to='soju.beer')),
                ('sugar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='star_sugar', to='soju.beer')),
            ],
        ),
    ]
