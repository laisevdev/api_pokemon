from django.db import models

class Pokemon(models.Model):
    nome_pokemon = models.CharField(max_length=100)
    imagem = models.ImageField()


class Capacidades(models.Model):
    forca = models.IntegerField()
    inteligencia = models.IntegerField()
    salto = models.IntegerField()
    outras = models.CharField(max_length=100)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Deslocamento(models.Model):
    deslocamentos = models.CharField(max_length=100, default='N/A')    
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class GolpesNaturais(models.Model):
    golpe_natural = models.CharField(max_length=100)
    golpe_herdado = models.CharField(max_length=200, null=True)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    

class AtributosBasais(models.Model):
    saude =  models.CharField(max_length=100, default='N/A')
    ataque = models.CharField(max_length=100,  default='N/A')
    defesa =  models.CharField(max_length=100, default='N/A')
    ataque_especial =  models.CharField(max_length=100, default='N/A')
    defesa_especial = models.CharField(max_length=100, default='N/A')
    velocidade =  models.CharField(max_length=100, default='N/A')
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class TiposHabilidades(models.Model):
    tipo_01_img = models.ImageField()
    habilidade = models.CharField(max_length=100)
    alta_habilidade = models.CharField(max_length=100, null=True)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Comportamento(models.Model):
    dieta = models.CharField(max_length=100, null=True)
    habitat = models.CharField(max_length=100, null=True)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Narrador(models.Model):
    chance_captura = models.IntegerField()
    experiencia = models.IntegerField()
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Medidas(models.Model):
    tamanho =  models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

class Procriacao(models.Model):
    sexo =  models.CharField(max_length=100)
    grupo_reprodutivo =  models.CharField(max_length=100)
    incubacao =  models.CharField(max_length=100)
    id_pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)