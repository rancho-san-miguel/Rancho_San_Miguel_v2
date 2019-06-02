from django import forms
from .models import Ganado, Notificaciones, Galeria,ComprasPorcinos,ControlGanado, ControlVentaGanado


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
            'localizacion_tatuaje':'Tatuaje en oreja',
            'estado':'Estado',
            'galeria_venta':'Agregar a la ventana de venta',
            'img':'Foto',
            'img2': 'Foto2',
        }


        widgets = {

            'nombre':forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el nombre del bovino'}),
            'arete':forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el arete del bovino'}),
            'siniga': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame la siniga del bovino'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'propietario': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del propietario'}),
            'ganadera': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame ganadera'}),
            'arete_padre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el arete del padre'}),
            'arete_madre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el arete de la madre'}),
            'f_nacimiento':forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
            'tipo_nacimiento':forms.Select(attrs={'class': 'form-control'}),
            'tipo_parto':forms.Select(attrs={'class': 'form-control'}),
            'potrero':forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el potrero'}),
            'peso_nacimiento':forms.TextInput(attrs={'class': 'form-control','placeholder':'Peso de nacimiento'}),
            'localizacion_fierro':forms.TextInput(attrs={'class': 'form-control','placeholder':'Localización del fierro'}),
            'localizacion_tatuaje':forms.Select(attrs={'class': 'form-control'}),
            'estado':forms.Select(attrs={'class': 'form-control'}),
            'galeria_venta': forms.CheckboxInput(),
            'img': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'img2': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }

class Notificaciones_form(forms.ModelForm):
    class Meta:
        model = Notificaciones
        fields = {
            'descripcion',
            'fecha',
        }
        labels = {
            'descripcion':'Descripción',
            'fecha':'Fecha del evento',
        }
        widgets = {
            'descripcion':forms.Textarea(attrs={'class': 'form-control','placeholder':'Descripción de las actividades a realizar'}),
            'fecha':forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }

class SignUpForm(UserCreationForm):
    # password1 = forms.CharField()
    # password2 = forms.CharField()
    class Meta(UserCreationForm):
        model = User

        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email')
        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            # 'username':forms.CharField(help_text='First name'),
            'first_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electronico'}),
            'password1' : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'password2':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña otra vez'}),
        }

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = {
            'nombre',
            'img',
        }

        labels = {
            'nombre': 'Nombre',
            'img': 'Imagen',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Titulo de la imagen'}),
            'img': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }

class CompraPorcino_form(forms.ModelForm):
    class Meta:
        model = ComprasPorcinos
        fields = {
            'cantidad',
            'precio_unidad',
            'total_compra',
            'fecha',
            'vendedor',
        }

        labels = {
            'cantidad': 'Cantidad',
            'precio_unidad': 'Precio unidad',
            'total_compra': 'Total compra',
            'fecha':'Fehca',
            'vendedor':'Vendedor',
        }

        widgets = {
            'cantidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cantidad de cerdos'}),
            'precio_unidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Precio'}),
            'total_compra': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total'}),
            'fecha': forms.SelectDateWidget(years=range(y.year - 20, y.year + 2),attrs={'class': 'form-control snps-inline-select'}),
            'vendedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendedor'}),
        }

class Control_ganado_form(forms.ModelForm):
    class Meta:
        model = ControlGanado
        fields = {
            'arete',
            'motivo',
            'descripcion',
            'lugar',
            'fecha',
        }
        labels = {
            'arete':'Arete',
            'motivo': 'Motivo',
            'descripcion':'Descripción',
            'lugar':'Lugar',
            'fecha':'Fecha',
        }
        widgets = {
            'arete': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
        }


class ControlVentaGanado_form(forms.ModelForm):
    class Meta:
        model = ControlVentaGanado
        fields = {
            'descripcion_venta',
            'total_venta',
            'comprador',
            'fecha',
        }
        labels = {
            'descripcion_venta':'Descripción de la venta',
            'total_venta':'Total de la venta',
            'comprador':'Comprador',
            'fecha':'Fecha de la venta',
        }
        widgets = {
            'descripcion_venta': forms.Textarea(attrs={'class': 'form-control'}),
            'total_venta': forms.TextInput(attrs={'class': 'form-control','placeholder':'Total del bovino'}),
            'comprador': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del comprador'}),
            'fecha': forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
        }