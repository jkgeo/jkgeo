# Generated by Django 3.0.5 on 2020-05-03 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_degree_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree',
            name='type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]