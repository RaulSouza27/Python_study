import os
import subprocess
from pathlib import Path

nome_arquivo_de_testes = "EletraSDK-ZeusNG-Test.exe"
diretorio_base = os.getenv("ELETRA_SDK_HOME")
direct = Path(diretorio_base)