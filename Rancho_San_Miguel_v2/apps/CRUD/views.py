from django.shortcuts import render
from django.shortcuts import redirect, render

from .models import *
from .forms import *


from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime

from django.contrib.auth.models import User, Group
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

def Bovino_Galeria_Venta_List(request):
    query = Ganado.objects.filter(galeria_venta=True).exclude(estado='Vendida').order_by('id')
    dic = {
        'object_list':query,
    }
    # return render(request, 'GaleriaVentas/calis.html', dic)
    return render(request, 'home/portfolio2.html', dic)

def Bovino_Galeria_Venta_Show(request,pk):
    query = Ganado.objects.get(pk=pk)
    dic = {
        'form':query,
    }
    return render(request, 'home/detalles.html', dic)

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
            var = form.save()
            var.tipo = query.tipo
            var.save()
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
        query3.save()
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

    query = Notificaciones.objects.filter(fecha=var).update(estado=False)

    query2 = Notificaciones.objects.filter(estado=False)

    dic = {

        'form':query2,
    }
    return render(request, 'Ventas/calis.html', dic)
    # return render(request, 'base/base.html',dic)

class Notificaciones_Listar(ListView):
    queryset = Notificaciones.objects.all()
    template_name = 'Notificaciones/notificaciones_list.html'
    paginate_by = 5

class Notificaciones_Update(UpdateView):
    model = Notificaciones
    form_class = Notificaciones_Update_form
    template_name = 'Notificaciones/notificaciones_update.html'
    success_url = reverse_lazy('notificacion_listar')


class Notificaciones_Create(CreateView):
    model = Notificaciones
    form_class = Notificaciones_form
    template_name = 'Notificaciones/notifi_form.html'
    success_url = reverse_lazy('index2')

#----------------------------------------------------------------------------------------------------------
"Inventario Agicola"

class InventarioA_List(ListView):
    queryset = InventarioAgricola.objects.all()
    template_name = 'Inventario_agricola/inventario_agricola_list.html'
    paginate_by = 5

class InventarioA_Create(CreateView):
    model = InventarioAgricola
    form_class = Registro_Agricola_form
    template_name = 'Inventario_agricola/inventario_agricola_form.html'
    success_url = reverse_lazy('inventario_list')

class InventarioA_Update(UpdateView):
    model = InventarioAgricola
    form_class = Registro_Agricola_form
    template_name = 'Inventario_agricola/inventario_agricola_form.html'
    success_url = reverse_lazy('inventario_list')

class InventarioA_Delete(DeleteView):
    model = InventarioAgricola
    template_name = 'Inventario_agricola/inventario_agricola_delete.html'
    success_url = reverse_lazy('inventario_list')

def Comprar_Vender_list(request):
    query = CompraVentaAgricola.objects.all()
    condi = 'holo'
    if request.method == 'POST':
        dime = request.POST['ordenar_registros']
        if dime=="ptodos":
            pass
        elif dime=="pfinal":
            query = CompraVentaAgricola.objects.filter(tipo='Venta')
            condi='venta'
        elif dime == "pproce":
            query = CompraVentaAgricola.objects.filter(tipo='Compra')
            condi='compra'
        elif dime == "retiros":
            query = CompraVentaAgricola.objects.filter(tipo='Baja')
            condi='baja'
        #else:
    page = request.GET.get('page', 1)
    paginator = Paginator(query, 10)
    try:
        pros = paginator.page(page)
    except PageNotAnInteger:
        pros = paginator.page(1)
    except EmptyPage:
        pros = paginator.page(paginator.num_pages)
    dic = {
        'object_list': pros,
        'con': condi,
    }

    return render(request, 'Inventario_agricola/compra_venta_list.html', dic)

def AVender_create(request, pk):
    query1 = InventarioAgricola.objects.get(cultivo=pk)
    # print ("QUE ES ESTO**********************************************************************************", query3)
    if request.method == 'POST':
        nombre = request.POST['nombre_vendedor']
        canti = int(request.POST['cantidad_comprar'])
        fecha = request.POST['fecha_final']
        b = CompraVentaAgricola(tipo='Venta', cultivo=query1, cantidad=canti, precio=(query1.precio * canti),
                                comprador=nombre, fecha=fecha)
        b.save()
        query1.cantidad = query1.cantidad - canti
        query1.save()
        return redirect('compraryvenderagricola')

    dic = {
        'object': query1,
    }
    return render(request, 'Inventario_agricola/AV_form.html', dic)


