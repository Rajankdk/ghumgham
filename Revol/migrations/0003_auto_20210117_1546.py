# Generated by Django 3.0 on 2021-01-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Revol', '0002_destination_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='desc',
            field=models.TextField(),
        ),
    ]
