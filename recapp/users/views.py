import os

from django.db.models import Model
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddRecept
from .models import Recept
from django.contrib import messages


def home(request):
    recept_list = Recept.objects.order_by('?')[:5]
    return render(request, 'users/home.html', {'recept_list': recept_list, 'title': 'Домашняя'})


def about(request):
    return render(request, 'users/about.html', {'title': 'Наши рецепты'})


def add_recept(request):
    form = AddRecept(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            new_recept = form.save(commit=False)
            new_recept.author = request.user.username
            new_recept.save()
        return redirect('home')
    else:
        form = AddRecept()
    return render(request, 'users/addrecept.html', {'form': form, 'title': 'Добавить рецепт'})


# def edit_recept(request, recept_id):
#     instance = get_object_or_404(Recept, id=recept_id)
#     if request.method == 'POST':
#         form = AddRecept(request.POST or None, instance=instance, files=request.FILES)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.save()
#             return redirect('home')
#     form = AddRecept(instance=instance)
#     return render(request, 'users/edit_recept.html', {'instance': instance, 'form':form,'title': 'Редактировать рецепт'})

def edit_recept(request, recept_id):
    rcpt = get_object_or_404(Recept, id=recept_id)
    if request.method == 'GET':
        context = {'form': AddRecept(instance=rcpt), 'id': recept_id, 'title': 'Редактировать рецепт'}
        return render(request, 'users/edit_recept.html', context)
    elif request.method == 'POST':
        form = AddRecept(request.POST, request.FILES, instance=rcpt)
        if form.is_valid():
            form.save()
            messages.success(request, 'Рецепт обновлен.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the following errors:')
            context = {'form': form, 'id': recept_id, 'title': 'Редактировать рецепт'}
            return render(request, 'users/edit_recept.html', context)


def recept(request, recept_id):
    recept_ = get_object_or_404(Recept, id=recept_id)
    return render(request, 'users/recept.html', {'recept': recept_, 'title': recept_.recept_name})
