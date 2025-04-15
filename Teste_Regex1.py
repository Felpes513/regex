import re
import sys
import os

# Captura todas as linhas digitadas pelo usuário
if os.name == 'nt':
    print("Insira as informações (pressione Ctrl + Z e Enter para finalizar)")
else:
    print("Insira as informações (pressione Ctrl + D para finalizar)")

texto = sys.stdin.read()

# Expressões Regulares (apenas unidade)
padrao_data = r"data_exame:\s*([\d/]+\s[\d:]+)"
padrao_unidade = r"unidade:\s*(\S+)"
padrao_accession = r"accession_number:\s*([\w-]+)"
padrao_studies = r"studies_iuid:\s*([\d.]+)"

# Encontrando todos os exames
datas_exames = re.findall(padrao_data, texto)
unidades = re.findall(padrao_unidade, texto)
accession_numbers = re.findall(padrao_accession, texto)
studies_iuids = re.findall(padrao_studies, texto)

# Verificando se há exames encontrados
if datas_exames and unidades and studies_iuids and accession_numbers:
    print("\nDados extraídos:")

    unidade_anterior = unidades[0]
    for i in range(len(datas_exames)):
        print(f"\n Exame {i+1}:")
        print(f"Data do Exame: {datas_exames[i]}")
        print(f"Unidade: {unidades[i]}")
        print(f"Accession Number: {accession_numbers[i]}")
        print(f"Studies IUID: {studies_iuids[i]}")
else:
    print("\nNenhum exame encontrado! Verifique se os dados foram inseridos corretamente.")

# Visualização de resultado
input("\nPressione Enter para sair...")