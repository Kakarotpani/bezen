from django.db import models
from auth_app.models import User

class Food(models.Model):
    f_id = models.BigAutoField(primary_key=True, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=60, verbose_name='Item name')
    f_description = models.CharField(max_length=200, verbose_name='Description')
    ingredients = models.TextField()
    f_procedure = models.TextField(verbose_name='procedure')
    f_photo = models.ImageField(blank=True, null=True, upload_to = 'food_img', verbose_name='Item Photo')

    def __str__(self):
        return self.f_name
    
    