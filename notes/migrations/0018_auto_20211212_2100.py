# Generated by Django 3.1.5 on 2021-12-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0017_merge_20211202_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='header',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(max_length=160),
        ),
    ]
