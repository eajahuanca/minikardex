# Generated by Django 4.1.2 on 2022-10-05 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('categoria', models.CharField(max_length=50, unique=True, verbose_name='Categoria')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('producto', models.CharField(max_length=100, verbose_name='Nombre del Producto')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('imagen', models.ImageField(upload_to='productos/', verbose_name='Imagen del Producto')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock del Producto')),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Costo del Producto $us')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado Actual')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
                ('tipoproducto', models.CharField(max_length=50, unique=True, verbose_name='Tipo de Producto')),
                ('descripcion', models.CharField(max_length=150, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo de Producto',
                'verbose_name_plural': 'Tipos de Productos',
            },
        ),
    ]