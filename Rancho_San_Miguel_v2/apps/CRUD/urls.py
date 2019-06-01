from django.urls import path
from .views import Bovino_Create
from .views import Query_Notificaciones, Notificaciones_Create, Notificaciones_Listar
from .views import CrearUsuario, ListarUsuarios, AddGrupos
from .views import GaleriaCreate, GaleriaList, GaleriaDelete, GaleriaDetail, GaleriaUpdate
from .views import GaleriaList2
from .views import Controlg_Update, Controlg_Show, Controlg_List, Controlg_Delete, Controlg_Create
from .views import Compra_Cerdos_Create, Compra_Cerdos_List


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
    #Porcinos
    path('porcino/crear/', Compra_Cerdos_Create, name="cerdos_crear"),
    path('porcino/list/', Compra_Cerdos_List.as_view(), name="cerdos_list"),
    #path('porcino/delete/<int:pk>', Venta_Cerdos_Delete, name="cerdos_delete"),
# Control_ganado
    path('controlganado/', Controlg_Create.as_view(), name="control_crear"),
    path('controllist/', Controlg_List.as_view(), name="control_list"),
    path('controlshow/<int:pk>', Controlg_Show.as_view(), name="control_show"),
    path('controlupdate/<int:pk>', Controlg_Update.as_view(), name="control_update"),
    path('controldelete/<int:pk>', Controlg_Delete.as_view(), name="control_delete"),
]