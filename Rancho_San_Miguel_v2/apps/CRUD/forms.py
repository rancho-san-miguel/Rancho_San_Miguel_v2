from django import forms
from .models import Ganado


import datetime

y = datetime.datetime.now()

class Ganado_Form(forms.ModelForm):
    # fecha_nacimiento=forms.DateTimeField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Ganado
        fields = {
            'nombre',
            'arete',
            'siniga',
            'sexo',
            'propietario',
            'ganadera',
            'arete_padre',
            'arete_madre',
            'f_nacimiento',
            'tipo_nacimiento',
            'tipo_parto',
            'potrero',
            'peso_nacimiento',
            'localizacion_fierro',
            'localizacion_tatuaje',
            'estado',
            'galeria_venta',
            'img',
            'img2',

        }
        labels = {
            'nombre':'Nombre',
            'arete':'Arete',
            'siniga':'Siniga',
            'sexo':'Sexo',
            'propietario':'Propietario',
            'ganadera':'Ganadera',
            'arete_padre':'Arete del padre',
            'arete_madre':'Arete de la madre',
            'f_nacimiento':'Fecha de nacimiento',
            'tipo_nacimiento':'Tipo de nacimiento',
            'tipo_parto':'Tipo de parto',
            'potrero':'Potrero',
            'peso_nacimiento':'Peso al nacer',
            'localizacion_fierro':'Fierro',
            'localizacion_tatuaje':'Tatuaje localización',
            'estado':'Estado',
            'galeria_venta':'Agregar a la ventana de venta',
            'img':'Foto',
            'img2': 'Foto2',
        }


        widgets = {

            'nombre':forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el nombre del bovino'}),
            'arete':forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el codigo del arete del bovino'}),
            'siniga': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame la siniga del bovino'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el sexo'}),
            'propietario': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el prop'}),
            'ganadera': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame ganad'}),
            'arete_padre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el are p'}),
            'arete_madre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el are m'}),
            'f_nacimiento':forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
            'tipo_nacimiento':forms.TextInput(attrs={'class': 'form-control','placeholder':'tip nac'}),
            'tipo_parto':forms.TextInput(attrs={'class': 'form-control','placeholder':'tip part'}),
            'potrero':forms.TextInput(attrs={'class': 'form-control','placeholder':'potre'}),
            'peso_nacimiento':forms.TextInput(attrs={'class': 'form-control','placeholder':'peso nac'}),
            'localizacion_fierro':forms.TextInput(attrs={'class': 'form-control','placeholder':'loc fierro'}),
            'localizacion_tatuaje':forms.TextInput(attrs={'class': 'form-control','placeholder':'loc tatu'}),
            'estado':forms.TextInput(attrs={'class': 'form-control','placeholder':'estado'}),
            'galeria_venta': forms.CheckboxInput(),
            'img': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'img2': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }