
from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns(
    '',

    url(r'^recipes/$', RecipeList.as_view(), name='recipe-list'),
    url(r'^ingredients/$', IngredientList.as_view(), name='ingredient-list'),
    url(r'^add-recipe$', AddRecipe.as_view(), name='add-recipe'),
    url(r'^review$', ReviewList.as_view(), name='review-list'),

)