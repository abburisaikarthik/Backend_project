# Generated by Django 4.0.2 on 2022-12-30 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banklockerapp', '0003_assignlocker_idproof'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignlocker',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='banklockerapp.lockertype'),
        ),
    ]