def Acomprar_create(request, pk):
    query1 = InventarioAgricola.objects.get(cultivo=pk)
    #print ("QUE ES ESTO**********************************************************************************", query3)
    if request.method == 'POST':
        nombre = request.POST['nombre_vendedor']
        canti = int(request.POST['cantidad_comprar'])
        precio = float(request.POST['precio_compra'])
        fecha = request.POST['fecha_final']
        b = CompraVentaAgricola(tipo='Compra', cultivo=query1, cantidad=canti, precio=(precio*canti),comprador=nombre, fecha=fecha)
        b.save()
        query1.cantidad = canti + query1.cantidad
        query1.save()
        return redirect('compraryvenderagricola')

    dic = {
        'object': query1,
    }
    return render(request, 'Inventario_agricola/AC_form.html', dic)

def Abaja_create(request, pk):
    query1 = InventarioAgricola.objects.get(cultivo=pk)
    # print ("QUE ES ESTO**********************************************************************************", query3)
    if request.method == 'POST':
        canti = int(request.POST['cantidad_comprar'])
        fecha = request.POST['fecha_final']
        b = CompraVentaAgricola(tipo='Baja', cultivo=query1, cantidad=canti, precio=0,
                                comprador="Rancho San Miguel", fecha=fecha)
        b.save()
        query1.cantidad = query1.cantidad - canti
        query1.save()
        return redirect('compraryvenderagricola')

    dic = {
        'object': query1,
    }
    return render(request, 'Inventario_agricola/AB_form.html', dic)



# class InventarioA_Update(UpdateView):
#     model = InventarioAgricola
#     form_class = Registro_Agricola_form
#     template_name = 'Inventario_agricola/inventario_agricola_form.html'
#     success_url = reverse_lazy('inventario_list')
#
# class InventarioA_Delete(DeleteView):
#     model = InventarioAgricola
#     template_name = 'Inventario_agricola/inventario_agricola_delete.html'
#     success_url = reverse_lazy('inventario_list')
#----------------------------------------------------------------------------------------------------------
#"Galeria"
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



#---------------------------------------------------------------------------------------------------------------------
"Venta de leche"

# class Venta_Leche_Create(CreateView):
#     model = VentaLeche
#     form_class = Ventas_Leche_form
#     template_name = 'Ventas/ventas_leche_form.html'
#     success_url = reverse_lazy('leche_list')

def Venta_Leche_Create(request):
    if request.method == 'POST':
        print("---------------------------------------------------------------------------------")
        form=Ventas_Leche_form(request.POST)
        if form.is_valid():
            var=form.save()
            var.total=var.cantidad*var.precio
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", var.total)
            var.save()
        return redirect('leche_list')
    else:
        form=Ventas_Leche_form()
    dic={
        'form':form,
    }
    return render(request, 'Ventas/ventas_leche_form.html',dic )


class Venta_Leche_List(ListView):
    queryset = VentaLeche.objects.all()
    #queryset = HISTORIAL_VENTAS_LECHE.objects.exclude(estado=True).order_by('id')
    template_name = 'Ventas/ventas_leche_list.html'
    paginate_by = 5




#----------------------------------------------------------------------------------------------------------------------
"Planes"

class PlanCreate(CreateView):
    model = Planes
    form_class = Planes_form
    template_name = 'Plan/planeacion.html'
    success_url = reverse_lazy('list_plan')

class PlanList(ListView):
    queryset = Planes.objects.all()
    template_name = 'Plan/planeacion_list.html'
    paginate_by = 5

def PlanAgroCreate(request,pk):
    query = Planes.objects.get(no_planeacion=pk)
    if request.method == 'POST':
        form = Plan_Agro_form(request.POST)
        if form.is_valid():
            var = form.save()
            var.no_planeacion = query.no_planeacion
            var.produccion_estimada = var.hectareas * var.costo
            var.total = var.produccion_estimada * var.cantidad
            var.save()
        return redirect('list_plan')
    else:
        form = Plan_Agro_form()
    dic = {
        'form':form,
    }
    return render(request, 'Plan/PlanAgroCreate.html', dic)


