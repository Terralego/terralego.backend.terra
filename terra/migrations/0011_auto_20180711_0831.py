# Generated by Django 2.0.7 on 2018-07-11 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("terra", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="feature",
            name="source",
            field=models.IntegerField(
                help_text="Internal field used by pgRouting", null=True
            ),
        ),
        migrations.AddField(
            model_name="feature",
            name="target",
            field=models.IntegerField(
                help_text="Internal field used by pgRouting", null=True
            ),
        ),
    ]
