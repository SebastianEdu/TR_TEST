# Generated by Django 3.1.2 on 2021-11-02 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Turismo_core', '0005_auto_20211101_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='check_inv2_cod_chek_in',
            field=models.ForeignKey(db_column='check_inv2_cod_chek_in', default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Turismo_core.checkinv1'),
        ),
    ]
