#!/usr/bin/env python
# coding: utf-8

# #Medidas Resumo

# In[ ]:


#importando as bibliotecas
import pandas as pd
import scipy
from scipy.stats import variation
import numpy as np


# In[ ]:


#Renomeando a planilha de dados
arquivo='energia sustentável 1.xlsx'
fossil = 'Eletricidade_a_partir_de_combustíveis_fósseis_(TWh)'
sustentavel = 'Eletricidade_de_fontes_renováveis_(TWh)'
pais ='País'


# In[ ]:


#lendo os dados da planilha
df=pd.read_excel(arquivo)


# #Variável 1- Eletrecidade por Combustível Fóssil

# ##Mediana

# In[ ]:


#calcular a mediana da variável especificada
df[fossil].median()


# ##Outiliers
# 

# In[ ]:


Q1 = df[fossil].quantile(q=0.25)
Q3 = df[fossil].quantile(q=0.75)
print(Q1)
Q3


# Segundo, calcule a amplitude interquartil (AIQ = Q3 - Q1)

# In[ ]:


AIQ = Q3 - Q1
AIQ


# Terceiro, calcule os limites (linf = Q1 - 1.5AIQ e lsup = Q3 + 1.5AIQ)

# In[ ]:


E1 = Q1 - 1.5*AIQ
E2 = Q3 + 1.5*AIQ
print("linf =", E1)
print("lsup =", E2)


# Visualizando os outliers superiores.

# In[ ]:


df[df[fossil]>E2]


# Visualizando os outliers inferiores

# In[ ]:


df[df[fossil]<E1]


# ##Percentis

# In[ ]:


#calcular o percentil "q da variável especificada
df[fossil].quantile(q=0.25)


# ##Desvio Padrão

# In[ ]:


#calcular o desvio padrão amostral da variável especificada
df[fossil].std()


# In[ ]:


#calcular o desvio padrão populacional da variável especificada
df[fossil].std(ddof=0)


# In[ ]:


#Quando o data set possui mais de uma variável númerica, é possível calcular
# o desvio padrão de todas as variáveis simultaneamente.
df.std()


# ## Coeficiente de variação
# 
# 

# In[ ]:


#coeficiente de variação (amostral)
scipy.stats.variation(df[fossil],ddof=1)*100


# In[ ]:


#coeficiente de variação (populacional)
scipy.stats.variation(df[fossil],ddof=0)*100


# #Variável 2- Energia Sustentável

# ##Mediana

# In[ ]:


#calcular a mediana da variável especificada
df[sustentavel].median()


# ##Outiliers

# Método do boxplot (ou Método de Tukey)

# Calcular os limites inferior (linf) e superior (lsup) para identificação dos outliers
# 
# Primeiro, vamos calcular Q1 e Q3

# In[ ]:


Q1 = df[sustentavel].quantile(q=0.25)
Q3 = df[sustentavel].quantile(q=0.75)
print(Q1)
Q3


# Terceiro, calcule os limites (linf = Q1 - 1.5AIQ e lsup = Q3 + 1.5AIQ)

# In[ ]:


linf = Q1 - 1.5*AIQ
lsup = Q3 + 1.5*AIQ
print("linf =", linf)
print("lsup =", lsup)


# Visualizando os outliers superiores.

# In[ ]:


df[df[sustentavel]>lsup]


# Visualizando os outliers inferiores

# In[ ]:


df[df[sustentavel]<linf]


# ##Percentis

# In[ ]:


#calcular o percentil "q da variável especificada
df[sustentavel].quantile(q=0.77)


# ##Desvio Padrão

# In[ ]:


#calcular o desvio padrão amostral da variável especificada
df[sustentavel].std()


# In[ ]:


#calcular o desvio padrão populacional da variável especificada
df[sustentavel].std(ddof=0)


# In[ ]:


#Quando o data set possui mais de uma variável númerica, é possível calcular
# o desvio padrão de todas as variáveis simultaneamente.
df.std()


# ##Coeficiente de variação

# In[ ]:


#coeficiente de variação (amostral)
scipy.stats.variation(df[sustentavel],ddof=1)*100


# In[ ]:


#coeficiente de variação (populacional)
scipy.stats.variation(df[sustentavel],ddof=0)*100


# ##Comando "describe" da biblioteca pandas
# Gera estatísticas descritivas.
# 
# As estatísticas descritivas incluem aquelas que resumem a tendência central, a dispersão e a forma da distribuição de um conjunto de dados

# O comando describe() para variável qualitativa mostra:
# 
# - count = contagem de valores
# - unique = número de categorias (observações) diferentes
# - top = categoria (observação) de maior frequência = moda
# - freq = frequência absoluta da moda

# In[ ]:


df[pais].describe()


# O comando describe() para variável quantitativa mostra:
# 
# - count = contagem de valores
# - mean = média
# - std = desvio padrão
# - min = valor mínimo
# - 25% = Q1 (primeiro quartil)
# - 50% = Q2 (segundo quartil) = mediana
# - 75% = Q3 (terceiro quartil)
# - max = valor máximo

# O comando .round(n) arredonda os valores para n casas decimais

# **Variável quantitativa 1 - Combustível Fóssil**

# In[ ]:


df[fossil].describe().round(2)


# **Variável quantitativa 2 - Energia Sustentável**

# In[ ]:


df[sustentavel].describe().round(2)

