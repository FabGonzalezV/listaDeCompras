# Generated by Django 4.1.5 on 2023-01-29 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0005_listproducts_status_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listproducts',
            old_name='_id_list',
            new_name='id',
        ),
    ]