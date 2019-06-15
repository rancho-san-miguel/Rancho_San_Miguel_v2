from django import forms
from .models import *


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
            'tipo',
            # 'galeria_venta',
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
            'tipo':'Tipo de bovino',
            # 'galeria_venta':'Agregar a la ventana de venta',
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
            'tipo':forms.Select(attrs={'class': 'form-control'}),
            # 'galeria_venta': forms.CheckboxInput(),
            'img': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'img2': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }

class Ganado_Venta_form(forms.ModelForm):
    class Meta:
        model = Ganado
        fields = {
            'galeria_venta',
            'costo',
        }
        labels = {
            'galeria_venta': 'Marcar para poner en venta',
            'costo':'Costo total de la venta $',
        }
        widgets = {
            'galeria_venta': forms.CheckboxInput(),
            'costo':forms.TextInput(attrs={'class': 'form-control','placeholder':''}),
        }

class Ganado_Venta_form2(forms.ModelForm):
    class Meta:
        model = Ganado
        fields = {
            'galeria_venta',
            'costo',
        }
        labels = {
            'galeria_venta': 'Marcar para poner en venta',
            'costo':'Costo total de la venta $',
        }
        widgets = {
            'galeria_venta': forms.CheckboxInput(),
            'costo':forms.TextInput(attrs={'class': 'form-control','placeholder':''}),
        }


class Ganado2_Form(forms.ModelForm):
    class Meta:
        model = Ganado_sin_registro
        fields = {
            'nombre',
            'arete',
            'sexo',
            'propietario',
            # 'arete_padre',
            'arete_madre',
            'f_nacimiento',
            'peso_nacimiento',
            'localizacion_fierro',
            # 'galeria_venta',
            'img',
            'img2',

        }
        labels = {
            'nombre':'Nombre',
            'arete':'Arete',
            'sexo':'Sexo',
            'propietario':'Propietario',
            # 'arete_padre':'Arete del padre',
            'arete_madre':'Arete de la madre',
            'f_nacimiento':'Fecha de nacimiento',
            'peso_nacimiento':'Peso al nacer',
            'localizacion_fierro':'Fierro',
            # 'galeria_venta':'Agregar a la ventana de venta',
            'img':'Foto',
            'img2': 'Foto2',
        }


        widgets = {

            'nombre':forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el nombre del bovino'}),
            'arete':forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el arete del bovino'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'propietario': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del propietario'}),
            # 'arete_padre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el arete del padre'}),
            'arete_madre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el arete de la madre'}),
            'f_nacimiento':forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
            'peso_nacimiento':forms.TextInput(attrs={'class': 'form-control','placeholder':'Peso de nacimiento'}),
            'localizacion_fierro':forms.TextInput(attrs={'class': 'form-control','placeholder':'Localización del fierro'}),
            # 'galeria_venta': forms.CheckboxInput(),
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

class Notificaciones_Update_form(forms.ModelForm):
    class Meta:
        model = Notificaciones
        fields = {
            'estado',
        }
        labels = {
            'estado': 'Marcar como leido',
        }
        widgets = {
            'estado': forms.CheckboxInput(),
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
            #'total_compra',
            'fecha',
            'vendedor',
        }

        labels = {
            'cantidad': 'Cantidad',
            'precio_unidad': 'Precio unidad $',
            #'total_compra': 'Total compra $',
            'fecha':'Fehca',
            'vendedor':'Vendedor',
        }

        widgets = {
            'cantidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cantidad de cerdos'}),
            'precio_unidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Precio $'}),
            #'total_compra': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total $'}),
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





class DeudoresAcredoresForm(forms.ModelForm):
    class Meta:
        model = DeudoresAcreedores
        fields = {
            'nombre',
            'tipo',
            'motivo',
            'deuda',
            'fecha',
        }

        labels = {
            'nombre': 'Nombre',
            'tipo': 'Tipo',
            'motivo': 'Motivo',
            'deuda': 'Deuda $',
            'fecha': 'Fecha',
         }

        widgets = {

            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nombre'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Motivo'}),
            'deuda': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Deuda $'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }


################################################################################
################################################################################
################################################################################
class Registro_Agricola_form(forms.ModelForm):
    class Meta:
        model = InventarioAgricola
        fields = {
            'cultivo',
            'unidad_medida',
            'cantidad',
            'precio',
        }
        labels = {
            'cultivo':'Ingresa el nombre del producto',
            'unidad_medida':'Unidad de medida',
            'cantidad':'Ingresa la cantidad',
            'precio':'Ingresa el precio $',
        }
        widgets = {
            'cultivo':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del producto Ej. Maíz, Frijol'}),
            'unidad_medida': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
        }
