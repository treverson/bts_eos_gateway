# Generated by Django 2.0.7 on 2018-07-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0002_auto_20180711_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='eos_hash',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
