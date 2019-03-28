from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Category, Cocktail, Ingredient

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'alcohol_percentage','category')


class CocktailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cocktail
        fields = ('name', 'ingredients', 'recipe')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('category')
        