# Generated by Django 2.0.13 on 2019-06-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("terra", "0024_layer_geom_type")]

    operations = [
        migrations.AddIndex(
            model_name="feature",
            index=models.Index(fields=["layer"], name="terra_featu_layer_i_921f95_idx"),
        ),
        migrations.AddIndex(
            model_name="feature",
            index=models.Index(
                fields=["updated_at"], name="terra_featu_updated_62a19a_idx"
            ),
        ),
    ]
