# Generated by Django 4.0.2 on 2022-12-30 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banklockerapp', '0004_assignlocker_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignlocker',
            name='status',
            field=models.CharField(blank=True, default='Unapproved', max_length=200, null=True),
        ),
    ]