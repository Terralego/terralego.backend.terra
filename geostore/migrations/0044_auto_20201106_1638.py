# Generated by Django 3.1.3 on 2020-11-06 16:38

from django.db import migrations, models
import django.db.models.deletion
import geostore.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('geostore', '0043_merge_20201023_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='identifier',
            field=models.CharField(default=uuid.uuid4, max_length=255, verbose_name='Identifier'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='layer',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.PROTECT, related_name='features', to='geostore.layer', verbose_name='Layer'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='properties',
            field=models.JSONField(blank=True, default=dict, verbose_name='Properties'),
        ),
        migrations.AlterField(
            model_name='featureextrageom',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_geometries', to='geostore.feature', verbose_name='Feature'),
        ),
        migrations.AlterField(
            model_name='featureextrageom',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='Identifier'),
        ),
        migrations.AlterField(
            model_name='featureextrageom',
            name='layer_extra_geom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='geostore.layerextrageom', verbose_name='Feature'),
        ),
        migrations.AlterField(
            model_name='featureextrageom',
            name='properties',
            field=models.JSONField(blank=True, default=dict, verbose_name='Properties'),
        ),
        migrations.AlterField(
            model_name='featurerelation',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_as_destination', to='geostore.feature', verbose_name='Destination'),
        ),
        migrations.AlterField(
            model_name='featurerelation',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_as_origin', to='geostore.feature', verbose_name='Origin'),
        ),
        migrations.AlterField(
            model_name='featurerelation',
            name='properties',
            field=models.JSONField(blank=True, default=dict, verbose_name='Properties'),
        ),
        migrations.AlterField(
            model_name='featurerelation',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_features', to='geostore.layerrelation', verbose_name='Relation'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='authorized_groups',
            field=models.ManyToManyField(blank=True, related_name='authorized_layers', to='auth.Group', verbose_name='Authorized groups'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='name',
            field=models.CharField(default=uuid.uuid4, max_length=256, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='schema',
            field=models.JSONField(blank=True, default=dict, validators=[geostore.validators.validate_json_schema], verbose_name='Schema'),
        ),
        migrations.AlterField(
            model_name='layerextrageom',
            name='editable',
            field=models.BooleanField(default=True, verbose_name='Editable'),
        ),
        migrations.AlterField(
            model_name='layerextrageom',
            name='layer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_geometries', to='geostore.layer', verbose_name='Layer'),
        ),
        migrations.AlterField(
            model_name='layerextrageom',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='layerextrageom',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='layergroup',
            name='layers',
            field=models.ManyToManyField(related_name='layer_groups', to='geostore.Layer', verbose_name='Layers'),
        ),
        migrations.AlterField(
            model_name='layergroup',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Name'),
        ),
    ]
