# Generated by Django 5.0.6 on 2024-06-15 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_categoria_01_medidas_categoria_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='golpesnaturais',
            old_name='golpe_02',
            new_name='golpe_herdado',
        ),
        migrations.RenameField(
            model_name='golpesnaturais',
            old_name='evolucao',
            new_name='golpe_natural',
        ),
        migrations.RemoveField(
            model_name='golpesnaturais',
            name='golpe_01',
        ),
    ]
