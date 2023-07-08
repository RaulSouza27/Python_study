###################################################################
#   COMANDO PARA ACHAR APENAS OS CAMINHOS DOS ARQUIVOS + ARQUIVO  #
###################################################################
import subprocess
from pathlib import Path

diretorio_base = Path("C:\Dev\Eletra-SDK")
nome_arquivo = "EletraSDK-ZeusNG-Test.exe"

caminho_arquivo = None

for caminho in diretorio_base.glob('**/' + nome_arquivo):
    caminho_arquivo = caminho
    break

if caminho_arquivo:
    print("Caminho do arquivo encontrado:", caminho_arquivo)
else:
    print("O arquivo não foi encontrado.")

# comando = f'OpenCppCoverage.exe --sources=%ELETRA_SDK_HOME%\source\libraries\zeus_ng\src\services\zeus_ng --sources=%ELETRA_SDK_HOME%\source\libraries\zeus_ng\src\services\zeus_ng\commands --sources=%ELETRA_SDK_HOME%\source\libraries\zeus_ng\src\zeus_ng --sources=%ELETRA_SDK_HOME%\source\libraries\zeus_ng\src\zeus_ng\commands --sources=%ELETRA_SDK_HOME%\source\libraries\zeus_ng\src\zeus_ng\models --sources=%ELETRA_SDK_HOME%\source\libraries\zeus_ng\src\zeus_ng\models\permanent_change_log --export_type=html -- {caminho_arquivo}'

# subprocess.call(comando,shell=True)