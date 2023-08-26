# Generated by Django 4.2.4 on 2023-08-25 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio_proveedor',
        ),
        migrations.AddField(
            model_name='factura',
            name='pendiente',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('res', 'Res'), ('pollo', 'Pollo'), ('cerdo', 'Cerdo'), ('embutido', 'Embutido')], default='res', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='productos_ofrecidos',
            field=models.ManyToManyField(related_name='proveedores', to='facturas.producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productos_relacionados', to='facturas.proveedor'),
        ),
    ]
