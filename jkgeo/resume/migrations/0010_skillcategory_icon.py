# Generated by Django 3.0.5 on 2020-05-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_degree_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillcategory',
            name='icon',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
