# Generated by Django 3.0.7 on 2020-11-29 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Registrar Datos Del Conductor',
                'verbose_name_plural': 'Registrar Datos De los Conductores',
            },
        ),
        migrations.CreateModel(
            name='TipoTransporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transporte', models.CharField(max_length=100, verbose_name='Tipo Transporte')),
            ],
            options={
                'verbose_name': 'Registrar Datos Del Transporte',
                'verbose_name_plural': 'Registrar Datos De los Transportes',
            },
        ),
    ]