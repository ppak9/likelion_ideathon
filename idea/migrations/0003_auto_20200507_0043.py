# Generated by Django 3.0.5 on 2020-05-06 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0002_auto_20200507_0023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addcomment',
            old_name='create_data',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='create_data',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='idea',
            old_name='idea_create_data',
            new_name='idea_create_date',
        ),
    ]
