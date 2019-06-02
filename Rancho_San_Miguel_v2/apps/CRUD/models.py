# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `#managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from model_utils import Choices

from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class Ganado(models.Model):
    opciones = Choices('Macho', 'Hembra')
    opciones2 = Choices('Vendida', 'Viva', 'Muerta')
    tc = Choices('Uníparo', 'Gemelar MH', 'Gemelar HH', 'Gemelar MM', 'Múltiple')
    tp = Choices('Normal', 'Distónico', 'Difícil', 'Cesárea')
    tt = Choices("Derecha",'Izquierda')
    nombre = models.CharField(max_length=15)
    arete = models.CharField(max_length=15, unique=True)
    siniga = models.CharField(max_length=15, blank=True, null=True)
    sexo = models.CharField(choices=opciones, max_length=10)
    propietario = models.CharField(max_length=20)
    ganadera = models.CharField(max_length=30)
    arete_padre = models.CharField(max_length=15)
    arete_madre = models.CharField(max_length=15)
    f_nacimiento = models.DateField()
    tipo_nacimiento = models.CharField(choices=tc,max_length=10)
    tipo_parto = models.CharField(choices=tp,max_length=10)
    potrero = models.CharField(max_length=30)
    peso_nacimiento = models.DecimalField(max_digits=11, decimal_places=0)
    localizacion_fierro = models.CharField(max_length=20, blank=True, null=True)
    localizacion_tatuaje = models.CharField(choices=tt,max_length=20, blank=True, null=True)
    estado = models.CharField(choices=opciones2, max_length=10)
    galeria_venta = models.BooleanField(default=False)
    img = models.ImageField(verbose_name="Imagen", upload_to='Ganado', blank=True, null=True)
    img2 = models.ImageField(verbose_name="Imagen2", upload_to='Ganado', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'ganado'


class ControlVentaGanado(models.Model):
    no_venta = models.AutoField(primary_key=True)
    descripcion_venta = models.CharField(max_length=240)
    total_venta = models.DecimalField(max_digits=10, decimal_places=0)
    comprador = models.CharField(max_length=30)
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        db_table = 'control_venta_ganado'

class VentasGanado(models.Model):
    no_venta = models.ForeignKey(ControlVentaGanado, models.DO_NOTHING, db_column='no_venta')
    arete = models.ForeignKey(Ganado, models.DO_NOTHING, db_column='arete')
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        #managed = False
        db_table = 'ventas_ganado'


class ControlBitacoraGanado(models.Model):
    no_registrob = models.IntegerField(primary_key=True)
    bovino = models.ManyToManyField(Ganado)
    descripcion = models.CharField(max_length=240)
    lugar = models.CharField(max_length=15)
    fecha = models.DateField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'control_bitacora_ganado'

#

# class BitacoraGanado(models.Model):
#     no_registrob = models.ForeignKey('ControlBitacoraGanado', models.DO_NOTHING, db_column='no_registrob')
#     arete = models.ForeignKey('Ganado', models.DO_NOTHING, db_column='arete')

    # class Meta:
    #     #managed = False
    #     db_table = 'bitacora_ganado'


class ControlGanado(models.Model):
    mot = Choices('Control de peso', 'Control sanitario', 'Control preventivo', 'Otro')
    arete = models.ForeignKey('Ganado', models.DO_NOTHING, db_column='arete')
    motivo = models.CharField(choices=mot, max_length=50)
    descripcion = models.CharField(max_length=240)
    lugar = models.CharField(max_length=50)
    fecha = models.DateField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'control_ganado'

class InventarioAgricola(models.Model):
    cultivo = models.CharField(primary_key=True, max_length=50)
    unidad_medida = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        #managed = False
        db_table = 'inventario_agricola'

    def __str__(self):
        return self.cultivo


class ControlVentasAgricolas(models.Model):
    no_registro = models.AutoField(primary_key=True)
    total_venta = models.DecimalField(max_digits=10, decimal_places=0)
    comprador = models.CharField(max_length=30)
    fecha = models.DateField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'control_ventas_agricolas'

class VentasAgricola(models.Model):
    no_venta = models.ForeignKey(ControlVentasAgricolas, models.DO_NOTHING, db_column='no_venta')
    cultivo = models.ForeignKey(InventarioAgricola, models.DO_NOTHING, db_column='cultivo')
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=11, decimal_places=0)

    class Meta:
        #managed = False
        db_table = 'ventas_agricola'

class ControlComprasAgricolas(models.Model):
    no_compra = models.IntegerField(primary_key=True)
    total_compra = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateField()
    vendedor = models.CharField(max_length=30)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'control_compras_agricolas'

class ComprasAgricolas(models.Model):
    no_compra = models.ForeignKey('ControlComprasAgricolas', models.DO_NOTHING, db_column='no_compra')
    cultivo = models.ForeignKey('InventarioAgricola', models.DO_NOTHING, db_column='cultivo')
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=11, decimal_places=0)

    class Meta:
        #managed = False
        db_table = 'compras_agricolas'

class Produccion(models.Model):
    opciones = Choices(1, 2)
    hectareas = models.IntegerField()  # Hectareas sembradas
    cultivo = models.ForeignKey(InventarioAgricola, models.DO_NOTHING, db_column='cultivo')
    cantidad = models.IntegerField()  # cantidad de semilla utilizada
    produccion_obtenida = models.IntegerField(blank=True, null=True)  # Lo que se produjo
    unidad_medida = models.CharField(max_length=20, blank=True, null=True)
    ciclo = models.IntegerField(choices=opciones)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'produccion'

