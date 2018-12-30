from django.contrib import admin
from .models import Cocktail, Ingredient, Category

class CocktailAdmin(admin.ModelAdmin):
    list_display = ('name', 'recipe')

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', )


admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category, CategoryAdmin)
