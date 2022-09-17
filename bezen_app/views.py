from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bezen_app.forms import *
from bezen_app.models import *
from django.db.models import Q

# Create your views here.

def item_detail(request, id):
    item = Food.objects.get(f_id = id)
    return render(request, 'detail_view.html', {'item': item})

def recipes(request):
    items = Food.objects.filter(user = request.user)
    return render(request, 'recipes_view.html', {'items': items})

def recipe_details(request, id):
    item = Food.objects.get(f_id = id)
    return render(request, 'recipe_details.html', {'item': item})

def recipe_add(request):
    form = RecipeAddForm()
    if request.method == "POST":
        data = RecipeAddForm(request.POST, request.FILES)
        if data.is_valid():
            tmp = data.save(commit=False)
            tmp.user = request.user
            tmp.save()
            messages.success(request, "* Updated successfully .....")
            return HttpResponseRedirect('/site/recipes')
        else:
            messages.error(request, "* Invalid data . Try Again !!")
            return HttpResponseRedirect('/site/recipes')
    context = {
        'form': form,
    }
    return render(request, 'recipe_add.html', context=context)

def recipe_update(request, id):
    item = Food.objects.get(f_id = id)
    form = RecipeUpdateForm(instance=item)
    if request.method == "POST":
        data = RecipeUpdateForm(request.POST, request.FILES, instance=item)
        if data.is_valid():
            data.save()
            messages.success(request, "* Updated successfully .....")
            return HttpResponseRedirect('/site/recipes')
        else:
            messages.error(request, "* Invalid data . Try Again !!")
            return HttpResponseRedirect('/site/recipes')
    context = {
        'form': form,
    }
    return render(request, 'recipe_update.html', context=context)

def recipe_delete(request, id):
    item = Food.objects.get(f_id = id)
    item.delete()
    return render(request, 'recipes_view.html')

def search(request):
    if request.method == 'GET':
        search_request = request.GET['search']
        res= Food.objects.filter(Q(f_name__icontains = search_request) | Q(ingredients__icontains = search_request))
    return render(request, 'search.html', {'items': res})
