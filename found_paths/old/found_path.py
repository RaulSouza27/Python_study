import os

def find_index_html(start_path):
    for root, dirs, files in os.walk(start_path):
        if 'index.html' in files:
            return os.path.join(root, 'index.html')
    return None

# Defina o caminho inicial onde a pasta 'build' deve estar localizada
start_path = './build'
index_html_path = find_index_html(start_path)

if index_html_path:
    print(f"Arquivo encontrado em: {index_html_path}")
else:
    print("Arquivo index.html não encontrado.")
