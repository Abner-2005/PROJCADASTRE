# Generated by Django 4.1.2 on 2022-11-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dpedidos',
            name='status',
            field=models.CharField(choices=[('PP', 'pedido em processo'), ('PR', 'pedido realizado'), ('PE', 'pedido entregue')], max_length=2),
        ),
    ]
