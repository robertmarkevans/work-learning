from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.category

class Ingredient(models.Model):    
    name = models.CharField(max_length=50, null=False, blank=False)
    alcohol_percentage = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
            return self.name

    class Meta:
        ordering = ('name',)

class Cocktail(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    ingredients = models.ManyToManyField(Ingredient)
    recipe = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
    