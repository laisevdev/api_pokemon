# Generated by Django 5.0.6 on 2024-06-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_tiposhabilidades_tipo_01_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='imagem',
            field=models.ImageField(upload_to='imgs/'),
        ),
    ]