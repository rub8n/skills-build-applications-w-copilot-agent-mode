# Generated by Django 4.1 on 2025-04-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("octofit_tracker", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="members",
            field=models.TextField(),
        ),
    ]
