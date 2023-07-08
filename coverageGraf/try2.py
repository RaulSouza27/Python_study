import matplotlib.pyplot as plt

# Dados para o gráfico
categorias = ['Zeus', 'Zeus THS', 'Zeus NG', 'Recloser','House Water meter','Bulk Water meter','Cronos NG']
valores_anterior = [48, 36, 23, 79,76,72,65]
valores_atual = [48, 51, 55, 92,76,100,76]

# Configuração das barras
largura_barra = 0.35  # Largura das barras
posicao_categorias = range(len(categorias))  # Posição das categorias no eixo x

# Criar o gráfico de barras duplas
fig, ax = plt.subplots()
barra_anterior = ax.bar(posicao_categorias, valores_anterior, largura_barra, label='Anterior',color='#FF0000')
barra_atual = ax.bar([p + largura_barra for p in posicao_categorias], valores_atual, largura_barra, label='Atual',color='#00FF00')

# Adicionar os valores no topo de cada barra
for barra in barra_anterior + barra_atual:
    altura = barra.get_height()
    porc = f'{int(altura)}%'
    ax.text(barra.get_x() + barra.get_width() / 2, altura,porc, ha='center', va='bottom')

# Personalizar o gráfico
ax.set_title('Evolução das Coberturas de teste')
ax.set_xlabel('Devices')
ax.set_ylabel('Porcentagens %')
ax.set_xticks([p + largura_barra / 2 for p in posicao_categorias])
ax.set_xticklabels(categorias)
ax.legend()

# Exibir o gráfico
plt.show()