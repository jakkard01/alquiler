# Generated by Django 5.0.1 on 2024-01-22 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='productos/')),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
