# Generated by Django 3.2.4 on 2021-07-07 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datos',
            fields=[
                ('rutcola', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=30, verbose_name='Direccion')),
                ('email', models.CharField(max_length=10, verbose_name='Email')),
                ('pais', models.CharField(max_length=10, verbose_name='pais')),
                ('contrasena', models.CharField(max_length=20, verbose_name='contrasena')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('Correo', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Correo')),
                ('Nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('Detalles', models.CharField(max_length=150, verbose_name='Detalles')),
                ('rutcola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.datos')),
            ],
        ),
    ]
