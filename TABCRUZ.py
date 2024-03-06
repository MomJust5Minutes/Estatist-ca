#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importando a biblioteca
import pandas as pd


# In[2]:


#renomeando a planilha
arquivo='energia sustentável 1_CategorizadaCompleta.xlsx'


# In[3]:


#lendo a planilha
df=pd.read_excel(arquivo)


# In[4]:


#Renomeando as variáveis que serão consideradas para a construção da tabela cruzada
var1= "Eletricidade a partir de combustíveis fósseis em relação ao Brasil"
var2= "Ano"


# In[5]:


#Exibindo as 5 primeiras observações do Data Set
df.head()


# #Tabela Cruzada com frequências absolutas

# In[6]:


#Contruindo a tabela cruzada com frequências absolutas.
df_tabela_cruz=pd.crosstab(df[var1],df[var2],margins=True)


# In[7]:


#A tabela cruzada é construída com uma coluna total e uma linha total escritas em inglês
df_tabela_cruz


# In[8]:


#Podemos renomear a coluna All para o Português:
df_tabela_cruz.rename(columns={'All': 'Total'}, inplace = True)
#Podemos renomear a linha All para o Português:
df_tabela_cruz.rename(index={'All': 'Total'}, inplace = True)


# In[9]:


df_tabela_cruz


# #Tabela Cruzada com frequências relativas (% do Total)

# In[10]:


df_tabela_cruz_porcentagem = (pd.crosstab(df[var1], df[var2], margins = True, normalize= True)*100).round(1)
df_tabela_cruz_porcentagem


# In[11]:


#Podemos renomear a linha All e a coluna ALL para o Português:
df_tabela_cruz_porcentagem.rename(index={'All': 'Total'}, inplace = True)
df_tabela_cruz_porcentagem.rename(columns={'All': 'Total'}, inplace = True)


# In[12]:


df_tabela_cruz_porcentagem


# #Tabela Cruzada com frequências relativas nas linhas (% da Linha)

# In[13]:


df_tabela_cruz_porcentagem_linhas = (pd.crosstab(df[var1], df[var2], margins = True, normalize='index')*100).round(1)
df_tabela_cruz_porcentagem_linhas


# In[14]:


#Podemos renomear a linha All para o Português:
df_tabela_cruz_porcentagem_linhas.rename(index={'All': 'Total'}, inplace = True)


# In[15]:


df_tabela_cruz_porcentagem_linhas


# #Tabela Cruzada com frequências relativas nas colunas (% da Coluna)

# In[16]:


df_tabela_cruz_porcentagem_colunas = (pd.crosstab(df[var1], df[var2], margins = True, normalize='columns')*100).round(1)
df_tabela_cruz_porcentagem_colunas


# In[17]:


#Podemos renomear a coluna All para o Português:
df_tabela_cruz_porcentagem_colunas.rename(columns={'All': 'Total'}, inplace = True)


# In[18]:


df_tabela_cruz_porcentagem_colunas


# *INTERPRETANDO OS RESULTADOS*
# 
# Com base nas tabelas geradas anteriormente e mostradas a seguir, podemos observar por exemplo,que:
# 
# 
# *   **10,7%** dos itens do Menu fazem parte da Categoria Breakfast Menu (tabela cruzada exibida com as frequências relativas (porcentagens) -df_tabela_cruz_porcentagem)
# *   **20%** dos itens do  Menu possuem nível de sódio aceitável (tabela cruzada exibida com as frequências relativas (porcentagens) -df_tabela_cruz_porcentagem)
# *   **Nenhum (0%)** item do Menu Gourmet possui nível de sódio aceitável *OU* **Nenhum (0%)** item com nível de sódio aceitável é do Menu Gourmet (tabela cruzada exibida com as frequências relativas (porcentagens)-df_tabela_cruz_porcentagem)
# *   **0,9%**  dos itens que possuem nível não aceitável de sódio são do Menu Desserts (sobremesa) (tabela cruzada exibida com frequências relativas por linhas -df_tabela_cruz_porcentagem_linhas).
# *   **Dentre** os itens com nível de sódio aceitável, 50% são do Menu McCafe (tabela cruzada exibida com as frequências relativas (porcentagens) por linhas -df_tabela_cruz_porcentagem_linhas)
# *   **Dentre** os itens do Menu Desserts (sobremesa), 50% tem nível de sódio aceitável (tabela cruzada exibida com as frequências relativas (porcentagens)  por colunas -df_tabela_cruz_porcentagem_colunas)
# *   **94,4%**  dos itens do Meu Regular possuem nível não aceitável de sódio(tabela cruzada exibida com frequências relativas (porcentagens) por colunas -df_tabela_cruz_porcentagem_colunas).
# 
# 

# In[19]:


df_tabela_cruz


# In[20]:


df_tabela_cruz_porcentagem


# In[21]:


df_tabela_cruz_porcentagem_linhas


# In[22]:


df_tabela_cruz_porcentagem_colunas


# In[23]:


#Salvando as tabelas cruzadas em arquivo de planilha excel
writer=pd.ExcelWriter('Tabelas_Cruzadas.xlsx')
df_tabela_cruz.to_excel(writer, sheet_name="Tab_cruz_abs",index=True)
df_tabela_cruz_porcentagem.to_excel(writer, sheet_name="Tab_Cruzada_porc", index=True)
df_tabela_cruz_porcentagem_linhas.to_excel(writer, sheet_name="Tab_Cruzada_porc_linhas",index=True)
df_tabela_cruz_porcentagem_colunas.to_excel(writer, sheet_name="Tab_Cruzada_porc_colunas", index=True)
writer.save()

