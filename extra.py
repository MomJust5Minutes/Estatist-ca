#!/usr/bin/env python
# coding: utf-8

# # **`CONTEÚDO EXTRA`**
# 
# 
# 
# 

# Comandos inseridos para estudo da correlação entre várias váriáveis simultaneamente.

# In[18]:


#Importando as bibliotecas

import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from scipy.stats import linregress


# In[19]:


#Definindo a variável "arquivo" pelo nome da planilha.

arquivo ='energia sustentável 1_CompletaFiltrada.xlsx'
fossil = 'Eletricidade a partir de combustíveis fósseis (TWh)'
emissao = 'Emissões de dióxido de carbono por pessoa em toneladas métricas.'


# In[20]:


#lendo a planilha no Python. Escolhemos o nome df para armazenar.

df=pd.read_excel(arquivo)


# # Matriz dos coeficientes de correlação - método corr() do Pandas
# 
# Quando o Data Set estudado tem mais de duas variáveis quantitativas, podemos estudar o coeficiente de correlação de forma simultânea de todas as variáveis quantitativas.

# In[21]:


#Apresenta a matriz de correlação linear duas a duas das variáveis quantitativas do Data Set.
df.corr()


# # Diagramas de dispersão simultâneos - sns.pairplot()
# 
# É possível plotar os diagramas de dispersão das variáveis quantitativas duas a duas simultaneamente.

# In[22]:


sns.pairplot(data=df)
plt.show()


# In[23]:


# Ajustando a altura para adequar o gráfico à tela.
sns.pairplot(data=df,height=3)
plt.show()


# # Heatmap (mapa de calor) dos coeficientes de correlação
# 
# Podemos contruir uma tabela de escala de cores dependendo do valor do coeficiente de correlação r.
# 

# In[24]:


#Matriz de correlação do Data Set
matrizcorrelacao = df.corr()
matrizcorrelacao


# #Matriz de correlação
# 
# Mapa de calor (heatmap).

# In[25]:


# Mapa de Calor (heatmap) básico
sns.heatmap(matrizcorrelacao)
plt.show()


# In[26]:


# Heatmap exibindo os valores de r
sns.heatmap(matrizcorrelacao, annot = True)
plt.show()


# In[27]:


# Alterar o número de casas decimais de heatmap
sns.heatmap(matrizcorrelacao, annot = True, fmt=".1f")
plt.show()


# In[28]:


# Ajustar a espessura/largura das linhas do heatmap
sns.heatmap(matrizcorrelacao, annot = True, fmt=".2f", linewidths=0.6)
plt.show()


# #Tendência linear positiva e negativa
# 
# Gerando um Heatmap para análise de tendência linear dos dados.

# In[29]:


# Posicionando o centro no zero na barra de referência do heatmap
# ATENÇÃO: se você não posicionar em zero, a função vai centralizar no ponto
# médio dos dados disponíveis, o que pode distorcer a interpretação
sns.heatmap(matrizcorrelacao, annot = True, fmt=".2f", linewidths=0.6, center=0)
plt.show()


# In[30]:


# Escolhendo heatmap variando de azul para vermelho (cmap = "bwr")
# para ver lista de cores pesquise por "choosing colormaps in matplotlib"
sns.heatmap(matrizcorrelacao, annot = True, fmt=".2f", linewidths=0.6, center = 0, cmap= "bwr")
plt.show()


# In[31]:


# É uma boa prática, quando possível, estabelecer os valores min e max
# Neste caso, é importante para evitar distorções
sns.heatmap(matrizcorrelacao, annot = True, fmt=".2f", linewidths=0.6, center = 0, vmin=-1, vmax=1, cmap= "RdYlBu")
plt.show()


# In[32]:


# Separando positivos e negativos (abaixo e acima do centro)
# Basta passar uma lista de cores
sns.heatmap(matrizcorrelacao, annot = True, fmt=".2f", linewidths=0.6, center = 0, cmap=["Red", "Blue"])
plt.show()


