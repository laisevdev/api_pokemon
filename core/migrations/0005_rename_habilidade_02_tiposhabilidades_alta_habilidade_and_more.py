# Generated by Django 5.0.6 on 2024-06-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_atributosbasais_atributo_01_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiposhabilidades',
            old_name='habilidade_02',
            new_name='alta_habilidade',
        ),
        migrations.RenameField(
            model_name='tiposhabilidades',
            old_name='habilidade_01',
            new_name='habilidade',
        ),
        migrations.RenameField(
            model_name='tiposhabilidades',
            old_name='tipo_02',
            new_name='tipo_01_img',
        ),
        migrations.RemoveField(
            model_name='tiposhabilidades',
            name='tipo_01',
        ),
        migrations.AddField(
            model_name='tiposhabilidades',
            name='tipo_02_img',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]