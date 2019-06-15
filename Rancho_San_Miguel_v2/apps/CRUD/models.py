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
    tipo_g = Choices('Vientre en producción limousin', 'Vientre en crecimiento limousin', 'Vientre en producción brangus',
                  'Vientre en crecimiento brangus', 'Sementales', 'Becerros')
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
    tipo = models.CharField(choices=tipo_g, max_length=40)
    galeria_venta = models.BooleanField(default=False)
    costo = models.FloatField(default='0')
    img = models.ImageField(verbose_name="Imagen", upload_to='Ganado')
    img2 = models.ImageField(verbose_name="Imagen2", upload_to='Ganado')

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'ganado'

    def __str__(self):
        return self.nombre

class Ganado_sin_registro(models.Model):
    opciones = Choices('Macho', 'Hembra')
    nombre = models.CharField(max_length=15)
    arete = models.CharField(max_length=15, unique=True)
    sexo = models.CharField(choices=opciones, max_length=10)
    propietario = models.CharField(max_length=20)
    arete_padre = models.CharField(max_length=15, default='')
    arete_madre = models.CharField(max_length=15)
    f_nacimiento = models.DateField()
    peso_nacimiento = models.DecimalField(max_digits=11, decimal_places=0)
    localizacion_fierro = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=40, default='Sin registro')
    galeria_venta = models.BooleanField(default=False)
    costo = models.FloatField(default='0')
    img = models.ImageField(verbose_name="Imagen", upload_to='Ganado')
    img2 = models.ImageField(verbose_name="Imagen2", upload_to='Ganado')

    class Meta:
        ordering = ['-id']
        db_table = 'ganado2'

    def __str__(self):
        return self.nombre



class ControlVentaGanado(models.Model):
    no_venta = models.AutoField(primary_key=True)
    descripcion_venta = models.CharField(max_length=240)
    total_venta = models.DecimalField(max_digits=10, decimal_places=0)
    comprador = models.CharField(max_length=30)
    tipo = models.CharField(max_length=40, default='')
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        ordering = ['-no_venta']
        db_table = 'control_venta_ganado'

class VentasGanado(models.Model):
    no_venta = models.ForeignKey(ControlVentaGanado, models.DO_NOTHING, db_column='no_venta')
    arete = models.ForeignKey(Ganado, models.CASCADE, db_column='arete')
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        #managed = False
        ordering = ['-no_venta']
        db_table = 'ventas_ganado'


class ControlBitacoraGanado(models.Model):
    no_registrob = models.AutoField(primary_key=True)
    bovino = models.ManyToManyField(Ganado)
    descripcion = models.CharField(max_length=240)
    lugar = models.CharField(max_length=15)
    fecha = models.DateField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)



    class Meta:
        #managed = False
        ordering = ['-no_registrob']
        db_table = 'control_bitacora_ganado'


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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'control_ganado'

class InventarioAgricola(models.Model):
    opc= Choices('Toneladas', 'Pacas')
    cultivo = models.CharField(primary_key=True, max_length=50)
    unidad_medida = models.CharField(choices=opc, max_length=20)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        #managed = False
        ordering = ['-cultivo']
        db_table = 'inventario_agricola'

    def __str__(self):
        return str(self.cultivo)


class CompraVentaAgricola(models.Model):
    opciones = Choices('Compra', 'Venta', 'Baja')
    tipo =  models.CharField(choices=opciones,max_length=15, default="0")
    cultivo = models.ForeignKey(InventarioAgricola, models.DO_NOTHING, db_column='cultivo', default="0")
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=11, decimal_places=0, default="0", null=True)
    comprador = models.CharField(max_length=30, default='Rancho San Miguel')
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'Compras_ventas_agricolas'


class Produccion(models.Model):
    opciones = Choices('Primavera-Verano','Otoño-Invierno')
    hectareas = models.IntegerField()  # Hectareas sembradas
    cultivo = models.ForeignKey(InventarioAgricola, models.DO_NOTHING, db_column='cultivo')
    cantidad = models.IntegerField()  # cantidad de semilla utilizada
    produccion_obtenida = models.IntegerField(blank=True, null=True)  # Lo que se produjo
    unidad_medida = models.CharField(max_length=20, blank=True, null=True)
    ciclo = models.TextField(choices=opciones)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField(blank=True, null=True)

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'produccion'

class Planes(models.Model):
    no_planeacion = models.AutoField(primary_key=True)
    fecha = models.DateField()

    class Meta:
        #managed = False
        ordering = ['-no_planeacion']
        db_table = 'planes'

    def __str__(self):
        return str(self.no_planeacion)

#############################################################################
#############################################################################
#############################################################################

class ComprasPorcinos(models.Model):
    no_compra = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=0)
    total_compra = models.DecimalField(max_digits=10, decimal_places=0,default='0')
    fecha = models.DateField()
    vendedor = models.CharField(max_length=30)

    class Meta:
        #managed = False
        ordering = ['-no_compra']
        db_table = 'compras_porcinos'



class DeudoresAcreedores(models.Model):
    opciones = Choices('Acreedor','Deudor')
    nombre = models.CharField(max_length=40, default='')
    tipo = models.CharField(max_length=10,choices=opciones)
    motivo = models.CharField(max_length=240)
    deuda = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        ordering = ['-created']
        db_table = 'deudores_acreedores'

    def __str__(self):
        return str(self.nombre)


