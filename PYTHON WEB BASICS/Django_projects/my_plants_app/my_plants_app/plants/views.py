from django.shortcuts import render, redirect

from my_plants_app.common.views import add_user_to_context
from my_plants_app.plants.forms import PlantForm, PlantDeleteForm
from my_plants_app.plants.models import Plant


def plant_create(request):
    form = PlantForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'create-plant.html', context=add_user_to_context(context))


def plant_edit(request, pk):
    plant = Plant.objects.get(pk=pk)
    form = PlantForm(request.POST or None, instance=plant)

    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'edit-plant.html', context=add_user_to_context(context))


def plant_details(request, pk):
    plant = Plant.objects.get(pk=pk)
    context = {
        'plant': plant,
    }

    return render(request, 'plant-details.html', context=add_user_to_context(context))


def plant_delete(request, pk):
    plant = Plant.objects.get(pk=pk)
    form = PlantDeleteForm(request.POST or None, instance=plant)

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'delete-plant.html', context=add_user_to_context(context))