# #Análise de correlação/regressão linear para o par correspondente
# 
# Análise de correlação/regressão linear do par:
# 
# | Eletricidade a partir de combustíveis fósseis (TWh) |
# 
# | Emissões de dióxido de carbono por pessoa em toneladas métricas |
# 
# (melhores valores para análise, pois possuem r mais perto de 1)
# 

# **3.a)** Coeficiente de determinação (ou explicação)
# 

# In[34]:


# Suponha que você tenha um DataFrame chamado 'df' com suas variáveis
# Substitua 'x' e 'y' pelos nomes das variáveis que você deseja analisar

x = df[fossil]
y = df[emissao]

# Calcular o coeficiente de correlação (r)
correlation_coefficient = np.corrcoef(x, y)[0, 1]

# Calcular o coeficiente de determinação (r²)
coefficient_of_determination = correlation_coefficient ** 2

print(f"Coeficiente de Correlação (r): {correlation_coefficient:.2f}")
print(f"Coeficiente de Determinação (r²): {coefficient_of_determination:.4f}")


# **3.b)** Diagrama de dispersão

# In[72]:


# Cria um gráfico de dispersão usando a função sns.scatterplot()
plt.rcParams["figure.figsize"]=(9,5.5)
sns.scatterplot(x=df[fossil], y=df[emissao], data=df)

# Personaliza o gráfico
plt.xlabel('Eletricidade a partir de combustíveis fósseis (TWh)')
plt.ylabel('Emissões de dióxido de carbono por pessoa em toneladas métricas')
plt.title('Diagrama de Dispersão Entre X e Y')


# Exibe o gráfico
plt.show()


# **3.c)** Reta de regressão

# In[73]:


x = df[fossil]
y = df[emissao]

# Calcula os coeficientes da regressão linear
coefficients = np.polyfit(x, y, 1)
slope = coefficients[0]
intercept = coefficients[1]

# Cria a reta de regressão usando os coeficientes
regression_line = slope * x + intercept

# Cria o gráfico apenas da reta de regressão
plt.rcParams["figure.figsize"]=(9,5.5)
plt.plot(x, regression_line, color='red', label='Reta de Regressão')

# Personaliza o gráfico (rótulos de eixo, título, legenda, etc.)
plt.xlabel('Eletricidade a partir de combustiveis fosseis (TWh)')
plt.ylabel('Emissões de dióxido de carbono por pessoa em toneladas métricas')
plt.title('Reta de Regressão')
plt.legend()

# Exibe o gráfico
plt.show()


# **3.d)** Gráfico com diagrama de dispersão e reta de regressão

# In[74]:


x = df[fossil]
y = df[emissao]

# Calcula os coeficientes da regressão linear
coefficients = np.polyfit(x, y, 1)
slope = coefficients[0]
intercept = coefficients[1]

# Cria a reta de regressão usando os coeficientes
regression_line = slope * x + intercept

# Cria o gráfico de dispersão
plt.rcParams["figure.figsize"]=(9,5.5)
plt.scatter(x, y, label='Dados')

# Plota a reta de regressão
plt.plot(x, regression_line, color='red', label='Reta de Regressão')

# Personalizando o gráfico (rótulos de eixo, título, legenda, etc.)
plt.xlabel('Eletricidade a partir de combustiveis fosseis (TWh)')
plt.ylabel('Emissões de dióxido de carbono por pessoa em toneladas métricas')
plt.title('Gráfico de Dispersão com Reta de Regressão')
plt.legend()

# Exibe o gráfico
plt.show()


# FIM DO ITEM 3
# _______________________________________________________

# In[40]:


#Destacando as diferentes categorias da variável qualitativa com tons (hue) de cores.
sns.pairplot(data=df, height=1.5, hue = "País")
plt.show()

