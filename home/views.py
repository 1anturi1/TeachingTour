from django.shortcuts import render
from .models import*
from django.shortcuts import render
from .forms import*
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request,"index.html")

def listaTuristas(request):
    if request.method == 'POST':
        form = TuristaForm(request.POST)
        if form.is_valid():
            turista = form.save()
            turista.save()
            messages.add_message(request, messages.SUCCESS, 'Turista creado satisfactoriamente')
            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)
        context = {
            'form': form,
        }
    else:
        queryset = Turista.objects.all()
        context = {
        'turista_list': queryset
        }
    return render(request,"home.html", context)


def listaGuias(request):
    if request.method == 'POST':
        form = GuiaForm(request.POST)
        if form.is_valid():
            guia = form.save()
            guia.save()
            messages.add_message(request, messages.SUCCESS, 'Guia creado satisfactoriamente')
            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)
        context = {
            'form': form,
        }
    else:
        queryset = Guia.objects.all()
        context = {
        'guia_list': queryset
        }
    return render(request,"home.html", context)

@csrf_exempt
def listaToures(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            tour = form.save()
            tour.save()
            messages.add_message(request, messages.SUCCESS, 'Tour creado satisfactoriamente')
            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)
        context = {
            'form': form,
        }
    else:
        queryset = Tour.objects.all()
        context = {
        'title': 'Lista de toures',
        'tour_list': queryset
        }
    return render(request,"toures.html", context)

