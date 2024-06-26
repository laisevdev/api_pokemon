# Generated by Django 5.0.6 on 2024-06-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_pokemon_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atributosbasais',
            name='atributo_01',
        ),
        migrations.RemoveField(
            model_name='atributosbasais',
            name='atributo_02',
        ),
        migrations.RemoveField(
            model_name='atributosbasais',
            name='nome_atributo',
        ),
        migrations.RemoveField(
            model_name='atributosbasais',
            name='nome_pokemon_01',
        ),
        migrations.RemoveField(
            model_name='atributosbasais',
            name='nome_pokemon_02',
        ),
        migrations.RemoveField(
            model_name='deslocamento',
            name='escavacao',
        ),
        migrations.RemoveField(
            model_name='deslocamento',
            name='natacao',
        ),
        migrations.RemoveField(
            model_name='deslocamento',
            name='subaquatico',
        ),
        migrations.RemoveField(
            model_name='deslocamento',
            name='terrestre',
        ),
        migrations.RemoveField(
            model_name='deslocamento',
            name='voo',
        ),
        migrations.AddField(
            model_name='atributosbasais',
            name='ataque',
            field=models.CharField(default='N/A', max_length=60),
        ),
        migrations.AddField(
            model_name='atributosbasais',
            name='ataque_especial',
            field=models.CharField(default='N/A', max_length=60),
        ),
        migrations.AddField(
            model_name='atributosbasais',
            name='defesa',
            field=models.CharField(default='N/A', max_length=60),
        ),
        migrations.AddField(
            model_name='atributosbasais',
            name='defesa_especial',
            field=models.CharField(default='N/A', max_length=60),
        ),
        migrations.AddField(
            model_name='atributosbasais',
            name='saude',
            field=models.CharField(default='N/A', max_length=60),
        ),
        migrations.AddField(
            model_name='atributosbasais',
            name='velocidade',
            field=models.CharField(default='N/A', max_length=60),
        ),
        migrations.AddField(
            model_name='deslocamento',
            name='deslocamentos',
            field=models.CharField(default='N/A', max_length=60),
        ),
    ]