def PlanAgroList(request, pk):
    queryset = PlaneacionAgricola.objects.filter(no_planeacion=pk)
    dic = {
        'object_list':queryset,
    }
    return render(request, 'Plan/PlanAgroList.html', dic)

class PlanAgroUpdate(UpdateView):
    model = PlaneacionAgricola
    form_class = Plan_Agro_form
    template_name = 'Plan/PlanAgroCreate.html'
    success_url = reverse_lazy('list_plan')

class PlanAgroShow(DetailView):
    model = PlaneacionAgricola
    template_name = 'Plan/PlanAgroShow.html'

class PlanAgroDelete(DeleteView):
    model = PlaneacionAgricola
    template_name = 'Plan/PlanAgroDelete.html'
    success_url = reverse_lazy('list_plan')


def PlanBovCreate(request,pk):
    query = Planes.objects.get(no_planeacion=pk)
    if request.method == 'POST':
        form = Plan_Bovino_form(request.POST)
        if form.is_valid():
            var = form.save()
            var.no_planeacion = query.no_planeacion
            var.ingreso_anual = var.precio * var.venta
            print("----------------/////////////////-------------------",var.ingreso_anual)
            var.save()
        return redirect('list_plan')
    else:
        form = Plan_Bovino_form()
    dic = {
        'form':form,
    }
    return render(request, 'Plan/PlanBovCreate.html', dic)

def PlanBovList(request, pk):
    queryset = PlaneacionBovina.objects.filter(no_planeacion=pk)
    dic = {
        'object_list':queryset,
    }
    return render(request, 'Plan/PlanBovList.html', dic)

class PlanBovUpdate(UpdateView):
    model = PlaneacionBovina
    form_class = Plan_Bovino_form
    template_name = 'Plan/PlanBovCreate.html'
    success_url = reverse_lazy('list_plan')

class PlanBovShow(DetailView):
    model = PlaneacionBovina
    template_name = 'Plan/PlanBovShow.html'

class PlanBovDelete(DeleteView):
    model = PlaneacionBovina
    template_name = 'Plan/PlanBovDelete.html'
    success_url = reverse_lazy('list_plan')


def PlanLecheCreate(request,pk):
    query = Planes.objects.get(no_planeacion=pk)
    if request.method == 'POST':
        form = Plan_Leche_form(request.POST)
        if form.is_valid():
            var = form.save()
            var.no_planeacion = query.no_planeacion
            var.ingreso_diario = var.produccion_promedio * var.precio_litro
            var.estimado_anual = var.ingreso_diario * var.dias
            var.save()
        return redirect('list_plan')
    else:
        form = Plan_Leche_form()
    dic = {
        'form':form,
    }
    return render(request, 'Plan/PlanLecheCreate.html', dic)

def PlanLecList(request, pk):
    queryset = PlaneacionLeche.objects.filter(no_planeacion=pk)
    dic = {
        'object_list':queryset,
    }
    return render(request, 'Plan/PlanLecList.html', dic)


class PlanLecUpdate(UpdateView):
    model = PlaneacionLeche
    form_class = Plan_Leche_form
    template_name = 'Plan/PlanLecheCreate.html'
    success_url = reverse_lazy('list_plan')


class PlanLecheShow(DetailView):
    model = PlaneacionLeche
    template_name = 'Plan/PlanLecShow.html'

class PlanLecDelete(DeleteView):
    model = PlaneacionLeche
    template_name = 'Plan/PlanLecDelete.html'
    success_url = reverse_lazy('list_plan')


def PlanPorCreate(request,pk):
    query = Planes.objects.get(no_planeacion=pk)
    if request.method == 'POST':
        form = Plan_Porcina_form(request.POST)
        if form.is_valid():
            var = form.save()
            var.no_planeacion = query.no_planeacion
            var.ingresos = (var.cerdos + var.lechones) * var.precio_venta
            var.inversion = (var.cerdos + var.lechones) * var.precio_compra
            var.save()
        return redirect('list_plan')
    else:
        form = Plan_Porcina_form()
    dic = {
        'form':form,
    }
    return render(request, 'Plan/PlanPorCreate.html', dic)


def PlanPorList(request, pk):
    queryset = PlaneacionPorcina.objects.filter(no_planeacion=pk)
    dic = {
        'object_list':queryset,
    }
    return render(request, 'Plan/PlanPorcList.html', dic)


