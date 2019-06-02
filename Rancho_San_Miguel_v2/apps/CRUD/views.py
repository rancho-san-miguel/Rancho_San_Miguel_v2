from django.shortcuts import render
from django.shortcuts import redirect, render

from .models import Ganado, ComprasPorcinos, InventarioPorcino,VentasPorcinos, ControlVentaGanado
from .models import Notificaciones, InventarioAgricola,MovimientosDya
from .models import Galeria , ControlGanado, ControlVentaGanado, Produccion, ComprasPorcinos, DeudoresAcreedores, Gastos

from .forms import Ganado_Form,Notificaciones_form, GaleriaForm
from .forms import Control_ganado_form,MovDeudoresAcredoresForm,GastosForm, ControlVentaGanado_form, En_Proceso_form
from .forms import Ganado_Form,Notificaciones_form, GaleriaForm, CompraPorcino_form,VentaPorcino_form,DeudoresAcredoresForm
from .forms import Control_ganado_form, ControlVentaGanado_form
from .forms import Ganado_Form,Notificaciones_form, GaleriaForm, CompraPorcino_form


from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime

from django.contrib.auth.models import User, Group
from .forms import SignUpForm
from django.contrib import messages



class Bovino_Create(CreateView):
    model = Ganado
    form_class = Ganado_Form
    template_name = 'RegBov/regbov_form.html'
    # success_url = reverse_lazy('bovino_crear')#Cambiar a list
    success_url = reverse_lazy('bovino_list')

class Bovino_List(ListView):
    queryset = Ganado.objects.all()
    # queryset = Ganado.objects.exclude(estado='Vendida').order_by('id')
    # queryset = GANADO.objects.exclude(estado='Vendida')
    template_name = 'RegBov/regbov_list.html'
    paginate_by = 5

class Bovino_Show(DetailView):
    model = Ganado
    template_name = 'RegBov/regbov_show.html'

class Bovino_Update(UpdateView):
    model = Ganado
    form_class = Ganado_Form
    template_name = 'RegBov/regbov_form.html'
    success_url = reverse_lazy('bovino_list')

class Bovino_Delete(DeleteView):
    model = Ganado
    template_name = 'RegBov/regbov_delete.html'
    success_url = reverse_lazy('bovino_list')

def Bovino_Search(request):
    query = Ganado.objects.all()
    # query_filter = Ganado_filter(request.GET, queryset=query)
    if request.method == 'POST':
        fecha = request.POST['caja']
        fecha1 = fecha
        fecha = str(fecha+"-01-01")
        fecha2 = str(fecha1+"-12-31")
        print("FEHCA-------------********************-------------", fecha)
        print("FEHCA-------------********************-------------", fecha2)
        # query = Ganado.objects.get(f_nacimiento=)
        query = Ganado.objects.filter(f_nacimiento__range=[fecha,fecha2])
    dic = {
        'object_list':query,
    }
    return render(request, 'RegBov/regbov_list.html', dic)

def Bovino_update_ventas_create(request, pk):
    query = Ganado.objects.get(pk=pk)
    if request.method == 'POST':
        form = ControlVentaGanado_form(request.POST)
        if form.is_valid():
            form.save()
            query.delete()
        return redirect('venta_list')
    else:
        form = ControlVentaGanado_form()
    dic = {
        'datos':query,
        'form':form,
    }

    return render(request, 'RegBov/regbov_ventas_form.html', dic)

class Venta_Bovino_List(ListView):
    queryset = ControlVentaGanado.objects.all()
    template_name = 'Ventas/ventas_bovino_list.html'
    paginate_by = 5

class Venta_Bovino_Show(DetailView):
    model = ControlVentaGanado
    template_name = 'Ventas/ventas_bovino_show.html'


#----------------------------------------------------------------------
class Controlg_Create(CreateView):
    model = ControlGanado
    form_class = Control_ganado_form
    template_name = 'control_ganado/control_form.html'
    success_url = reverse_lazy('control_list')

class Controlg_List(ListView):
    queryset = ControlGanado.objects.all()
    template_name = 'control_ganado/control_list.html'
    paginate_by = 5

class Controlg_Show(DetailView):
    model = ControlGanado
    template_name = 'control_ganado/control_show.html'

