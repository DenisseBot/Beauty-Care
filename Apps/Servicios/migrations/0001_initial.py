# Generated by Django 2.2.6 on 2019-10-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=100)),
                ('descripcion_servicio', models.TextField()),
                ('imagen_servicio', models.ImageField(default='servicios/tidusHahaha.jpg', upload_to='servicios/')),
            ],
        ),
    ]
