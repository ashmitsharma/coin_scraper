# Generated by Django 5.0.6 on 2024-06-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskmanager", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scrapingtask",
            name="job_id",
            field=models.CharField(max_length=255),
        ),
    ]
