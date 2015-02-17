from django.contrib import admin
from models import *

class RecipeAdmin(admin.ModelAdmin):
    filter_horizontal = ('ingredients',)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Review)
