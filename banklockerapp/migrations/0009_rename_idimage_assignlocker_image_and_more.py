# Generated by Django 4.0.2 on 2022-12-30 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banklockerapp', '0008_alter_assignlocker_idimage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignlocker',
            old_name='idimage',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='assignlocker',
            old_name='picimage',
            new_name='image2',
        ),
    ]
