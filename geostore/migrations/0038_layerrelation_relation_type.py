# Generated by Django 2.2.7 on 2019-11-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geostore', '0037_layerrelation_multiple'),
    ]

    operations = [
        migrations.AddField(
            model_name='layerrelation',
            name='relation_type',
            field=models.CharField(choices=[(None, 'Manuelle'), ('intersects', 'Intersects'), ('dwithin', 'DWithin')], default=(None, 'Manuelle'), max_length=25),
        ),
    ]