################################################################################
################################################################################
################################################################################


class MovDeudoresAcredoresForm(forms.ModelForm):
    class Meta:
        model = MovimientosDya
        fields = {
            'no',
            'descripcion',
            'deuda',
            'fecha',
        }

        labels = {
            'no': 'Confirma el nombre',
            'descripcion': 'Descripcion',
            'deuda': 'Deuda $',
            'fecha': 'Fecha',
         }

        widgets = {
            'no': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Movimiento'}),
            'deuda': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad $'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }

class GastosForm(forms.ModelForm):
    class Meta:
        model = Gastos
        fields = {
            'tipo',
            'motivo',
            'monto',
            'img',
            'fecha',

        }

        labels = {
            'tipo': 'Tipo',
            'motivo': 'Descripcion',
            'monto': 'Monto',
            'img': 'Imagen',
            'fecha': 'Fecha',
            }

        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion de la compra'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total $'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
            }



###########################################################################################################
###########################################################################################################
#En produccion
###########################################################################################################
###########################################################################################################

class En_Proceso_form(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = {
            'cultivo',
            'hectareas',
            'cantidad',
            'ciclo',
            'fecha_inicio',
        }
        labels = {
            'cultivo': 'Cultivo a sembrar',
            'hectareas': 'Hectáreas a sembrar',
            'cantidad':'Cantidad de semilla a sembrar',
            'ciclo':'Selecciona el ciclo de siembra',
            'fecha_inicio':'Fecha de inicio'
        }
        widgets = {
            'Cultivo':forms.Select(attrs={'class': 'form-control'}),
            'hectareas':forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad':forms.TextInput(attrs={'class': 'form-control'}),
            'ciclo':forms.Select(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
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
            'total_venta':'Total de la venta $',
            'comprador':'Comprador',
            'fecha':'Fecha de la venta',
        }
        widgets = {
            'descripcion_venta': forms.Textarea(attrs={'class': 'form-control'}),
            'total_venta': forms.TextInput(attrs={'class': 'form-control','placeholder':'Total del bovino $'}),
            'comprador': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del comprador'}),
            'fecha': forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
        }
###########################################################################################################
###########################################################################################################
#Galeria
###########################################################################################################
###########################################################################################################

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

#Venta de leche form by Miku


class Ventas_Leche_form(forms.ModelForm):
    class Meta:
        model = VentaLeche
        fields = {
            'cantidad',
            'precio',
            # 'total',
            'fecha',
        }
        labels = {
            'cantidad':'Cantidad',
            'precio':'Precio $',
            # 'total':'Total',
            'fecha':'Fecha',
        }
        widgets = {
            'cantidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cantidad Litros de Leche'}),
            'precio': forms.TextInput(attrs={'class': 'form-control','placeholder':'Costo $'}),
            # 'total': forms.TextInput(attrs={'class': 'form-control','placeholder':'Costo ejemplo: 15.20'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }



class ControlVentaGanado_form(forms.ModelForm):
    class Meta:
        model = ControlVentaGanado
        fields = {
            'descripcion_venta',
            # 'tipo',
            'total_venta',
            'comprador',
            'fecha',
        }
        labels = {
            'descripcion_venta':'Descripción de la venta',
            # 'tipo':'Tipo de bovino',
            'total_venta':'Total de la venta $',
            'comprador':'Comprador',
            'fecha':'Fecha de la venta',
        }
        widgets = {
            'descripcion_venta': forms.Textarea(attrs={'class': 'form-control'}),
            # 'tipo':forms.Select(attrs={'class': 'form-control'}),
            'total_venta': forms.TextInput(attrs={'class': 'form-control','placeholder':'Total del bovino'}),
            'comprador': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del comprador'}),
            'fecha': forms.SelectDateWidget(years=range(y.year-20,y.year+2),attrs={'class': 'form-control snps-inline-select'}),
        }

class Planes_form(forms.ModelForm):
    class Meta:
        model = Planes
        fields = {
            'fecha'
        }
        labels = {
            'fecha':'Fecha de la planeación'
        }
        widgets = {
            'fecha':forms.SelectDateWidget(years=range(y.year,y.year),attrs={'class': 'form-control snps-inline-select'}),
        }

class Plan_Agro_form(forms.ModelForm):
    class Meta:
        model = PlaneacionAgricola
        fields = {
            'ciclo',
            'cultivo',
            'hectareas',
            'costo',
            # 'produccion_estimada',
            'cantidad',
            # 'total',
        }
        labels = {
            'ciclo': 'Ciclo',
            'cultivo': 'Cultivo',
            'hectareas': 'Hectáreas',
            'costo': 'Costo $',
            # 'produccion_estimada': 'Producción estimada',
            'cantidad': 'Cantidad',
            # 'total': 'Total',
        }
        widgets = {
            'ciclo': forms.Select(attrs={'class': 'form-control'}),
            'cultivo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del cultivo'}),
            'hectareas': forms.TextInput(attrs={'class': 'form-control','placeholder':'Numero de hectáreas'}),
            'costo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el costo de las hectáreas $'}),
            # 'produccion_estimada': forms.TextInput(attrs={'class': 'form-control','placeholder':'Estimación de la producción'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cantidad a producir'}),
            # 'total': forms.TextInput(attrs={'class': 'form-control','placeholder':'Total'}),
        }


