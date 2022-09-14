from django.urls import path
from .import views


app_name = 'auth_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_method, name= 'register'),
    path('login', views.login_method, name='login'),
    path('logout', views.logout_method, name='logout'),
    path('profile', views.profile_update, name='profile'),
]

