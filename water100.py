#!/usr/bin/env python
# coding: utf-8

# #Critérios 6 ao 7

# In[1]:


#importando as bibliotecas
import pandas as pd
import scipy
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import statsmodels.api as sm
import pylab


# In[2]:


#Renomeando a planilha de dados
arquivo = 'Planilha1.xlsx'
arquivo2 = 'Planilha2.xlsx'
consumo = 'Consumo de água (Litros por habitante ao dia)'


# In[3]:


#lendo os dados da planilha
df=pd.read_excel(arquivo)
df2=pd.read_excel(arquivo2)


# ##Sorteando uma amostra e exportando os dados para o Excel.

# In[4]:


#Sorteando uma amostra com 100 elementos
amostra = df.sample(100)


# In[5]:


amostra.to_excel("Amostra.xlsx", index=False)


# #Representação Gráfica

# ##Histograma

# In[6]:


sns.histplot(data = df2[consumo], kde = True)
plt.show()


# ##BloxPlot

# In[7]:


sns.boxplot(data=df2[consumo])
plt.ylabel('Quantidade de elementos',fontsize=12)
plt.title('Boxplot do consumo de água do Brasil',fontsize=12)
plt.show()


# ##Média

# In[8]:


media = df2[consumo].mean()
round (media,2)


# ##Desvio Padrão

# In[9]:


#calcular o desvio padrão da variável
desvio = df2[consumo].std()
round (desvio,2)


# ##Mediana

# In[10]:


#calcular a mediana da variável
mediana = df2[consumo].median()
round (mediana,2)


# ##Análise do Histograma

# ####Calculando a quantidade de dados no intervalo entre 110 e 150:
# 
# 

# In[11]:


quantidade_1dp = sum(i>=110 and i<=150 for i in df2[consumo].sort_values())
quantidade_1dp


# ####Calculo da quantidade de dados até 110 (entre 0 e 110):
# 

# In[12]:


quantidade_2dp = sum(i>=0 and i<=110 for i in df2[consumo].sort_values())
quantidade_2dp


# ##Análise do Boxplot

# ####Calculando o valor dos quartis do boxplot
# 
# Q1 = 25% dos dados da tabela |
# Q3 = 75% dos dados da tabela

# In[13]:


Q1 = df2[consumo].quantile(q=0.25)
Q3 = df2[consumo].quantile(q=0.75)
print(Q1)
Q3


# ####Verificando a simetria dos dados da tabela

# In[14]:


s1 = mediana - Q1
s2 = Q3 - mediana
print(s1)
s2


# ##Sprint 2
# ####Calculando a quantidade de dados no intervalo entre 0 e 150:

# In[16]:


quantidade_6dp = sum(i>=0 and i<=150 for i in df2[consumo].sort_values())
quantidade_6dp


# ####Proporção de dados presentes no intervalo entre 0 e 150:

# In[18]:


quantidade_6dp = sum(i>=0 and i<=150 for i in df2[consumo].sort_values())
proporção = (quantidade_6dp/100)*100
print(proporção,'%')

