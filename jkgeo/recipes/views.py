from django.shortcuts import render
from .models import Recipe, Quantity, Step, Note


def recipeList(request):
	recipes = Recipe.objects.all()
	context = {'recipes': recipes}
	return render(request, 'recipes/recipes.html', context)


def recipeDetail(request, recipe_slug):
	context = {}
	try:
		recipe = Recipe.objects.get(slug=recipe_slug)
		steps = Step.objects.filter(recipe=recipe).order_by('number')
		notes = Note.objects.filter(recipe=recipe).order_by('number')
		ingredients = recipe.ingredients.all()
		context['details'] = []
		for ingredient in ingredients:
			ing = {}
			q = Quantity.objects.get(recipe=recipe, ingredient=ingredient)
			ing['ingredient'] = ingredient
			ing['quantity'] = q
			ing['steps'] = steps
			context['details'].append(ing)

		context['recipe'] = recipe
		context['steps'] = steps
		context['notes'] = notes

	except Recipe.DoesNotExist:
		context['recipe'] = None
		context['details'] = None
		context['steps'] = None
		context['notes'] = None


	return render(request, 'recipes/recipe-detail.html', context)