class PlanPorcUpdate(UpdateView):
    model = PlaneacionPorcina
    form_class = Plan_Porcina_form
    template_name = 'Plan/PlanPorCreate.html'
    success_url = reverse_lazy('list_plan')


class PlanPorcinoShow(DetailView):
    model = PlaneacionPorcina
    template_name = 'Plan/PlanPorcShow.html'


class PlanPorcDelete(DeleteView):
    model = PlaneacionPorcina
    template_name = 'Plan/PlanPorcDelete.html'
    success_url = reverse_lazy('list_plan')

def PlanProyGastCreate(request,pk):
    query = Planes.objects.get(no_planeacion=pk)
    if request.method == 'POST':
        form = Proyeccion_Gastos_form(request.POST)
        if form.is_valid():
            var = form.save()
            var.no_planeacion = query.no_planeacion
            var.semanal = var.cantidad * 7
            var.total_anual = var.semanal * 52
            var.save()
        return redirect('list_plan')
    else:
        form = Proyeccion_Gastos_form()
    dic = {
        'form':form,
    }
    return render(request, 'Plan/PlanProyGastCreate.html', dic)

def PlanProyGastList(request, pk):
    queryset = ProyeccionGastos.objects.filter(no_planeacion=pk)
    dic = {
        'object_list':queryset,
    }
    return render(request, 'Plan/PlanProyGastList.html', dic)

class PlanProyGasUpdate(UpdateView):
    model = ProyeccionGastos
    form_class = Proyeccion_Gastos_form
    template_name = 'Plan/PlanProyGastCreate.html'
    success_url = reverse_lazy('list_plan')

class PlanProyGasShow(DetailView):
    model = ProyeccionGastos
    template_name = 'Plan/PlanProyGasShow.html'

class PlanProyGasDelete(DeleteView):
    model = ProyeccionGastos
    template_name = 'Plan/PlanProyGasDelete.html'
    success_url = reverse_lazy('list_plan')


#Comparacion bovinos--------------------------------------------------------------------------------
def ComparacionBovino(request):
    Fecha_Actual = Notificaciones_function()

    day = Fecha_Actual.day
    month = Fecha_Actual.month
    year = Fecha_Actual.year

    fecha1 = str(year)+"-01-01"
    fecha2 = str(year)+"-12-31"
    # fecha_actual = str
    query1 = ControlVentaGanado.objects.filter(fecha__range=[fecha1,fecha2])

    vaca1 = ControlVentaGanado.objects.filter(fecha__range=[fecha1, fecha2]).filter(
        tipo='Vientre en producción limousin')

    vaca2 = ControlVentaGanado.objects.filter(fecha__range=[fecha1, fecha2]).filter(
        tipo='Vientre en crecimiento limousin')

    vaca3 = ControlVentaGanado.objects.filter(fecha__range=[fecha1, fecha2]).filter(
        tipo='Vientre en producción brangus')

    vaca4 = ControlVentaGanado.objects.filter(fecha__range=[fecha1, fecha2]).filter(
        tipo='Vientre en crecimiento brangus')

    vaca5 = ControlVentaGanado.objects.filter(fecha__range=[fecha1, fecha2]).filter(
        tipo='Sementales')

    vaca6 = ControlVentaGanado.objects.filter(fecha__range=[fecha1, fecha2]).filter(
        tipo='Becerros')

    vaca7 = ControlVentaGanado.objects.filter(fecha__range=[fecha1, fecha2]).filter(
        tipo='Sin registro')

    v1 = len(vaca1)
    v2 = len(vaca2)
    v3 = len(vaca3)
    v4 = len(vaca4)
    v5 = len(vaca5)
    v6 = len(vaca6)
    v7 = len(vaca7)

    query3 = Planes.objects.filter(fecha__range=[fecha1,fecha2])
    suma = 0
    size = 0
    try:
        query2 = PlaneacionBovina.objects.filter(no_planeacion=query3[0])

        size = len(query1)
        for i in range(len(query2)):
            suma = suma + int(query2[i].venta)
    except:
        query2 = PlaneacionBovina.objects.all()
    dic = {
        'total':size,
        'query':query1,
        'query2':query2,
        'suma':suma,
        'v1': v1,
        'v2': v2,
        'v3': v3,
        'v4': v4,
        'v5': v5,
        'v6': v6,
        'v7':v7,
    }
    return render(request, 'Comparacion/Comp_Bov.html', dic)


