from django.urls import path
from .views import Bovino_Create
from .views import Query_Notificaciones, Notificaciones_Create, Notificaciones_Listar
from .views import CrearUsuario, ListarUsuarios, AddGrupos
from .views import GaleriaCreate, GaleriaList, GaleriaDelete, GaleriaDetail, GaleriaUpdate
from .views import GaleriaList2


urlpatterns = [
    path('bovino/', Bovino_Create.as_view(), name="bovino_crear"),
    #Notificaciones
    path('notificaciones/', Query_Notificaciones, name="notificacion"),
    path('notificaciones/listar/', Notificaciones_Listar.as_view(), name="notificacion_listar"),
    path('notificaciones/create/', Notificaciones_Create.as_view(), name="notificaciones_crear"),
    #Usuarios
    path('crear/usuario/', CrearUsuario.as_view(), name='crear_usuario'),
    path('listar/usuario/', ListarUsuarios.as_view(), name='listar_usuario'),
    path('add/grupos/usuario/<int:pk>', AddGrupos, name='crear_grupos'),
    #Galeria
    path('galeria/', GaleriaCreate.as_view(), name='galeria_create'),
    path('galerialist/', GaleriaList.as_view(), name='galeria_list'),
    path('galeriadelete/<int:pk>/', GaleriaDelete.as_view(), name='galeria_delete'),
    path('galeriashow/<int:pk>/', GaleriaDetail.as_view(), name='galeria_show'),
    path('galeriaupdate/<int:pk>/', GaleriaUpdate.as_view(), name='galeria_update'),
    path('galerialist2/', GaleriaList2.as_view(), name='galeria_list2'),
]