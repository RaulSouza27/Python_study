import subprocess
from pathlib import Path

diretorio_base = Path("C:\Dev\Eletra-SDK")
nome_arquivo = "EletraSDK-ZeusNG-Test.exe"

caminho_arquivo = None

for caminho in diretorio_base.glob('**/' + nome_arquivo):
    caminho_arquivo = caminho
    break

if caminho_arquivo:
    print("Caminho do arquivo com o nome do arquivo:", caminho_arquivo)
else:
    print("O arquivo não foi encontrado.")

caminhos_arquivos = list(diretorio_base.glob('**/' + nome_arquivo))

if caminhos_arquivos:
    for caminho_arquivo in caminhos_arquivos:
        caminho_pasta = caminho_arquivo.parent
    print("Caminho do arquivo com sem nome do arquivo:",caminho_pasta)
else:
    print("Nenhum arquivo foi encontrado.")