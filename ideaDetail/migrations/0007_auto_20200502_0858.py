# Generated by Django 3.0.5 on 2020-05-01 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideaDetail', '0006_auto_20200502_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcomment',
            name='add_text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_pk',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='addcomment',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
