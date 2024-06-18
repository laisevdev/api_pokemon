from django.db import models

class Pokemon(models.Model):
    nome_pokemon = models.CharField(max_length=200)
    imagem = models.ImageField()


class Capacidades(models.Model):
    forca = models.IntegerField()
    inteligencia = models.IntegerField()
    salto = models.IntegerField()
    outras = models.CharField(max_length=200)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Deslocamento(models.Model):
    deslocamentos = models.CharField(max_length=200, default='N/A')    
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class GolpesNaturais(models.Model):
    golpe_natural = models.CharField(max_length=200)
    golpe_herdado = models.CharField(max_length=300, null=True)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    

class AtributosBasais(models.Model):
    saude =  models.IntegerField()
    ataque = models.IntegerField()
    defesa = models.IntegerField()
    ataque_especial =  models.IntegerField()
    defesa_especial = models.IntegerField()
    velocidade =  models.IntegerField()
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class TiposHabilidades(models.Model):
    tipo_01_img = models.ImageField(upload_to='tipos_images/', max_length=300)
    habilidade = models.CharField(max_length=200)
    alta_habilidade = models.CharField(max_length=200, null=True)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Comportamento(models.Model):
    dieta = models.CharField(max_length=200, null=True)
    habitat = models.CharField(max_length=200, null=True)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Narrador(models.Model):
    chance_captura = models.IntegerField()
    experiencia = models.IntegerField()
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Medidas(models.Model):
    tamanho =  models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Procriacao(models.Model):
    sexo =  models.CharField(max_length=200)
    grupo_reprodutivo =  models.CharField(max_length=200)
    incubacao =  models.CharField(max_length=200)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)