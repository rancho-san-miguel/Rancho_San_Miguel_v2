from django.urls import path
from .views import *

urlpatterns = [
    #Ganado
    path('bovinoshow/<int:pk>', Bovino_Show.as_view(), name="bovino_show"),
    path('bovino/', Bovino_Create.as_view(), name="bovino_crear"),
    path('bovino/search/', Bovino_Search, name="bovino_search"),
    path('bovino/list/', Bovino_Search, name="bovino_list"),
    path('bovinoupdate/<int:pk>',Bovino_Update.as_view(), name="bovino_update"),
    path('bovinodelete/<int:pk>', Bovino_Delete.as_view(), name="bovino_delete"),
    path('bovinoventa/<int:pk>', Bovino_update_ventas_create, name="bovino_venta"),
    path('bovino/update/venta/<int:pk>',Bovino_Update_Poner_En_Venta.as_view(), name="bovino_venta_poner"),
    path('ventalist/', Venta_Bovino_List.as_view(), name="venta_list"),
    path('ventashow/<int:pk>', Venta_Bovino_Show.as_view(), name="venta_show"),
    path('bovino/galeria/venta/list/', Bovino_Galeria_Venta_List, name="bovino_galeria_venta_list"),
    path('bovino/galeria/venta/list/<int:pk>', Bovino_Galeria_Venta_Show, name="bovino_galeria_venta_show"),

    #Ganado sin registro
    path('bovino/sinregistro', Bovino_Create2.as_view(), name="bovino_sinregistro_crear"),
    path('bovino/sinregistro/search/', Bovino_Search2, name="bovino_sinregistro_search"),
    path('bovinoshow/sinregistro/<int:pk>', Bovino_Show2.as_view(), name="bovino_sinregistro_show"),
    path('bovinoupdate/sinregistro/<int:pk>',Bovino_Update2.as_view(), name="bovino_sinregistro_update"),
    path('bovinodelete/sinregistro/<int:pk>', Bovino_Delete2.as_view(), name="bovino_sinregistro_delete"),
    path('bovinoventa/sinregistro/<int:pk>', Bovino_update_ventas_create2, name="bovino_sinregistro_venta"),
    path('bovino/galeria/venta/list2/<int:pk>', Bovino_Galeria_Venta_Show2, name="bovino_galeria_venta_show2"),
    path('bovino/update2/venta/<int:pk>',Bovino_Update_Poner_En_Venta2.as_view(), name="bovino_venta_poner2"),


    #Notificaciones
    path('notificaciones/', Query_Notificaciones, name="notificacion"),
    path('notificaciones/listar/', Notificaciones_Listar.as_view(), name="notificacion_listar"),
    path('notificaciones/create/', Notificaciones_Create.as_view(), name="notificaciones_crear"),
    path('notificaciones/update/<int:pk>', Notificaciones_Update.as_view(), name="notificaciones_update"),
    #Usuarios
    path('crear/usuario/', CrearUsuario.as_view(), name='crear_usuario'),
    path('listar/usuario/', ListarUsuarios.as_view(), name='listar_usuario'),
    path('add/grupos/usuario/<int:pk>', AddGrupos, name='crear_grupos'),
    path('delete/usuario/<int:pk>', DeleteUsuario.as_view(), name='delete_usuarios'),
    path('update/usuario/<int:pk>', UpdateUsuario.as_view(), name='update_usuarios'),
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

    path('porcinoinvent/', InventCerdos_List.as_view(), name="cerdos_inventario"),

# Control_ganado
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

    #Planeacion
    path('plan/crear/', PlanCreate, name='crear_plan'),
    path('plan/list/', PlanList.as_view(), name='list_plan'),
    path('plan/agro/create/<int:pk>', PlanAgroCreate, name='plan_agro_create'),
    path('plan/agro/list/<int:pk>', PlanAgroList, name='plan_agro_list'),
    path('plan/agro/update/<int:pk>', PlanAgroUpdate, name='plan_agro_update'),
    path('plan/agro/show/<int:pk>', PlanAgroShow.as_view(), name='plan_agro_show'),
    path('plan/agro/delete/<int:pk>', PlanAgroDelete.as_view(), name='plan_agro_delete'),
    path('plan/bovino/create/<int:pk>', PlanBovCreate, name='plan_bov_create'),
    path('plan/bovino/list/<int:pk>', PlanBovList, name='plan_bov_list'),
    path('plan/bovino/update/<int:pk>', PlanBovUpdate, name='plan_bov_update'),
    path('plan/bovino/show/<int:pk>', PlanBovShow.as_view(), name='plan_bov_show'),
    path('plan/bovino/delete/<int:pk>', PlanBovDelete.as_view(), name='plan_bov_delete'),
    path('plan/leche/create/<int:pk>', PlanLecheCreate, name='plan_leche_create'),
    path('plan/leche/list/<int:pk>', PlanLecList, name='plan_leche_list'),
    path('plan/leche/update/<int:pk>', PlanLecUpdate, name='plan_leche_update'),
    path('plan/leche/show/<int:pk>', PlanLecheShow.as_view(), name='plan_leche_show'),
    path('plan/leche/delete/<int:pk>', PlanLecDelete.as_view(), name='plan_leche_delete'),
    path('plan/porcina/create/<int:pk>', PlanPorCreate, name='plan_porcina_create'),
    path('plan/porcino/list/<int:pk>', PlanPorList, name='plan_porcino_list'),
    path('plan/porcino/update/<int:pk>', PlanPorcUpdate, name='plan_porcino_update'),
    path('plan/porcino/show/<int:pk>', PlanPorcinoShow.as_view(), name='plan_porcino_show'),
    path('plan/porcino/delete/<int:pk>', PlanPorcDelete.as_view(), name='plan_porcino_delete'),
    path('plan/gastos/create/<int:pk>', PlanProyGastCreate, name='plan_proyec_gasto_create'),
    path('plan/gastos/list/<int:pk>', PlanProyGastList, name='plan_proyec_gasto_list'),
    path('plan/gastos/update/<int:pk>', PlanProyGasUpdate, name='plan_proyec_gasto_update'),
    path('plan/gastos/show/<int:pk>', PlanProyGasShow.as_view(), name='plan_proyec_gasto_show'),
    path('plan/gastos/delete/<int:pk>', PlanProyGasDelete.as_view(), name='plan_proyec_gasto_delete'),
    #Comparacion
    path('comparacion/bovino/', ComparacionBovino, name='comparacion_bovino'),
    path('comparacion/porcino/', ComparacionPorcino, name='comparacion_porcino'),
    path('comparacion/leche/', ComparacionLeche, name='comparacion_leche'),
    path('comparacion/agro/', ComparacionAgricola, name='comparacion_agro'),
    path('comparacion/gastos/', Comparacion_Gastos, name='comparacion_gastos'),
    #Ganancias
    path('ganancias/', Ganancias, name='ganancias_list'),
    path('comparacion/ganancias/', Comparacion_Ganancias, name='comparacion_ganancias_list'),
]