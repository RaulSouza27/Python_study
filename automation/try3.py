import matplotlib.pyplot as plt

with open('C:\\Dev\\Python_study\\automation\\numbers.txt','r') as arquivo:
    linhas = arquivo.read()

vec = ['vendedor1','vendedor2','vendedor3','vendedor4']
vendas = [int(linha) for linha in linhas.split(',')]
vendedores = range(len(vec))

fig, ax = plt.subplots()
barras_vendas = ax.bar(vendedores,vendas,0.4,color='#FF0083')

ax.set_title('Evolução de Vendas')
ax.set_xlabel('Vendedores')
ax.set_xticks(vendedores)
ax.set_xticklabels(vec)

plt.show()