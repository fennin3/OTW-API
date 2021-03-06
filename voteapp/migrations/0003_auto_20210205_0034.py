# Generated by Django 3.1.6 on 2021-02-05 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voteapp', '0002_auto_20210204_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklypost',
            name='rating',
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='thumbnail',
            field=models.ImageField(upload_to='categories/images/'),
        ),
        migrations.AlterField(
            model_name='weeklypost',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weekly_posts', to='voteapp.postcategory'),
        ),
    ]
