#!/usr/bin/env python
# coding: utf-8

# 1. Importar as bibliotecas Pandas (pd) e math

# In[1]:


import pandas as pd
import math


# 2. Definir a variável "arquivo" pelo nome da planilha.
# 

# In[2]:


arquivo='dados_projeto1.xlsx'


# 3. Ler a planilha no Python. Escolha um nome para armazenar. Escolheremos df

# In[3]:


df=pd.read_excel(arquivo)
df


# 4.Agrupando os valores qualitativos a partir da variável selecionada.Escolhemos Escolaridade (nome da coluna no arquivo df)

# In[4]:


df2=df.Escolaridade.value_counts()
df2


# 5. Ordenando os valores da variável em ordem alfabética

# In[5]:


df2=df.Escolaridade.value_counts().sort_index()
df2


# 6. Contando o total de elementos

# In[6]:


totaldf2=df2.sum()
totaldf2


# 7. Montando a tabela de frequências da variável

# 7.1. Criar um DataFrame para a coluna desejada (dadosvquali no exemplo)

# In[7]:


dadosvquali=pd.DataFrame(df2)


# In[8]:


dadosvquali


# 7.2 Calcular a frequencia relativa em % com 2 casas decimais

# In[9]:


dadosvquali['Frequência %']=round(dadosvquali['Escolaridade']*100/totaldf2,2)
dadosvquali


# 7.3 Criando uma nova tabela, renomeando as colunas

# In[10]:


tabela=pd.DataFrame({"Escolaridade":dadosvquali.index,"Frequência":dadosvquali['Escolaridade'],"Frequência %":dadosvquali["Frequência %"]})


# In[11]:


tabela