#Comparaciom Porcino--------------------------------------------------------------------------------------------------
def ComparacionPorcino(request):
    Fecha_Actual = Notificaciones_function()
    day = Fecha_Actual.day
    month = Fecha_Actual.month
    year = Fecha_Actual.year
    fecha1 = str(year) + "-01-01"
    fecha2 = str(year) + "-12-31"

    query1 = VentasPorcinos.objects.filter(fecha__range=[fecha1, fecha2])
    query2 = Planes.objects.filter(fecha__range=[fecha1, fecha2])
    suma = 0
    suma2 = 0
    suma3 = 0
    suma4 = 0
    g1 = 0
    g2 = 0
    try:
        size = len(query1)
        for i in range(size):
            suma = suma + int(query1[i].cantidad)
            g1 = g1 + int(query1[i].total_venta)
    except:
        pass

    try:
        query3 = PlaneacionPorcina.objects.filter(no_planeacion=query2[0])
        size = len(query3)
        for i in range(size):
            suma2 = suma2 + int(query3[i].cerdos)
            suma3 = suma3 + int(query3[i].lechones)
            g2 = g2 + int(query3[i].ingresos)
        suma4 = suma2 + suma3
    except:
        query3 = PlaneacionPorcina.objects.all()
        pass

    dic = {
        'venta_total':suma,
        'planeado':suma4,
        'query2':query3,
        'query1':query1,
        'g1':g1,
        'g2':g2,
    }

    return render(request, 'Comparacion/Comp_cerdos.html', dic)

def ComparacionLeche(request):
    Fecha_Actual = Notificaciones_function()
    day = Fecha_Actual.day
    month = Fecha_Actual.month
    year = Fecha_Actual.year
    fecha1 = str(year) + "-01-01"
    fecha2 = str(year) + "-12-31"

    query1 = VentaLeche.objects.filter(fecha__range=[fecha1, fecha2])
    query2 = Planes.objects.filter(fecha__range=[fecha1, fecha2])

    suma = 0
    suma2 = 0
    g1 = 0
    dias = 0

    try:
        size = len(query1)
        for i in range(size):
            suma = suma + int(query1[i].cantidad)
            g1 = g1 + int(query1[i].total)
    except:
        pass

    try:
        query3 = PlaneacionLeche.objects.filter(no_planeacion=query2[0])
        size = len(query3)
        for i in range(size):
            suma2 = suma2 + int(query3[i].estimado_anual)
            dias = dias + int(query3[i].dias)
            # plan_venta =
    except:
        query3 = PlaneacionLeche.objects.all()

    dic = {
        'ventas_leche':suma,
        'plan_ganancias':suma2,
        'venta_ganancia':g1,
        'dias':dias,
    }

    return render(request, 'Comparacion/Comp_Leche.html', dic)

def ComparacionAgricola(request):
    Fecha_Actual = Notificaciones_function()
    day = Fecha_Actual.day
    month = Fecha_Actual.month
    year = Fecha_Actual.year
    fecha1 = str(year) + "-01-01"
    fecha2 = str(year) + "-12-31"

    query1 = CompraVentaAgricola.objects.filter(fecha__range=[fecha1, fecha2]).filter(tipo='Venta')
    query2 = Planes.objects.filter(fecha__range=[fecha1, fecha2])

    L1 = []
    L2 = []
    L3 = []


    L4 = []
    L5 = []
    L6 = []

    g1 = 0
    g2 = 0

    try:
        size = len(query1)
        for i in range(size):
            L1.append(query1[i].cultivo)
            L2.append(query1[i].cantidad)
            L3.append(query1[i].precio)
            g1 = g1 + int(query1[i].precio)
    except:
        pass

    try:
        query3 = PlaneacionAgricola.objects.filter(no_planeacion=query2[0])
        size = len(query3)
        for i in range(size):
            L4.append(query3[i].cultivo)
            L5.append(query3[i].cantidad)
            L6.append(query3[i].total)
            g2 = g2 + int(query3[i].total)
    except:
        pass


    dic = {
        'cultivo':L1,
        'cantidad':L2,
        'precio':L3,
        'cultivo_plan':L4,
        'cantidad_plan':L5,
        'total':L6,
        'g':g1,
        'g2':g2,
    }

    return render(request, 'Comparacion/Comp_Agro.html', dic)
