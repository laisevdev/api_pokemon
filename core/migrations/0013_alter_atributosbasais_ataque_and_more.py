# Generated by Django 5.0.6 on 2024-06-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_tiposhabilidades_tipo_02_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atributosbasais',
            name='ataque',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='atributosbasais',
            name='ataque_especial',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='atributosbasais',
            name='defesa',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='atributosbasais',
            name='defesa_especial',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='atributosbasais',
            name='saude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='atributosbasais',
            name='velocidade',
            field=models.IntegerField(),
        ),
    ]
