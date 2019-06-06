from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from ..CRUD.views import Notificaciones_function, Notificaciones



def index(request):
    return render(request, 'home/index.html')

def index2(request):
    Fecha_Actual = Notificaciones_function()

    day = Fecha_Actual.day
    month = Fecha_Actual.month
    year = Fecha_Actual.year

    if int(day) <= 9:
        day = "0" + str(day)

    if int(month) <= 9:
        month = "0" + str(month)

    var = str(year) + "-" + str(month) + "-" + str(day)

    query = Notificaciones.objects.filter(fecha=var).update(estado=False)


    query2 = Notificaciones.objects.filter(estado=False)

    dic = {
        'form': query2,
    }
    return render(request, 'home/index2.html', dic)
    # return render(request, 'home/index2.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contacto.html')

def blog(request):
    return render(request, 'home/blog.html')

def element(request):
    return render(request, 'home/element.html')

def portfolio(request):
    return render(request, 'home/portfolio.html')

def service(request):
    return render(request, 'home/service.html')