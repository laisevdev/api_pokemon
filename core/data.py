import os
import openpyxl
from core.models import Pokemon, Capacidades, Comportamento, Deslocamento, GolpesNaturais, AtributosBasais, TiposHabilidades, Medidas, Narrador, Procriacao
from django.core.files import File


excel_path = 'poke_atributos.xlsx'
project_path = 'core' 
images_path = os.path.join(project_path, 'imagens', 'poke_imagens/')


if not os.path.exists(excel_path):
    raise FileNotFoundError(f"Planilha não encontrada: {excel_path}")

if not os.path.isdir(images_path):
    raise NotADirectoryError(f"Diretório de imagens não encontrado: {images_path}")


wb = openpyxl.load_workbook(excel_path)
ws = wb.active


def truncate_string(value, max_length):
    if isinstance(value, str) and len(value) > max_length:
        print(f"Valor truncado: {value}")
        return value[:max_length]
    return value


for row in ws.iter_rows(min_row=2, values_only=True):
    nome_pokemon, imagem, saude, ataque, defesa, ataque_especial, defesa_especial, velocidade,  tipo_01_img, tipo_02_img, forca, inteligencia, salto, outras, habilidade, alta_habilidade, deslocamentos, tamanho, categoria, sexo, grupo_reprodutivo, incubacao, golpe_natural, golpe_herdado, dieta, habitat, chance_captura, experiencia = row  


    image_path = os.path.join(images_path, imagem)
    if not os.path.exists(image_path):
        print(f"Imagem não encontrada: {images_path}")
        continue


    nome_pokemon = truncate_string(nome_pokemon, 200)
    outras = truncate_string(outras, 200)
    deslocamentos = truncate_string(deslocamentos, 200)
    golpe_natural = truncate_string(golpe_natural, 200)
    golpe_herdado = truncate_string(golpe_herdado, 300)
    saude = truncate_string(saude, 200)
    ataque = truncate_string(ataque, 200)
    defesa = truncate_string(defesa, 200)
    ataque_especial = truncate_string(ataque_especial, 200)
    defesa_especial = truncate_string(defesa_especial, 200)
    velocidade = truncate_string(velocidade, 200)
    habilidade = truncate_string(habilidade, 200)
    alta_habilidade = truncate_string(alta_habilidade, 200)
    dieta = truncate_string(dieta, 200)
    habitat = truncate_string(habitat, 200)
    tamanho = truncate_string(tamanho, 200)
    categoria = truncate_string(categoria, 200)
    sexo = truncate_string(sexo, 200)
    grupo_reprodutivo = truncate_string(grupo_reprodutivo, 200)
    incubacao = truncate_string(incubacao, 200)
    tipo_01_img = truncate_string(tipo_01_img, 300)
    tipo_02_img = truncate_string(tipo_02_img, 300)


    with open(image_path, 'rb') as img_file:
        pokemon, created = Pokemon.objects.get_or_create(nome_pokemon=nome_pokemon, imagem=imagem)
        if created:
            pokemon.imagem.save(imagem, File(img_file))
            pokemon.save()

    Capacidades.objects.create(forca=forca, inteligencia=inteligencia, salto=salto, outras=outras, id_pokemon=pokemon)
    Comportamento.objects.create(dieta=dieta, habitat=habitat, id_pokemon=pokemon)
    Deslocamento.objects.create(deslocamentos=deslocamentos, id_pokemon=pokemon)
    GolpesNaturais.objects.create(golpe_natural=golpe_natural, golpe_herdado=golpe_herdado, id_pokemon=pokemon)
    AtributosBasais.objects.create(saude=saude, ataque=ataque, defesa=defesa, ataque_especial=ataque_especial, defesa_especial=defesa_especial, velocidade=velocidade, id_pokemon=pokemon)
    TiposHabilidades.objects.create(habilidade=habilidade, alta_habilidade=alta_habilidade, tipo_01_img=tipo_01_img, tipo_02_img=tipo_02_img, id_pokemon=pokemon)
    Medidas.objects.create(tamanho=tamanho, categoria=categoria, id_pokemon=pokemon)
    Narrador.objects.create(chance_captura=chance_captura, experiencia=experiencia, id_pokemon=pokemon)
    Procriacao.objects.create(sexo=sexo, grupo_reprodutivo=grupo_reprodutivo, incubacao=incubacao, id_pokemon=pokemon)   