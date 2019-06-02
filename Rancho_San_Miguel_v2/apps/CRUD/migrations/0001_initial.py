# Generated by Django 2.1.7 on 2019-06-02 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitacoraGanado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'bitacora_ganado',
            },
        ),
        migrations.CreateModel(
            name='ComprasAgricolas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=0, max_digits=11)),
            ],
            options={
                'db_table': 'compras_agricolas',
            },
        ),
        migrations.CreateModel(
            name='ComprasPorcinos',
            fields=[
                ('no_compra', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio_unidad', models.DecimalField(decimal_places=0, max_digits=10)),
                ('total_compra', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fecha', models.DateField()),
                ('vendedor', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'compras_porcinos',
            },
        ),
        migrations.CreateModel(
            name='ControlBitacoraGanado',
            fields=[
                ('no_registrob', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=240)),
                ('lugar', models.CharField(max_length=15)),
                ('fecha', models.DateField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'control_bitacora_ganado',
            },
        ),
        migrations.CreateModel(
            name='ControlComprasAgricolas',
            fields=[
                ('no_compra', models.IntegerField(primary_key=True, serialize=False)),
                ('total_compra', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fecha', models.DateField()),
                ('vendedor', models.CharField(max_length=30)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'control_compras_agricolas',
            },
        ),
        migrations.CreateModel(
            name='ControlGanado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(choices=[('Control de peso', 'Control de peso'), ('Control sanitario', 'Control sanitario'), ('Control preventivo', 'Control preventivo'), ('Otro', 'Otro')], max_length=50)),
                ('descripcion', models.CharField(max_length=240)),
                ('lugar', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'control_ganado',
            },
        ),
        migrations.CreateModel(
            name='ControlVentaGanado',
            fields=[
                ('no_venta', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_venta', models.CharField(max_length=240)),
                ('total_venta', models.DecimalField(decimal_places=0, max_digits=10)),
                ('comprador', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'control_venta_ganado',
            },
        ),
        migrations.CreateModel(
            name='ControlVentasAgricolas',
            fields=[
                ('no_registro', models.AutoField(primary_key=True, serialize=False)),
                ('total_venta', models.DecimalField(decimal_places=0, max_digits=10)),
                ('comprador', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'control_ventas_agricolas',
            },
        ),
        migrations.CreateModel(
            name='DeudoresAcreedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
                ('motivo', models.CharField(max_length=240)),
                ('deuda', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fecha', models.DateField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'deudores_acreedores',
            },
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('img', models.ImageField(blank=True, null=True, upload_to='Galeria', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'galeria',
            },
        ),
        migrations.CreateModel(
            name='Ganado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('arete', models.CharField(max_length=15, unique=True)),
                ('siniga', models.CharField(blank=True, max_length=15, null=True)),
                ('sexo', models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], max_length=10)),
                ('propietario', models.CharField(max_length=20)),
                ('ganadera', models.CharField(max_length=30)),
                ('arete_padre', models.CharField(max_length=15)),
                ('arete_madre', models.CharField(max_length=15)),
                ('f_nacimiento', models.DateField()),
                ('tipo_nacimiento', models.CharField(choices=[('Uníparo', 'Uníparo'), ('Gemelar MH', 'Gemelar MH'), ('Gemelar HH', 'Gemelar HH'), ('Gemelar MM', 'Gemelar MM'), ('Múltiple', 'Múltiple')], max_length=10)),
                ('tipo_parto', models.CharField(choices=[('Normal', 'Normal'), ('Distónico', 'Distónico'), ('Difícil', 'Difícil'), ('Cesárea', 'Cesárea')], max_length=10)),
                ('potrero', models.CharField(max_length=30)),
                ('peso_nacimiento', models.DecimalField(decimal_places=0, max_digits=11)),
                ('localizacion_fierro', models.CharField(blank=True, max_length=20, null=True)),
                ('localizacion_tatuaje', models.CharField(blank=True, choices=[('Derecha', 'Derecha'), ('Izquierda', 'Izquierda')], max_length=20, null=True)),
                ('estado', models.CharField(choices=[('Vendida', 'Vendida'), ('Viva', 'Viva'), ('Muerta', 'Muerta')], max_length=10)),
                ('galeria_venta', models.BooleanField(default=False)),
                ('img', models.ImageField(blank=True, null=True, upload_to='Ganado', verbose_name='Imagen')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='Ganado', verbose_name='Imagen2')),
            ],
            options={
                'db_table': 'ganado',
            },
        ),
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('motivo', models.CharField(max_length=240)),
                ('monto', models.DecimalField(decimal_places=0, max_digits=10)),
                ('img', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'gastos',
            },
        ),
        migrations.CreateModel(
            name='InventarioAgricola',
            fields=[
                ('cultivo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('unidad_medida', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'inventario_agricola',
            },
        ),
        migrations.CreateModel(
            name='InventarioPorcino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'db_table': 'inventario_porcino',
            },
        ),
        migrations.CreateModel(
            name='MovimientosDya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=240)),
                ('monto', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fecha', models.DateField()),
                ('no', models.ForeignKey(db_column='no', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.DeudoresAcreedores')),
            ],
            options={
                'db_table': 'movimientos_dya',
            },
        ),
        migrations.CreateModel(
            name='Notificaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=240)),
                ('fecha', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'notificaciones',
            },
        ),
        migrations.CreateModel(
            name='PlaneacionAgricola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo', models.IntegerField()),
                ('cultivo', models.IntegerField()),
                ('hectareas', models.IntegerField()),
                ('costo', models.IntegerField()),
                ('produccion_estimada', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
            options={
                'db_table': 'planeacion_agricola',
            },
        ),
        migrations.CreateModel(
            name='PlaneacionBovina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_ganado', models.CharField(max_length=50)),
                ('hato', models.IntegerField()),
                ('venta', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
                ('ingreso_anual', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'planeacion_bovina',
            },
        ),
        migrations.CreateModel(
            name='PlaneacionLeche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacas_produccion', models.IntegerField()),
                ('produccion_promedio', models.IntegerField()),
                ('ingreso_diario', models.DecimalField(decimal_places=0, max_digits=10)),
                ('estimado_anual', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'planeacion_leche',
            },
        ),
        migrations.CreateModel(
            name='PlaneacionPorcina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cerdos', models.IntegerField()),
                ('lechones', models.IntegerField()),
                ('precio_venta', models.DecimalField(decimal_places=0, max_digits=10)),
                ('inversion', models.DecimalField(decimal_places=0, max_digits=10)),
                ('ingresos', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'planeacion_porcina',
            },
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('no_planeacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'planes',
            },
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hectareas', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('produccion_obtenida', models.IntegerField(blank=True, null=True)),
                ('unidad_medida', models.CharField(blank=True, max_length=20, null=True)),
                ('ciclo', models.IntegerField(choices=[(1, 1), (2, 2)])),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField(blank=True, null=True)),
                ('cultivo', models.ForeignKey(db_column='cultivo', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.InventarioAgricola')),
            ],
            options={
                'db_table': 'produccion',
            },
        ),
        migrations.CreateModel(
            name='ProyeccionGastos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_gasto', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('semanal', models.DecimalField(decimal_places=0, max_digits=10)),
                ('total_anual', models.DecimalField(decimal_places=0, max_digits=10)),
                ('eventual', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('no_planeacion', models.ForeignKey(db_column='no_planeacion', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.Planes')),
            ],
            options={
                'db_table': 'proyeccion_gastos',
            },
        ),
        migrations.CreateModel(
            name='VentaLeche',
            fields=[
                ('no_venta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'venta_leche',
            },
        ),
        migrations.CreateModel(
            name='VentasAgricola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=0, max_digits=11)),
                ('cultivo', models.ForeignKey(db_column='cultivo', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.InventarioAgricola')),
                ('no_venta', models.ForeignKey(db_column='no_venta', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.ControlVentasAgricolas')),
            ],
            options={
                'db_table': 'ventas_agricola',
            },
        ),
        migrations.CreateModel(
            name='VentasGanado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
                ('arete', models.ForeignKey(db_column='arete', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.Ganado')),
                ('no_venta', models.ForeignKey(db_column='no_venta', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.ControlVentaGanado')),
            ],
            options={
                'db_table': 'ventas_ganado',
            },
        ),
        migrations.CreateModel(
            name='VentasPorcinos',
            fields=[
                ('no_venta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio_unidad', models.DecimalField(decimal_places=0, max_digits=10)),
                ('total_venta', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fecha', models.DateField()),
                ('comprador', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'ventas_porcinos',
            },
        ),
        migrations.AddField(
            model_name='planeacionporcina',
            name='no_planeacion',
            field=models.ForeignKey(db_column='no_planeacion', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.Planes'),
        ),
        migrations.AddField(
            model_name='planeacionleche',
            name='no_planeacion',
            field=models.ForeignKey(db_column='no_planeacion', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.Planes'),
        ),
        migrations.AddField(
            model_name='planeacionbovina',
            name='no_planeacion',
            field=models.ForeignKey(db_column='no_planeacion', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.Planes'),
        ),
        migrations.AddField(
            model_name='planeacionagricola',
            name='no_planeacion',
            field=models.ForeignKey(db_column='no_planeacion', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.Planes'),
        ),
        migrations.AddField(
            model_name='controlganado',
            name='arete',
            field=models.ForeignKey(db_column='arete', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.Ganado'),
        ),
        migrations.AddField(
            model_name='comprasagricolas',
            name='cultivo',
            field=models.ForeignKey(db_column='cultivo', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.InventarioAgricola'),
        ),
        migrations.AddField(
            model_name='comprasagricolas',
            name='no_compra',
            field=models.ForeignKey(db_column='no_compra', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.ControlComprasAgricolas'),
        ),
        migrations.AddField(
            model_name='bitacoraganado',
            name='arete',
            field=models.ForeignKey(db_column='arete', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.Ganado'),
        ),
        migrations.AddField(
            model_name='bitacoraganado',
            name='no_registrob',
            field=models.ForeignKey(db_column='no_registrob', on_delete=django.db.models.deletion.DO_NOTHING, to='CRUD.ControlBitacoraGanado'),
        ),
    ]