class Plan_Bovino_form(forms.ModelForm):
    class Meta:
        model = PlaneacionBovina
        fields = {
            'tipo_ganado',
            'hato',
            'venta',
            'precio',
            # 'ingreso_anual',
        }
        labels = {
            'tipo_ganado': 'Tipo de ganado',
            'hato':'Hato',
            'venta':'Venta',
            'precio':'Precio $',
            # 'ingreso_anual': 'Ingreso anual',
        }
        widgets = {
            'tipo_ganado': forms.Select(attrs={'class': 'form-control'}),
            'hato': forms.TextInput(attrs={'class': 'form-control','placeholder':'Hato'}),
            'venta': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cantidad a vender'}),
            'precio': forms.TextInput(attrs={'class': 'form-control','placeholder':'Dame el precio $'}),
            # 'ingreso_anual': forms.TextInput(attrs={'class': 'form-control','placeholder':'0.0'}),
        }

class Plan_Leche_form(forms.ModelForm):
    class Meta:
        model = PlaneacionLeche
        fields = {
            'vacas_produccion',
            'produccion_promedio',
            'precio_litro',
            'dias',
            # 'ingreso_diario',
            # 'estimado_anual',
        }
        labels = {
            'vacas_produccion': 'Vacas en producción',
            'produccion_promedio':'Producción promedio de lts al dia',
            'precio_litro':'Precio por litro $',
            'dias':'Dias a estimar',
            # 'ingreso_diario':'Ingreso diario',
            # 'estimado_anual':'Estimado anual',
        }
        widgets = {
            'vacas_produccion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cantidad de vacas en producción'}),
            'produccion_promedio': forms.TextInput(attrs={'class': 'form-control','placeholder':'Producción promedio por todas las vacas'}),
            'precio_litro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Precio de la leche'}),
            'dias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de dias'}),
            # 'ingreso_diario':forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingreso diario'}),
            # 'estimado_anual':forms.TextInput(attrs={'class': 'form-control','placeholder':'Estimado anual'}),
        }


class Plan_Porcina_form(forms.ModelForm):
    class Meta:
        model = PlaneacionPorcina
        fields = {
            'cerdos',
            'lechones',
            'precio_venta',
            'precio_compra',
            # 'inversion',
            # 'ingresos',
        }
        labels = {
            'cerdos': 'Cerdos',
            'lechones': 'Lechones',
            'precio_venta': 'Precio de venta $',
            'precio_compra':'Precio de compra $',
            # 'inversion': 'Inversión',
            # 'ingresos':'Ingresos',
        }
        widgets = {
            'cerdos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de cerdos a vender'}),
            'lechones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de lechones a comprar'}),
            'precio_venta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Precio a la venta $'}),
            'precio_compra': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Precio de compra $'}),
            # 'inversion':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad a invertir'}),
            # 'ingresos':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantida de ingresos'}),
        }

class Proyeccion_Gastos_form(forms.ModelForm):
    class Meta:
        model = ProyeccionGastos
        fields = {
            'tipo_gasto',
            'descripcion',
            'cantidad',
        }
        labels = {
            'tipo_gasto': 'Tipo de gasto',
            'descripcion': 'Descripción',
            'cantidad': 'Costo $',
        }
        widgets = {
            'tipo_gasto': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Costo al año $'}),
        }



