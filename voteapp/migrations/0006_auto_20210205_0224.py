# Generated by Django 3.1.6 on 2021-02-05 02:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteapp', '0005_weeklywinner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklywinner',
            name='category',
        ),
        migrations.AddField(
            model_name='weeklywinner',
            name='rating',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
