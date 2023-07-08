from pathlib import Path

diretorio = Path("C:\Dev\Eletra-SDK\\build\win-dbg\source\libraries\zeus_ng\\tests")
nome_arquivo = "EletraSDK-ZeusNG-Test.exe"

caminho_arquivo = diretorio / nome_arquivo

if caminho_arquivo.exists():
    print("Caminho do arquivo encontrado:", caminho_arquivo)
else:
    print("O arquivo não foi encontrado.")
