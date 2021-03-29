from django.views.generic import ListView
from .models import Item
from django.shortcuts import render, redirect, get_object_or_404


class Home(ListView):
    model = Item
    template_name = 'home.html'


def add(request):
    title = request.POST.get('title')
    Item.objects.create(title=title)

    return redirect('core:home')


def delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    
    return redirect('core:home')


def complete(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.done = True
    item.save()
    
    return redirect('core:home')


def clear(request):
    item = Item.objects.filter(done=True).delete()
    
    return redirect('core:home')