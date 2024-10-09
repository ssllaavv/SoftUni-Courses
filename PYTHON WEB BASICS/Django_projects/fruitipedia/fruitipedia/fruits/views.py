from django.shortcuts import render, redirect

from fruitipedia.common.views import add_user_to_context
from fruitipedia.fruits.forms import FruitCreateForm, FruitBaseForm, FruitDeleteForm
from fruitipedia.fruits.models import Fruit


def fruit_create(request):

    form = FruitCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, template_name='create-fruit.html', context=add_user_to_context(context))


def fruit_details(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    context = {
        'fruit': fruit
    }

    return render(request, template_name='details-fruit.html', context=add_user_to_context(context))


def fruit_edit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = FruitBaseForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, template_name='edit-fruit.html', context=add_user_to_context(context))


def delete_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = FruitDeleteForm(request.POST or None, instance=fruit)
    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, template_name='delete-fruit.html', context=add_user_to_context(context))