class Galeria(models.Model):
    nombre = models.CharField(max_length=40)
    img = models.ImageField(verbose_name="Imagen", upload_to='Galeria', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        ordering = ['-created']
        db_table = 'galeria'


class Gastos(models.Model):
    opciones = Choices('Sueldos','Combustible','Insumo de alimentos','Rentas', 'Derecho de agua', 'Otros')
    tipo = models.CharField(choices=opciones,max_length=50)
    motivo = models.CharField(max_length=240)
    monto = models.DecimalField(max_digits=10, decimal_places=0)
    img = models.ImageField(verbose_name="Imagen", upload_to='Galeria', blank=True, null=True)
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        ordering = ['-created']
        db_table = 'gastos'





class InventarioPorcino(models.Model):
    cantidad = models.IntegerField()

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'inventario_porcino'


class MovimientosDya(models.Model):
    no = models.ForeignKey(DeudoresAcreedores, models.DO_NOTHING, db_column='no')
    nombre = models.CharField(max_length=40,default="0")
    descripcion = models.CharField(max_length=240)
    deuda = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateField()

    def __str__(self):
        return int(self.no)

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'movimientos_dya'


class Notificaciones(models.Model):
    descripcion = models.CharField(max_length=240)
    fecha = models.DateField()
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        ordering = ['-created']
        db_table = 'notificaciones'


class PlaneacionAgricola(models.Model):
    op1 = Choices('Primavera-Verano','Otoño-Invierno')
    no_planeacion = models.CharField(max_length=50, default="0")
    ciclo = models.TextField(choices=op1)
    cultivo =  models.CharField(max_length=50)
    hectareas = models.IntegerField()
    costo = models.IntegerField()
    produccion_estimada = models.IntegerField(default="0")
    cantidad = models.IntegerField()
    total = models.IntegerField(default="0")

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'planeacion_agricola'


class PlaneacionBovina(models.Model):
    op1 = Choices('Vientre en producción limousin','Vientre en crecimiento limousin','Vientre en producción brangus',
                  'Vientre en crecimiento brangus', 'Sementales','Becerros')
    no_planeacion = models.CharField(max_length=50, default="0")
    tipo_ganado = models.CharField(choices=op1,max_length=50)
    hato = models.IntegerField()
    venta = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    ingreso_anual = models.DecimalField(max_digits=10, decimal_places=0, default="0")

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'planeacion_bovina'


class PlaneacionLeche(models.Model):
    no_planeacion = models.CharField(max_length=50, default="0")
    vacas_produccion = models.IntegerField()
    produccion_promedio = models.IntegerField()
    precio_litro = models.IntegerField()
    dias = models.IntegerField()
    ingreso_diario = models.DecimalField(max_digits=10, decimal_places=0, default='0')
    estimado_anual = models.DecimalField(max_digits=10, decimal_places=0, default='0')

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'planeacion_leche'


class PlaneacionPorcina(models.Model):
    no_planeacion = models.CharField(max_length=50, default="0")
    cerdos = models.IntegerField()
    lechones = models.IntegerField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=0)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=0)
    inversion = models.DecimalField(max_digits=10, decimal_places=0, default='0')
    ingresos = models.DecimalField(max_digits=10, decimal_places=0, default='0')

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'planeacion_porcina'


class ProyeccionGastos(models.Model):
    op1 = Choices('Sueldos','Combustible','Insumo de alimentos','Rentas', 'Derecho de agua', 'Otros')
    no_planeacion = models.CharField(max_length=50, default="0")
    tipo_gasto = models.CharField(choices=op1,max_length=40)
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    semanal = models.DecimalField(max_digits=10, decimal_places=0, default='0')
    total_anual = models.DecimalField(max_digits=10, decimal_places=0, default='0')
    # eventual = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'proyeccion_gastos'


class VentaLeche(models.Model):
    no_venta = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    total = models.DecimalField(max_digits=10, decimal_places=0,default='0')
    fecha = models.DateField()

    class Meta:
        #managed = False
        ordering = ['-no_venta']
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
    total_venta = models.DecimalField(max_digits=10, decimal_places=0,default='0')
    fecha = models.DateField()
    comprador = models.CharField(max_length=30)

    class Meta:
        #managed = False
        ordering = ['-no_venta']
        db_table = 'ventas_porcinos'


class CompraVentaAgricola(models.Model):
    opciones = Choices('Compra', 'Venta', 'Baja')
    tipo =  models.CharField(choices=opciones,max_length=15)
    cultivo = models.ForeignKey(InventarioAgricola, models.DO_NOTHING, db_column='cultivo')
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=11, decimal_places=0)
    comprador = models.CharField(max_length=30)
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'Compras_ventas_agricolas'




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

#Inventario no agricola
class InventarioNoAgricola(models.Model):
    opc= Choices('Bultos',)
    articulo = models.CharField(primary_key=True, max_length=50)
    unidad_medida = models.CharField(choices=opc, max_length=20)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        #managed = False
        ordering = ['-articulo']
        db_table = 'inventario_noagricola'

    def __str__(self):
        return str(self.articulo)



class CompraVentaNoAgricola(models.Model):
    opciones = Choices('Compra',  'Baja')
    tipo =  models.CharField(choices=opciones,max_length=15, default="0", null=True)
    articulo = models.ForeignKey(InventarioNoAgricola, models.DO_NOTHING, db_column='articulo')
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=11, decimal_places=0, default="0", null=True)
    # comprador = models.CharField(max_length=30)
    fecha = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'Compras_retiro_noagricolas'

class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    direc = models.CharField(max_length=60)
    telefono = models.CharField(max_length=60)
    correo = models.EmailField()

    class Meta:
        #managed = False
        ordering = ['-id']
        db_table = 'Contacto'