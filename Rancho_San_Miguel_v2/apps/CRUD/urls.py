from django.urls import path
from .views import Bovino_Create, Bovino_Search, Bovino_Show, Bovino_List, Bovino_Update, Bovino_Delete
from .views import Query_Notificaciones, Notificaciones_Create, Notificaciones_Listar, Bovino_update_ventas_create
from .views import CrearUsuario, ListarUsuarios, AddGrupos, Venta_Bovino_List, Venta_Bovino_Show
from .views import GaleriaCreate, GaleriaList, GaleriaDelete, GaleriaDetail, GaleriaUpdate
from .views import GaleriaList2
from .views import Controlg_Update, Controlg_Show, Controlg_List, Controlg_Delete, Controlg_Create
from .views import Compra_Cerdos_Create, Compra_Cerdos_List
from .views import En_Proceso_Create,En_Proceso_Delete,En_Proceso_List,En_Proceso_Show, En_Proceso_Update, En_Proceso_Fin, ordenar_producciones
from .views import Venta_Cerdos_Create, Venta_Cerdos_List,Abonos,AbonosList
from .views import DeudoresAcreedoresCreate,DeudoresAcreedoresDetail,DeudoresAcreedoresList,DeudoresAcreedoresDelete,DeudoresAcreedoresUpdate
from .views import HistoriaCreate,HistoriaDelete,HistoriaDetail,HistoriaList,HistoriaUpdate
from .views import Venta_Leche_Create, Venta_Leche_List, Comprar_Vender_list, Acomprar_create, AVender_create, Abaja_create

from .views import InventarioA_Delete, InventarioA_Create, InventarioA_List, InventarioA_Update

urlpatterns = [
    path('bovinoshow/<int:pk>', Bovino_Show.as_view(), name="bovino_show"),
    path('bovino/', Bovino_Create.as_view(), name="bovino_crear"),
    path('bovino/search/', Bovino_Search, name="bovino_search"),
    path('bovino/list/', Bovino_Search, name="bovino_list"),
    path('bovinoupdate/<int:pk>',Bovino_Update.as_view(), name="bovino_update"),
    path('bovinodelete/<int:pk>', Bovino_Delete.as_view(), name="bovino_delete"),
    path('bovinoventa/<int:pk>', Bovino_update_ventas_create, name="bovino_venta"),
    path('ventalist/', Venta_Bovino_List.as_view(), name="venta_list"),
    path('ventashow/<int:pk>', Venta_Bovino_Show.as_view(), name="venta_show"),

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


    path('porcino_C_crear/',Venta_Cerdos_Create, name="cerdos_crearVenta"),
    path('porcino_C_list/', Venta_Cerdos_List.as_view(), name="cerdos_listVenta"),
# Control_ganado
    path('controlganado/', Controlg_Create.as_view(), name="control_crear"),
    path('controllist/', Controlg_List.as_view(), name="control_list"),
    path('controlshow/<int:pk>', Controlg_Show.as_view(), name="control_show"),
    path('controlupdate/<int:pk>', Controlg_Update.as_view(), name="control_update"),
    path('controldelete/<int:pk>', Controlg_Delete.as_view(), name="control_delete"),
    ###########################################################
    ###########################################################
    path('DeudoresAcreedores/', DeudoresAcreedoresCreate.as_view(), name='Deudore_Acreedores_create'),
    path('DeudoresAcreedoreslist/', DeudoresAcreedoresList.as_view(), name='Deudore_Acreedores_list'),
    path('DeudoresAcreedoresdelete/<int:pk>/', DeudoresAcreedoresDelete.as_view(), name='Deudore_Acreedores_delete'),
    path('DeudoresAcreedoresshow/<int:pk>/', DeudoresAcreedoresDetail.as_view(), name='Deudore_Acreedores_show'),
    path('DeudoresAcreedoresupdate/<int:pk>/', DeudoresAcreedoresUpdate.as_view(), name='Deudore_Acreedores_update'),

    path('Abonos/<int:pk>', Abonos, name="Abonar"),
    path('Abonoslist/venta', AbonosList.as_view(), name="Abono_list"),

#En Invenrario agricola/almacen
    path('inventario_agricola/almacen/create', InventarioA_Create.as_view(), name='inventario_crear'),
    path('inventario_agricola/almacen/list', InventarioA_List.as_view(), name='inventario_list'),
    path('inventario_agricola/almacen/modificar/<pk>', InventarioA_Update.as_view(), name='inventario_actualizar'),
    path('inventario_agricola/almacen/eliminar/<pk>', InventarioA_Delete.as_view(), name='inventario_eliminar'),
    path('compraventa_agricola/ver', Comprar_Vender_list, name='compraryvenderagricola'),
    path('compra_agricola/registrar_compra/<pk>', Acomprar_create, name='compraragricola_crear'),
    path('compra_agricola/registrar_venta/<pk>', AVender_create, name='venderagricola_crear'),
    path('compra_agricola/registrar_retiro/<pk>', Abaja_create, name='retiraragricola_crear'),

    path('historia/', HistoriaCreate.as_view(), name='Historial_Compras_create'),
    path('historialist/', HistoriaList.as_view(), name='Historial_Compras_list'),
    path('historiadelete/<int:pk>/', HistoriaDelete.as_view(), name='Historial_Compras_delete'),
    path('historiahow/<int:pk>/', HistoriaDetail.as_view(), name='Historial_Compras_show'),
    path('historiaupdate/<int:pk>/', HistoriaUpdate.as_view(), name='Historial_Compras_update'),
#Agricola en produccion
    path('producciones/enproceso/create', En_Proceso_Create.as_view(), name='cultivo_en_proceso_create'),
    path('producciones/enproceso/list', ordenar_producciones, name='cultivo_en_proceso_list'),
    path('producciones/enproceso/update/<int:pk>', En_Proceso_Update.as_view(), name='cultivo_en_proceso_update'),
    path('producciones/enproceso/delete/<int:pk>', En_Proceso_Delete.as_view(), name='cultivo_en_proceso_delete'),
    path('producciones/enproceso/show/<int:pk>', En_Proceso_Show.as_view(), name='cultivo_en_proceso_show'),
    path('producciones/enproceso/finalizar/<int:pk>', En_Proceso_Fin, name='finalizar_produccion'),

    #Venta de leche
    path('leche/crear/', Venta_Leche_Create, name="leche_crear"),
    path('leche/list/', Venta_Leche_List.as_view(), name="leche_list"),
]