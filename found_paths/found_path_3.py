#########################################################
#   COMANDO PARA ACHAR APENAS OS CAMINHOS DOS ARQUIVOS  #
#########################################################
from pathlib import Path

diretorio_base = Path("C:\Dev\Eletra-SDK")
padrao_nome_arquivo = "EletraSDK-ZeusNG-Test.exe"

caminhos_arquivos = list(diretorio_base.glob('**/' + padrao_nome_arquivo))

if caminhos_arquivos:
    for caminho_arquivo in caminhos_arquivos:
        caminho_pasta = caminho_arquivo.parent
    print(caminho_pasta)
else:
    print("Nenhum arquivo foi encontrado.")
