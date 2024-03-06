#!/usr/bin/env python
# coding: utf-8

# 1. Importar as bibliotecas Pandas (pd) e math

# In[8]:


import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 2. Definir a variável "arquivo" pelo nome da planilha.
# 

# In[9]:


arquivo='energia sustentável 1.xlsx'


# 3. Ler a planilha no Python. Escolha um nome para armazenar. Escolheremos df

# In[10]:


df=pd.read_excel(arquivo)
df


# 4.Agrupando os valores qualitativos a partir da variável selecionada.Escolhemos país/região (nome da coluna no arquivo df)

# In[11]:


df2=df.País.value_counts()
df2


# 5. Ordenando os valores da variável em ordem alfabética

# In[12]:


df2=df.País.value_counts().sort_index()
df2


# 6. Contando o total de elementos

# In[13]:


totaldf2=df2.sum()
totaldf2


# 7. Montando a tabela de frequências da variável

# 7.1. Criar um DataFrame para a coluna desejada (dadosvquali no exemplo)

# In[14]:


dadosvquali=pd.DataFrame(df2)


# In[15]:


dadosvquali


# 7.2 Calcular a frequencia relativa em % com 2 casas decimais

# In[16]:


dadosvquali['Frequência %']=round(dadosvquali['País']*100/totaldf2,2)
dadosvquali


# 7.3 Criando uma nova tabela, renomeando as colunas

# In[17]:


tabela=pd.DataFrame({"País":dadosvquali.index,"Frequência":dadosvquali['País'],"Frequência %":dadosvquali["Frequência %"]})


# In[18]:


tabela


# 8. Moda da variável "Países".
# 
# Analiza-se neste ponto qual a informação que mais se repete na tabela (possui maior frequência).

# In[19]:


moda = df["País"].mode()
moda


# 9. Gráficos para variáveis qualitativas
# 

# In[20]:


#ajustando os eixos da figura para melhor visualização e dando nomes aos eixos
fig,ax=plt.subplots(figsize=(5,5))
sns.countplot(x='País',data=df)
ax.set_xlabel("País", size=12)
ax.set_ylabel("Frequência",size=12)
ax.set_title("Frequência do País",size=20)
plt.show()


# In[21]:


#gráficos de variável qualitativa ordenada
df2=df.País.value_counts().sort_index()
df2


# In[22]:


#criando os rótulos e os valores baseados na ordenação anterior
rótulos2=['países com freq 21',' países com freq 14',' países com freq 8',' países com freq 1' ]
valores2=[175,2,1,1]
#criando gráfico de setor
plt.figure(figsize=(10,10))
plt.pie(valores2,labels=rótulos2,autopct='%1.1f%%',startangle=90)
plt.legend()
plt.show()


# In[23]:


#gráfico de barra, também usando os rótulos e valores
plt.bar(rótulos2,valores2)
plt.xlabel('País',fontsize=15)
plt.ylabel('Quantidade de países',fontsize=15)
plt.xticks(rótulos2,fontsize=13,rotation=40)
plt.title('Frequência de países',fontsize=20)
plt.show()


# In[23]:




