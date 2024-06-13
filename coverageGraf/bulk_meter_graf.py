import matplotlib.pyplot as plt

# Dados para o gráfico
categorias = ['Total Lines', 'Uncoverage Lines', 'Coverage Lines']
valores_anterior = [84, 84, 84]
valores_atual = [12, 12, 12]

# Configuração das barras
largura_barra = 0.35  # Largura das barras
posicao_categorias = range(len(categorias))  # Posição das categorias no eixo x

# Criar o gráfico de barras duplas
fig, ax = plt.subplots()
barra_anterior = ax.bar(posicao_categorias, valores_anterior, largura_barra, label='Anterior',color='#00000')
barra_atual = ax.bar([p + largura_barra for p in posicao_categorias], valores_atual, largura_barra, label='Atual',color='#00FF00')

# Adicionar os valores no topo de cada barra
for barra in barra_anterior + barra_atual:
    altura = barra.get_height()
    porc = f'{int(altura)}%'
    ax.text(barra.get_x() + barra.get_width() / 2, altura,porc, ha='center', va='bottom')

# Personalizar o gráfico
ax.set_title('BulkMeter Coverage Tests')
# ax.set_xlabel('Devices')
ax.set_ylabel('Porcentagens %')
ax.set_xticks([p + largura_barra / 2 for p in posicao_categorias])
ax.set_xticklabels(categorias)
ax.legend()

# Exibir o gráfico
plt.show()