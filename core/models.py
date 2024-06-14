from django.db import models

class Pokemon(models.Model):
    nome_pokemon = models.CharField(max_length=30)
    imagem = models.BinaryField()


class Capacidades(models.Model):
    forca = models.IntegerField()
    inteligencia = models.IntegerField()
    salto = models.IntegerField()
    outras = models.CharField(max_length=30)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Deslocamento(models.Model):
    deslocamentos = models.CharField(max_length=60, default='N/A')    
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class GolpesNaturais(models.Model):
    evolucao = models.CharField(max_length=60)
    golpe_01 = models.CharField(max_length=60)
    golpe_02 = models.CharField(max_length=60, null=True)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    

class AtributosBasais(models.Model):
    saude =  models.CharField(max_length=60, default='N/A')
    ataque = models.CharField(max_length=60,  default='N/A')
    defesa =  models.CharField(max_length=60, default='N/A')
    ataque_especial =  models.CharField(max_length=60, default='N/A')
    defesa_especial = models.CharField(max_length=60, default='N/A')
    velocidade =  models.CharField(max_length=60, default='N/A')
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class TiposHabilidades(models.Model):
    tipo_01_img = models.ImageField(upload_to=None, height_field=None, width_field=None, null=True)
    tipo_02_img = models.ImageField(upload_to=None, height_field=None, width_field=None, null=True)
    habilidade = models.CharField(max_length=60)
    alta_habilidade = models.CharField(max_length=60, null=True)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Comportamento(models.Model):
    dieta_01 = models.CharField(max_length=60)
    dieta_02 = models.CharField(max_length=60, null=True)
    habitat_01 = models.CharField(max_length=60)
    habitat_02 = models.CharField(max_length=60, null=True)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Narrador(models.Model):
    chance_captura = models.IntegerField()
    experiencia = models.IntegerField()
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Medidas(models.Model):
    tamanho_01 =  models.CharField(max_length=60)
    tamanho_02 =  models.CharField(max_length=60, null=True)
    categoria_01 = models.CharField(max_length=60)
    categoria_02 = models.CharField(max_length=60, null=True)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Procriacao(models.Model):
    sexo =  models.CharField(max_length=60)
    grupo_reprodutivo =  models.CharField(max_length=60)
    incubacao =  models.CharField(max_length=60)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)