from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Cuisine(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class UnitsOfMeasure(models.Model):
    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=8)

    def __str__(self):
        return self.abbreviation

class Ingredient(models.Model):
    VEGETABLES = 'V'
    FRUITS = 'F'
    GRAINS = 'G'
    MEAT = 'M'
    DAIRY = 'D'
    OTHER = 'O'

    FOOD_GROUP_CHOICES = [
        (VEGETABLES, 'Vegetables'),
        (FRUITS, 'Fruits'),
        (GRAINS, 'Grains'),
        (MEAT, 'Meat'),
        (DAIRY, 'Dairy'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(max_length=128)
    food_group = models.CharField(
        max_length=1,
        choices=FOOD_GROUP_CHOICES
    )

    def __str__(self):
        return self.name

class Recipe(models.Model):
    BREAKFAST = 1
    LUNCH = 2
    DINNER = 3
    SIDE = 4
    SNACK = 5

    RECIPE_CATEGORY_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (SIDE, 'Side'),
        (SNACK, 'Snack')
    ]
    
    title = models.CharField(max_length=255)    
    cuisine = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.IntegerField(
        choices=RECIPE_CATEGORY_CHOICES,
        null=True
    )
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='Quantity')
    slug = models.SlugField(null=True, blank=True)
    added = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    photo = models.ImageField(upload_to='recipes')
    link = models.URLField(max_length=255)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.added = timezone.now()
        self.modified = timezone.now()
        self.slug = slugify(self.title)
        return super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Step(models.Model):
    number = models.IntegerField(null=True)
    step = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Note(models.Model):
    number = models.IntegerField(null=True)
    note = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Quantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True, blank=True)
    value = models.FloatField()
    unit = models.ForeignKey(UnitsOfMeasure, on_delete=models.SET_NULL, null=True, blank=True)