from django.urls import path
from bezen_app import views

app_name = 'bezen_app'

urlpatterns = [
    path('item/detail/<int:id>', views.item_detail, name='item_detail'),
    path('recipes', views.recipes, name='recipes'),
    path('recipe/add', views.recipe_add, name='recipe_add'),
    path('recipe/details/<int:id>', views.recipe_details, name='recipe_details'),
    path('recipe/update/<int:id>', views.recipe_update, name='recipe_update'),
    path('recipe/delete/<int:id>', views.recipe_delete, name='recipe_delete'),
     path('search', views.search, name='search'),
]