class Planes(models.Model):
    no_planeacion = models.AutoField(primary_key=True)
    fecha = models.DateField()

    class Meta:
        #managed = False
        db_table = 'planes'
#############################################################################
#############################################################################
#############################################################################

class ComprasPorcinos(models.Model):
    no_compra = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=0)
    total_compra = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateField()
    vendedor = models.CharField(max_length=30)

    class Meta:
        #managed = False
        db_table = 'compras_porcinos'



class DeudoresAcreedores(models.Model):
    tipo = models.CharField(max_length=10)
    motivo = models.CharField(max_length=240)
    deuda = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        db_table = 'deudores_acreedores'


class Galeria(models.Model):
    nombre = models.CharField(max_length=40)
    img = models.ImageField(verbose_name="Imagen", upload_to='Galeria', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        db_table = 'galeria'


class Gastos(models.Model):
    opciones = Choices('Insumos','Insumos Agricolas','otros')
    tipo = models.CharField(choices=opciones,max_length=50)
    motivo = models.CharField(max_length=240)
    monto = models.DecimalField(max_digits=10, decimal_places=0)
    img = models.ImageField(verbose_name="Imagen", upload_to='Galeria', blank=True, null=True)
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        db_table = 'gastos'





class InventarioPorcino(models.Model):
    cantidad = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'inventario_porcino'


class MovimientosDya(models.Model):
    no = models.ForeignKey(DeudoresAcreedores, models.DO_NOTHING, db_column='no')
    descripcion = models.CharField(max_length=240)
    deuda = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateField()

    def __str__(self):
        return self.no._related_fields

    class Meta:
        #managed = False
        db_table = 'movimientos_dya'


class Notificaciones(models.Model):
    descripcion = models.CharField(max_length=240)
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        db_table = 'notificaciones'


class PlaneacionAgricola(models.Model):
    no_planeacion = models.ForeignKey('Planes', models.DO_NOTHING, db_column='no_planeacion')
    ciclo = models.IntegerField()
    cultivo = models.IntegerField()
    hectareas = models.IntegerField()
    costo = models.IntegerField()
    produccion_estimada = models.IntegerField()
    cantidad = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'planeacion_agricola'


class PlaneacionBovina(models.Model):
    no_planeacion = models.ForeignKey('Planes', models.DO_NOTHING, db_column='no_planeacion')
    tipo_ganado = models.CharField(max_length=50)
    hato = models.IntegerField()
    venta = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    ingreso_anual = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        #managed = False
        db_table = 'planeacion_bovina'


class PlaneacionLeche(models.Model):
    no_planeacion = models.ForeignKey('Planes', models.DO_NOTHING, db_column='no_planeacion')
    vacas_produccion = models.IntegerField()
    produccion_promedio = models.IntegerField()
    ingreso_diario = models.DecimalField(max_digits=10, decimal_places=0)
    estimado_anual = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        #managed = False
        db_table = 'planeacion_leche'


class PlaneacionPorcina(models.Model):
    no_planeacion = models.ForeignKey('Planes', models.DO_NOTHING, db_column='no_planeacion')
    cerdos = models.IntegerField()
    lechones = models.IntegerField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=0)
    inversion = models.DecimalField(max_digits=10, decimal_places=0)
    ingresos = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        #managed = False
        db_table = 'planeacion_porcina'


class ProyeccionGastos(models.Model):
    no_planeacion = models.ForeignKey(Planes, models.DO_NOTHING, db_column='no_planeacion')
    tipo_gasto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    semanal = models.DecimalField(max_digits=10, decimal_places=0)
    total_anual = models.DecimalField(max_digits=10, decimal_places=0)
    eventual = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'proyeccion_gastos'


class VentaLeche(models.Model):
    no_venta = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    total = models.DecimalField(max_digits=10, decimal_places=0,default='0')
    fecha = models.DateField()

    class Meta:
        #managed = False
        db_table = 'venta_leche'


class VentasGanado(models.Model):
    no_venta = models.ForeignKey(ControlVentaGanado, models.DO_NOTHING, db_column='no_venta')
    arete = models.ForeignKey(Ganado, models.DO_NOTHING, db_column='arete')
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        #managed = False
        db_table = 'ventas_ganado'


class VentasPorcinos(models.Model):
    no_venta = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=0)
    total_venta = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateField()
    comprador = models.CharField(max_length=30)

    class Meta:
        #managed = False
        db_table = 'ventas_porcinos'

# Borrar la foto vieja si se le da al boton borrar
@receiver(post_delete, sender=Ganado)
def photo_post_delete_handler(sender, **kwargs):
    listiningImage = kwargs['instance']
    storage, path = listiningImage.img.storage, listiningImage.img.path
    storage.delete(path)

# Borrar la foro vieja si se actualiza
@receiver(pre_save, sender=Ganado)
def update_img(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_img = Ganado.objects.get(pk=instance.pk).img
        except:
            return
        else:
            new_img = instance.img
            if old_img and old_img.url != new_img.url:
                old_img.delete(save=False)