# Generated by Django 3.0.5 on 2020-04-21 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_remove_recipe_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.IntegerField(choices=[(1, 'Breakfast'), (2, 'Lunch'), (3, 'Dinner'), (4, 'Side'), (5, 'Snack')], null=True),
        ),
    ]
