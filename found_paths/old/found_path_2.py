import os
import subprocess
from pathlib import Path

OpenCppCoverage = Path(os.getenv("OpenCppCoverage.exe"))

base_directory = Path(os.getcwd())

def found_file(direct, file_name):
    path_files = list(direct.glob('**/' + file_name))
    path = path_files[-1]
    return path

def found_directory_path(direct, file_name):
    path_files = list(direct.glob('**/' + file_name))
    if path_files:
        path = path_files[-1].parent  # Pega o último arquivo encontrado
        print(f"Caminho do arquivo com sem nome do arquivo: {path}")
        return path
    else:
        print("File not found.")
        return None

# Exemplo de como usar a função
file_name_4 = "Calculator.cpp"
path_1 = found_directory_path(base_directory, file_name_4)

test_exe = "EletraCITests.exe"
path_2 = found_file(base_directory, test_exe)

def extract_coverage(path_1, path_2):
    if path_1 and path_2:
        cmd = [OpenCppCoverage, "--sources=" + str(path_1), "--export_type=cobertura:calculator_coverage", "--",str(path_2)]
        subprocess.run(cmd,shell=True)
    else:
        print("ERROR")

try:
    extract_coverage(path_1, path_2)
except Exception as e:
    print("O erro foi ->", e)