class VentaPorcino_form(forms.ModelForm):
    class Meta:
        model = VentasPorcinos
        fields = {
            'cantidad',
            'precio_unidad',
           # 'total_venta',
            'fecha',
            'comprador',
        }

        labels = {
            'cantidad': 'Cantidad',
            'precio_unidad': 'Precio unidad $',
           # 'total_venta': 'Total venta $',
            'fecha':'Fecha',
            'comprador':'Comprador',
        }

        widgets = {
            'cantidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cantidad de cerdos'}),
            'precio_unidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Precio $'}),
          #  'total_venta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total $'}),
            'fecha': forms.SelectDateWidget(years=range(y.year - 20, y.year + 2),attrs={'class': 'form-control snps-inline-select'}),
            'comprador': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comprador'}),
        }

#bitacora
class Bitacora_Ganado_form(forms.ModelForm):
    class Meta:
        model = ControlBitacoraGanado
        fields = {
            'bovino',
            'descripcion',
            'lugar',
            'fecha',
        }
        labels = {
            'bovino':'Bovino',
            'descripcion':'Descripcion',
            'lugar':'Lugar',
            'fecha':'Fecha',
        }
        widgets = {
            # 'bovino': forms.TextInput(attrs={'class': 'form-control'}),
            'bovino': forms.CheckboxSelectMultiple(),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }

#Inventario General
class Registro_NoAgricola_form(forms.ModelForm):
    class Meta:
        model = InventarioNoAgricola
        fields = {
            'articulo',
            'unidad_medida',
            'cantidad',
            'precio',
        }
        labels = {
            'articulo':'Ingresa el nombre del producto',
            'unidad_medida':'Unidad de medida',
            'cantidad':'Ingresa la cantidad',
            'precio':'Ingresa el precio $',
        }
        widgets = {
            'articulo':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del producto Ej. Maíz, Frijol'}),
            'unidad_medida': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CompraVentaAgricola_form(forms.ModelForm):
    class Meta:
        model = CompraVentaAgricola
        fields = {
            'cultivo',
            'comprador',
            'cantidad',
            'fecha',
        }
        labels = {
            'cultivo':'Confirma producto',
            'comprador': 'Nombre del comprador:',
            'cantidad':'Cantidad',
            'fecha':'Fecha'
        }
        widgets = {
            'cultivo':forms.Select(attrs={'class': 'form-control'}),
            'comprador': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }

class CompraVentaAgricola_form2(forms.ModelForm):
    class Meta:
        model = CompraVentaAgricola
        fields = {
            'precio',
            'cultivo',
            'comprador',
            'cantidad',
            'fecha',
        }
        labels = {
            'precio':'Precio de compra por unidad $:',
            'cultivo':'Confirma producto:',
            'comprador': 'Nombre del comprador:',
            'cantidad':'Cantidad',
            'fecha':'Fecha'
        }
        widgets = {
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'cultivo':forms.Select(attrs={'class': 'form-control'}),
            'comprador': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }

class CompraVentaAgricola_form3(forms.ModelForm):
    class Meta:
        model = CompraVentaAgricola
        fields = {
            'cultivo',
            'cantidad',
            'fecha',
        }
        labels = {
            'cultivo': 'Confirma producto:',
            'cantidad':'Cantidad',
            'fecha':'Fecha'
        }
        widgets = {
            'cultivo': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }

class CompraVentaNOAgricola_form(forms.ModelForm):
    class Meta:
        model = CompraVentaNoAgricola
        fields = {
            'articulo',
            'precio',
            'cantidad',
            'fecha',
        }
        labels = {
            'articulo': 'Confirma producto:',
            'precio':'Precio de la compra $',
            'cantidad':'Cantidad',
            'fecha':'Fecha'
        }
        widgets = {
            'articulo': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }

class CompraVentaNOAgricola_form2(forms.ModelForm):
    class Meta:
        model = CompraVentaNoAgricola
        fields = {
            'articulo',
            'cantidad',
            'fecha',
        }
        labels = {
            'articulo': 'Confirma producto:',
            'cantidad':'Cantidad',
            'fecha':'Fecha',
        }
        widgets = {
            'articulo': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }

class Produccion_form(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = {
            'produccion_obtenida',
            'fecha_final',
        }
        labels = {
            'produccion_obtenida':'Producción obtenida',
            'fecha_final': 'Fecha de finalizacion:',
        }
        widgets = {
            'produccion_obtenida': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_final': forms.SelectDateWidget(attrs={'class': 'form-control snps-inline-select'}),
        }

class Contacto_form(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = {
            'nombre',
            'direc',
            'telefono',
            'correo'
        }
        labels = {
            'nombre':'Nombre completo',
            'direc': 'Dirección',
            'telefono': 'Teléfono',
            'correo':'Correo electronico',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direc': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
        }