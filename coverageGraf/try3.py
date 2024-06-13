import matplotlib.pyplot as plt

# Dados para o gráfico
categorias = ['Total Lines', 'Not Coverage Lines', 'Coverage Lines']
valores = [2604, 1331, 1273]  # Valores para cada categoria

# Configurações das barras
largura_barra = 0.5  # Largura das barras
posicao_categorias = range(len(categorias))  # Posição das categorias no eixo x

# Criar o gráfico de barras
fig, ax = plt.subplots()
barras = ax.bar(posicao_categorias, valores, largura_barra, color=['#C0C0C0', '#FF0000', '#00FF00'])

# Adicionar os valores no topo de cada barra
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2, altura, f'{altura}', ha='center', va='bottom')

# Personalizar o gráfico
ax.set_title('Gateway Coverage Graf')
ax.set_ylabel('Values')
ax.set_ylim(0, 2800)  # Define o valor máximo do eixo y como 100
ax.set_xticks(posicao_categorias)
ax.set_xticklabels(categorias)

# Exibir o gráfico
plt.show()
