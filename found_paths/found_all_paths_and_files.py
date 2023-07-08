import os
import subprocess
from pathlib import Path

nome_arquivo_de_testes = "EletraSDK-ZeusNG-Test.exe"
diretorio_base = os.getenv("ELETRA_SDK_HOME")
direct = Path(diretorio_base)

caminho_arquivo_de_testes = None

for caminho in direct.glob('**/' + nome_arquivo_de_testes):
    caminho_arquivo_de_testes = caminho
    break

if caminho_arquivo_de_testes:
    print("Caminho do arquivo com o nome do arquivo:", caminho_arquivo_de_testes)
else:
    print("O arquivo não foi encontrado.")

caminho_arquivo = None

caminhos_arquivos = list(direct.glob('**/' + nome_arquivo_de_testes))

if caminhos_arquivos:
    for caminho_arquivo in caminhos_arquivos:
        caminho_pasta = caminho_arquivo.parent
    print("Caminho do arquivo com sem nome do arquivo:",caminho_pasta)
else:
    print("Nenhum arquivo foi encontrado.")

###############################################################################################################
nome_arquivo_1 = "zeus_ng_dev.cpp"

caminho1 = None

caminhos_arquivos_1 = list(direct.glob('**/' + nome_arquivo_1))

if caminhos_arquivos_1:
    for caminho_arquivo in caminhos_arquivos_1:
        caminho_pasta_1 = caminho_arquivo.parent
    print("Caminho do arquivo com sem nome do arquivo do diretorio 1:",caminho_pasta_1)
else:
    print("Nenhum arquivo foi encontrado.")
###############################################################################################################

nome_arquivo_2 = "capture_objects_factory.cpp"

caminho2 = None

caminhos_arquivos_2 = list(direct.glob('**/' + nome_arquivo_2))

if caminhos_arquivos_2:
    for caminho_arquivo in caminhos_arquivos_2:
        caminho_pasta_2 = caminho_arquivo.parent
    print("Caminho do arquivo com sem nome do arquivo do diretorio 2:",caminho_pasta_2)
else:
    print("Nenhum arquivo foi encontrado.")
###############################################################################################################

nome_arquivo_3 = "get_date_time_log_data.cpp"

caminho3 = None

caminhos_arquivos_3 = list(direct.glob('**/' + nome_arquivo_3))

if caminhos_arquivos_3:
    for caminho_arquivo in caminhos_arquivos_3:
        caminho_pasta_3 = caminho_arquivo.parent
    print("Caminho do arquivo com sem nome do arquivo do diretorio 3:",caminho_pasta_3)
else:
    print("Nenhum arquivo foi encontrado.")
###############################################################################################################

nome_arquivo_4 = "zeus_ng_dlms_cmds_class_1.cpp"

caminho4 = None

caminhos_arquivos_4 = list(direct.glob('**/' + nome_arquivo_4))

if caminhos_arquivos_4:
    for caminho_arquivo in caminhos_arquivos_4:
        caminho_pasta_4 = caminho_arquivo.parent
    print("Caminho do arquivo com sem nome do arquivo do diretorio 4:",caminho_pasta_4)
else:
    print("Nenhum arquivo foi encontrado.")
###############################################################################################################

nome_arquivo_5 = "zeus_ng_services.cpp"

caminho5 = None

caminhos_arquivos_5 = list(direct.glob('**/' + nome_arquivo_5))

if caminhos_arquivos_5:
    for caminho_arquivo in caminhos_arquivos_5:
        caminho_pasta_5 = caminho_arquivo.parent
    print("Caminho do arquivo com sem nome do arquivo do diretorio 5:",caminho_pasta_5)
else:
    print("Nenhum arquivo foi encontrado.")
###############################################################################################################

nome_arquivo_6 = "get_alarms_parameters_services.cpp"

caminho6 = None

caminhos_arquivos_6 = list(direct.glob('**/' + nome_arquivo_6))

if caminhos_arquivos_6:
    for caminho_arquivo in caminhos_arquivos_6:
        caminho_pasta_6 = caminho_arquivo.parent
    print("Caminho do arquivo com sem nome do arquivo do diretorio 6:",caminho_pasta_6)
else:
    print("Nenhum arquivo foi encontrado.")
###############################################################################################################

comando = f'OpenCppCoverage.exe --sources={caminho_pasta_1} --sources={caminho_pasta_2} --sources={caminho_pasta_3} --sources={caminho_pasta_4} --sources={caminho_pasta_5} --sources={caminho_pasta_6} --export_type=html -- {caminho_arquivo_de_testes}'

subprocess.call(comando,shell=True)

