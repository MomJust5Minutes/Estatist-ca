#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importando as bibliotecas

import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from scipy.stats import linregress


# In[2]:


#Definindo a variável "arquivo" pelo nome da planilha.

arquivo='energia sustentável 1_CategorizadaCompleta.xlsx'
renovavel= 'Eletricidade de fontes renováveis ​​(TWh)'
fossil= 'Eletricidade a partir de combustíveis fósseis (TWh)'


# In[3]:


#lendo a planilha no Python. Escolhemos o nome df para armazenar.

df=pd.read_excel(arquivo)


# In[4]:


#Vizualindo as 5 primeiras observações do datafram df
df.head()


# #Cálculo do Coeficiente de Correlação Linear de Pearson, Gráfico de Dispersão, Reta de Regressão e cálculo do Coeficiente de Determinação.

# ##Pela Biblioteca Scipy.stats

# In[5]:


#Definindo a variável independente x e a variável dependente y
x=df[renovavel]
y=df[fossil]


# In[6]:


#Calculando os parâmetros da reta de regressão linear
res = stats.linregress(x, y)


# In[7]:


#Exibindo os resultados do comando anterior.
#slope= coeficiente angular da reta de regressão linear
#intercept = coeficiente linear da reta de regressão linear
#rvalue= valor do coeficiente de correlação linear

res


# In[8]:


#Caso queira calcular um parâmetro específico basta usar a estrutura res.nome_do_parâmetro.
#Por exemplo:
res.slope


# In[9]:


#Plotando o diagrama de dispersão de x por y.
plt.rcParams["figure.figsize"]=(10,8)
plt.plot(x, y, 'o',label="dados")
plt.title('Diagrama de Dispersão')
plt.xlabel("Eletricidade de fontes renováveis ​​(TWh)")
plt.ylabel('Eletricidade a partir de combustíveis fósseis (TWh)')
plt.legend()
plt.show()


# In[10]:


#Plotando o diagrama de dispersão de x por y e a reta de regressão linear
plt.rcParams["figure.figsize"]=(10,8)
plt.plot(x, y, 'o', label='dados')
plt.plot(x, res.slope*x + res.intercept, 'r', label='reta de regressão')
plt.title('Regressão Linear Simples')
plt.xlabel("Eletricidade de fontes renováveis ​​(TWh)")
plt.ylabel('Eletricidade a partir de combustíveis fósseis (TWh)')
plt.legend()
plt.show()


# In[11]:


#Exibindo os valores dos coeficientes e a equação da reta de regressão linear:
print(f"Coeficiente de correlação r = {res.rvalue:.4f}")
print( f"Coeficiente linear =  {res.intercept:.4f}")
print( f"Coeficiente angular =  {res.slope:.4f}")
print(f"Reta de regressão linear y = {res.slope:.4f}",f"*x + {res.intercept:.4f}" )
print(f"Coeficiente de determinação r^2 = {res.rvalue**2:.4f}")

