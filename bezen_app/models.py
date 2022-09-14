from django.db import models

class Food(models.Model):
    f_id = models.BigAutoField(primary_key=True, null=False, blank=False)
    f_name = models.CharField(max_length=60)
    f_description : models.CharField(max_length=200)
    f_procedure = models.TextField()
    f_photo = models.ImageField()

class Ingredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ing = models.CharField(max_length=60)