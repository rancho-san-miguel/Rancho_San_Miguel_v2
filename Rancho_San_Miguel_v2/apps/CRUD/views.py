from django.shortcuts import render
from django.shortcuts import redirect, render

from .models import Ganado
from .models import Notificaciones
from .models import Galeria

from .forms import Ganado_Form,Notificaciones_form, GaleriaForm


from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from datetime import datetime

from django.contrib.auth.models import User, Group
from .forms import SignUpForm

class Bovino_Create(CreateView):
    model = Ganado
    form_class = Ganado_Form
    template_name = 'RegBov/regbov_form.html'
    success_url = reverse_lazy('bovino_crear')#Cambiar a list
    # success_url = reverse_lazy('bovino_list')



#................................................................................................
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