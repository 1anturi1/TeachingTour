from django import forms
from .models import*

class TuristaForm(forms.ModelForm):
    class Meta:
        model = Turista
        fields = [
            'identificacion',
            'nombre',
            'correo',
        ]
        labels = {
            'identificacion': 'Identificación',
            'nombre': 'Nombre',
            'correo': 'Correo',
        }

class GuiaForm(forms.ModelForm):
    class Meta:
        model = Guia
        fields = [
            'identificacion',
            'nombre',
            'correo',
            'direccion',
        ]
        labels = {
            'identificacion': 'Identificación',
            'nombre': 'Nombre',
            'correo': 'Correo',
            'direccion': 'Dirección'
        }

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = [
            'lugar',
            'descripcion',
            'fecha',
            'cupos',
        ]
        labels = {
            'lugar': 'Lugar',
            'descripcion': 'Descripcion',
            'fecha': 'Fecha',
            'cupos': 'Cupos',
        }
