# Generated by Django 3.0.5 on 2020-05-09 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0012_auto_20200508_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='date_had',
            field=models.DateField(null=True),
        ),
    ]