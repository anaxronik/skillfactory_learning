# Generated by Django 3.0.2 on 2020-01-22 21:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0003_auto_20200122_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='title',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]