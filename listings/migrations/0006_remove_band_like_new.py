# Generated by Django 5.1.1 on 2024-09-08 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]
