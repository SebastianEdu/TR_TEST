# Generated by Django 3.1.2 on 2021-11-02 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Turismo_core', '0006_auto_20211101_2352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='cod_invetario',
            new_name='cod_inventario',
        ),
    ]