class Controlg_Update(UpdateView):
    model = ControlGanado
    form_class = Control_ganado_form
    template_name = 'control_ganado/control_form.html'
    success_url = reverse_lazy('control_list')
class Controlg_Delete(DeleteView):
    model = ControlGanado
    template_name = 'control_ganado/control_delete.html'
    success_url = reverse_lazy('control_list')
#---------------------------------------------------------------------------------------------------------------------
########Produccion
"En proceso/que esta cultivado"
class En_Proceso_Create(CreateView):
    model = Produccion
    form_class = En_Proceso_form
    template_name = 'Producciones/cultivo_en_proceso_form.html'
    success_url = reverse_lazy('cultivo_en_proceso_list')

class En_Proceso_List(ListView):
    queryset = Produccion.objects.all()
    template_name = 'Producciones/cultivo_en_proceso_list.html'
    paginate_by = 5

class En_Proceso_Update(UpdateView):
    model = Produccion
    form_class = En_Proceso_form
    template_name = 'Producciones/cultivo_en_proceso_form.html'
    success_url = reverse_lazy('cultivo_en_proceso_list')

class En_Proceso_Delete(DeleteView):
    model = Produccion
    template_name = 'Producciones/cultivo_en_proceso_delete.html'
    success_url = reverse_lazy('cultivo_en_proceso_list')

class En_Proceso_Show(DetailView):
    model = Produccion
    template_name = 'Producciones/cultivo_en_proceso_show.html'

def En_Proceso_Fin(request, pk):
    query1 = Produccion.objects.get(pk=pk)
    query3 = InventarioAgricola.objects.get(cultivo=query1.cultivo)
    print ("QUE ES ESTO**********************************************************************************", query3)
    if request.method == 'POST':
        n1 = int(request.POST['produccion_obtenida'])
        n3 = request.POST['fecha_final']
        Produccion.objects.filter(pk=pk).update(produccion_obtenida=n1,fecha_final=n3)

        query3.cantidad = n1 + query3.cantidad
        return redirect('cultivo_en_proceso_list')

    dic = {
        'object':query1,
    }

    return render(request, 'Producciones/finalizar_produccion.html', dic)
