import os
import zipfile

def main():
    # Diretórios onde estão os arquivos que você deseja zipar
    paths_to_files = ['./test/file1.txt', './test/file2.txt', './test/file3.txt']

    # Nome do arquivo ZIP a ser criado
    zip_file_name = 'test.zip'

    # Cria um objeto ZipFile para escrever no arquivo ZIP
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona cada arquivo ao arquivo ZIP
        for file_path in paths_to_files:
            # Obtém o nome do arquivo do caminho completo
            file_name = os.path.basename(file_path)
            # Adiciona o arquivo ao ZIP, usando o nome do arquivo como arcname
            zipf.write(file_path, arcname=file_name)

    print(f'Os arquivos foram zipados com sucesso para "{zip_file_name}".')

if __name__ == "__main__":
    main()
