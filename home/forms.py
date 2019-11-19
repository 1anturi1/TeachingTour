from django import forms
from .models import*

class TuristaForm(forms.ModelForm):
    class Meta:
        model = Turista
        fields = [
            'identificacion',
            'nombre',
            'correo',
            'idioma',
        ]
        labels = {
            'identificacion': 'Identificación',
            'nombre': 'Nombre',
            'correo': 'Correo',
            'idioma': 'Idioma'
        }

class GuiaForm(forms.ModelForm):
    class Meta:
        model = Guia
        fields = [
            'identificacion',
            'nombre',
            'correo',
            'idioma',
        ]
        labels = {
            'identificacion': 'Identificación',
            'nombre': 'Nombre',
            'correo': 'Correo',
            'idioma': 'Idioma'
        }

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = [
            'lugar',
            'descripcion',
            'fecha',
            'cupos',
            'imagen',
        ]
        labels = {
            'lugar': 'Lugar',
            'descripcion': 'Descripcion',
            'fecha': 'Fecha',
            'cupos': 'Cupos',
            'imagen': 'Imagen',
        }