#........................................
#
def ordenar_producciones(request):
    query = Produccion.objects.all()
    if request.method == 'POST':
        dime = request.POST['ordenar_produccion']
        if dime=="ptodos":
            pass
        elif dime=="pfinal":
            query = Produccion.objects.filter(fecha_final__isnull=False)
        elif dime == "pproce":
            query = Produccion.objects.filter(fecha_final__isnull=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(query, 10)
    try:
        pros = paginator.page(page)
    except PageNotAnInteger:
        pros = paginator.page(1)
    except EmptyPage:
        pros = paginator.page(paginator.num_pages)
    # query_filter = Ganado_filter(request.GET, queryset=query)
    dic = {
        'object_list': pros,
    }

    return render(request, 'Producciones/cultivo_en_proceso_list.html', dic)
# ........................................................
"Notificaciones"

def Notificaciones_function():
    ahora = datetime.now()
    return ahora

def Query_Notificaciones(request):
    Fecha_Actual = Notificaciones_function()

    day = Fecha_Actual.day
    month = Fecha_Actual.month
    year = Fecha_Actual.year

    if int(day) <= 9:
        day = "0"+str(day)

    if int(month) <= 9:
        month = "0"+str(month)

    var = str(year)+"-"+str(month)+"-"+str(day)

    query = Notificaciones.objects.filter(fecha=var)

    dic = {

        'form':query,
    }
    return render(request, 'Ventas/calis.html', dic)
    # return render(request, 'base/base.html',dic)

class Notificaciones_Listar(ListView):
    queryset = Notificaciones.objects.all()
    template_name = 'Notificaciones/notificaciones_list.html'
    paginate_by = 5


class Notificaciones_Create(CreateView):
    model = Notificaciones
    form_class = Notificaciones_form
    template_name = 'Notificaciones/notifi_form.html'
    success_url = reverse_lazy('index2')
#----------------------------------------------------------------------------------------------------------
"Galeria"
class GaleriaCreate(CreateView):
    model = Galeria
    form_class = GaleriaForm
    template_name = 'Galeria/galeria_form.html'
    success_url = reverse_lazy('galeria_list')

class GaleriaList(ListView):
    queryset = Galeria.objects.all()
    template_name = 'Galeria/galeria_list.html'
    paginate_by = 5

class GaleriaDetail(DetailView):
    model = Galeria
    template_name = 'Galeria/galeria_show.html'

class GaleriaDelete(DeleteView):
    model = Galeria
    template_name =  'Galeria/galeria_delete.html'
    success_url = reverse_lazy('galeria_list')

class GaleriaUpdate(UpdateView):
    model = Galeria
    form_class = GaleriaForm
    template_name = 'Galeria/galeria_form.html'
    success_url = reverse_lazy('galeria_list')

class GaleriaList2(ListView):
    queryset = Galeria.objects.all()
    template_name = 'home/portfolio.html'
#-------------------------------------------------------------------------------------------------------------
"porcinos"
class Compra_Cerdos_List(ListView):
    queryset = ComprasPorcinos.objects.all()
    template_name = 'Ventas/ventas_cerdos_list.html'
    paginate_by = 5

def Compra_Cerdos_Create(request):
    query = InventarioPorcino.objects.get_or_create(cantidad='0')
    var2 = InventarioPorcino.objects.all()
    if request.method == 'POST':
        form = CompraPorcino_form(request.POST)
        if form.is_valid():
            var = form.save()
            suma = int(var2[0].cantidad)+int(var.cantidad)

            var3 = InventarioPorcino.objects.get(pk=var2[0].id)
            var3.cantidad = suma
            var3.save()

        return redirect('cerdos_list')
    else:
        form = CompraPorcino_form()
    dic = {
        'form':form,
    }
    return render(request, 'Ventas/ventas_cerdos_form.html', dic)

#################pppp
###############################
class DeudoresAcreedoresCreate(CreateView):
    model = DeudoresAcreedores
    form_class = DeudoresAcredoresForm
    template_name = 'DeudoreAcreedores/Deudore_Acreedores_form.html'
    success_url = reverse_lazy('Deudore_Acreedores_list')

class DeudoresAcreedoresList(ListView):
    queryset = DeudoresAcreedores.objects.all()
    template_name = 'DeudoreAcreedores/Deudore_Acreedores_list.html'
    paginate_by = 5

class DeudoresAcreedoresDetail(DetailView):
    model = DeudoresAcreedores
    template_name = 'DeudoreAcreedores/Deudore_Acreedores_show.html'

class DeudoresAcreedoresDelete(DeleteView):
    model = DeudoresAcreedores
    template_name =  'DeudoreAcreedores/Deudore_Acreedores_delete.html'
    success_url = reverse_lazy('Deudore_Acreedores_list')

class DeudoresAcreedoresUpdate(UpdateView):
    model = DeudoresAcreedores
    form_class = DeudoresAcredoresForm
    template_name = 'DeudoreAcreedores/Deudore_Acreedores_form.html'
    success_url = reverse_lazy('Deudore_Acreedores_list')





def Abonos(request, pk):
    query1 = DeudoresAcreedores.objects.get(pk=pk)
    # print("Cantidad-----------------------------------------------------------------------------")
    # print(query1.cantidad)
    if request.method == 'POST':
        form = MovDeudoresAcredoresForm(request.POST)
        if form.is_valid():
            var = form.save()
            var.deuda

            if int(query1.deuda) >= int(var.deuda):
                query1.deuda = int(query1.deuda) - int(var.deuda)
                query1.save()
                var.save()
            else:
                messages.info(request, 'Error. No cuentas con el suficiente inventario para venderlo')
                var.delete()
        return redirect('Abono_list')
    else:
        form = MovDeudoresAcredoresForm()

    dic = {
        'form':query1,
        'form2':form,
    }
    return render(request, 'DeudoreAcreedores/AbonosCrear.html', dic)


class AbonosList(ListView):
    queryset = MovimientosDya.objects.all()
    template_name = 'DeudoreAcreedores/AbonosList.html'
    paginate_by = 5

###############################
##################################

class Venta_Cerdos_List(ListView):
    queryset = VentasPorcinos.objects.all()
    template_name = 'Compras/Compras_cerdos_list.html'
    paginate_by = 5

def Venta_Cerdos_Create(request):
    query = InventarioPorcino.objects.get_or_create(cantidad='0')
    var2 = InventarioPorcino.objects.all()
    if request.method == 'POST':
        form = VentaPorcino_form(request.POST)
        if form.is_valid():
            var = form.save()
            suma = int(var2[0].cantidad)-int(var.cantidad)

            var3 = InventarioPorcino.objects.get(pk=var2[0].id)
            var3.cantidad = suma
            var3.save()

        return redirect('cerdos_listVenta')
    else:
        form = VentaPorcino_form()
    dic = {
        'form':form,
    }
    return render(request, 'Compras/Compras_cerdos_form.html', dic)


###########################
###########################
class HistoriaCreate(CreateView):
    model = Gastos
    form_class = GastosForm
    template_name = 'Compras/Historial_Compras_form.html'
    success_url = reverse_lazy('Historial_Compras_list')

class HistoriaList(ListView):
    queryset = Gastos.objects.all()
    template_name = 'Compras/Historial_Compras_list.html'
    paginate_by = 5

class HistoriaDetail(DetailView):
    model = Gastos
    template_name = 'Compras/Historial_Compras_show.html'

class HistoriaDelete(DeleteView):
    model = Gastos
    template_name =  'Compras/Historial_Compras_delete.html'
    success_url = reverse_lazy('Historial_Compras_list')

class HistoriaUpdate(UpdateView):
    model = Gastos
    form_class = GastosForm
    template_name = 'Compras/Historial_Compras_form.html'
    success_url = reverse_lazy('Historial_Compras_list')


###########################
###########################

#----------------------------------------------------------------------------------------------------------
"Usuarios"
class CrearUsuario(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/usuario_create.html'
    success_url = reverse_lazy('listar_usuario')

class ListarUsuarios(ListView):
    # queryset = User.objects.exclude(username="admin").all()
    queryset = User.objects.all()
    template_name = 'registration/usuario_list.html'
    paginate_by = 5

def AddGrupos(request, pk):
    usuario = User.objects.get(pk=pk)
    if request.method == 'POST':
        usuario.groups.clear()
        usuario.groups.clear()
        try:
            op1 = request.POST['caja1']
            grupos = Group.objects.get(name="Galeria")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op2 = request.POST['caja2']
            grupos = Group.objects.get(name="Notificaciones")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op3 = request.POST['caja3']
            grupos = Group.objects.get(name="Ganaderia")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op4 = request.POST['caja4']
            grupos = Group.objects.get(name="Porcinos")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op5 = request.POST['caja5']
            grupos = Group.objects.get(name="Agricultura")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op6 = request.POST['caja6']
            grupos = Group.objects.get(name="Ganado")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op7 = request.POST['caja7']
            grupos = Group.objects.get(name="GanadoAdd")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op8 = request.POST['caja8']
            grupos = Group.objects.get(name="GanadoDel")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op8 = request.POST['caja9']
            grupos = Group.objects.get(name="GanadoVen")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op8 = request.POST['caja10']
            grupos = Group.objects.get(name="GanadoUpd")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op9 = request.POST['caja11']
            grupos = Group.objects.get(name="AgriculturaAdd")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op9 = request.POST['caja12']
            grupos = Group.objects.get(name="HisVenBov")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op9 = request.POST['caja13']
            grupos = Group.objects.get(name="Bitacora")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op9 = request.POST['caja14']
            grupos = Group.objects.get(name="Leche")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op9 = request.POST['caja15']
            grupos = Group.objects.get(name="Control")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op9 = request.POST['caja16']
            grupos = Group.objects.get(name="Produccion")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op9 = request.POST['caja17']
            grupos = Group.objects.get(name="Almacen")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op9 = request.POST['caja18']
            grupos = Group.objects.get(name="HisVenAgro")
            usuario.groups.add(grupos)
        except:
            pass
        try:
            op9 = request.POST['caja19']
            grupos = Group.objects.get(name="HisRet")
            usuario.groups.add(grupos)
        except:
            pass

        return redirect('listar_usuario')

    dic = {
        'form':usuario,
    }
    return render(request,'registration/Add_Groups.html', dic)