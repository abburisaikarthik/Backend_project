# Generated by Django 4.1.2 on 2022-12-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banklockerapp", "0006_about_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignlocker",
            name="status",
            field=models.CharField(
                blank=True, default="Active", max_length=200, null=True
            ),
        ),
    ]
