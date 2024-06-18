import os
import openpyxl
from core.models import Pokemon, Capacidades, Comportamento, Deslocamento, GolpesNaturais, AtributosBasais, TiposHabilidades, Medidas, Narrador, Procriacao
from django.core.files import File

# Caminhos para a planilha e as imagens
excel_path = 'poke_atributos.xlsx'
project_path = 'core' 
images_path = os.path.join(project_path, 'imagens', 'poke_imagens/')
images_path_02 = os.path.join(project_path, 'imagens', 'tipos/')  

# Verificar se os caminhos existem
if not os.path.exists(excel_path):
    raise FileNotFoundError(f"Planilha não encontrada: {excel_path}")

if not os.path.isdir(images_path):
    raise NotADirectoryError(f"Diretório de imagens não encontrado: {images_path}")

if not os.path.isdir(images_path_02):
    raise NotADirectoryError(f"Diretório de imagens para tipo 02 não encontrado: {images_path_02}")

# Abrir a planilha
wb = openpyxl.load_workbook(excel_path)
ws = wb.active

# Função auxiliar para truncar strings longas
def truncate_string(value, max_length):
    if isinstance(value, str) and len(value) > max_length:
        print(f"Valor truncado: {value}")
        return value[:max_length]
    return value

# Função auxiliar para remover '[]' dos caminhos das imagens
'''
def remove_brackets(images_path_02):
    if images_path_02.startswith("['") and images_path_02.endswith("']"):
        return images_path_02[2:-2]
    return images_path_02
'''

# Iterar sobre as linhas da planilha e adicionar ao banco de dados
for row in ws.iter_rows(min_row=2, values_only=True):
    nome_pokemon, imagem, saude, ataque, defesa, ataque_especial, defesa_especial, velocidade,  tipo_01_img, forca, inteligencia, salto, outras, habilidade, alta_habilidade, deslocamentos, tamanho, categoria, sexo, grupo_reprodutivo, incubacao, golpe_natural, golpe_herdado, dieta, habitat, chance_captura, experiencia = row  # Ajuste conforme as colunas da sua planilha

     # Limpar os caminhos das imagens
    #tipo_01_img = remove_brackets(tipo_01_img)

    # Verificar se o arquivo de imagem existe
    image_path = os.path.join(images_path, imagem)
    if not os.path.exists(image_path):
        print(f"Imagem não encontrada: {images_path}")
        continue

     # Verificar se o segundo arquivo de imagem existe
    tipo_01_image_path = os.path.join(images_path_02, tipo_01_img)

     # Truncar strings longas
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

    # Criar ou obter o Pokemon
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

    tipos_habilidades = TiposHabilidades.objects.create(habilidade=habilidade, alta_habilidade=alta_habilidade, id_pokemon=pokemon)
    if os.path.exists(tipo_01_image_path):
        with open(images_path_02, 'rb') as img_file:
            tipos_habilidades.tipo_01_img.save(tipo_01_img, File(img_file))
            tipos_habilidades.save()

    Medidas.objects.create(tamanho=tamanho, categoria=categoria, id_pokemon=pokemon)
    Narrador.objects.create(chance_captura=chance_captura, experiencia=experiencia, id_pokemon=pokemon)
    Procriacao.objects.create(sexo=sexo, grupo_reprodutivo=grupo_reprodutivo, incubacao=incubacao, id_pokemon=pokemon)

   