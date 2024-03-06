#!/usr/bin/env python
# coding: utf-8

# **Problema 1**

# In[ ]:


# Na lista Quantidades a seguir DEVERIAM ESTAR as quantidades de produtos vendidas em cada um dos últimos 7 dias
# esses dados seguem a sequência de dias da semana: seg, ter, quar, ..., com uma semana sucedendo a outra na mesma lista
Quantidades = [14, 15, 18, 25, 34, 48]
print(Quantidades)


# In[ ]:


# ATENÇÃO: as correções a seguir não devem ser feitas de forma manual (alterando diretamente nas listas)
# Em cada item, você precisa utilizar um método próprio de listas para esse fim


# In[ ]:


# a) A pessoa responsável pela anotação das vendas na lista esqueceu de anotar as vendas da 5a feira (19 unidades)
# Acrescente esse valor à lista na posição adequada e imprima a lista corrigida.
Quantidades.insert(3,19)
print(Quantidades)


# In[ ]:


# b) Considere que no próximo dia da sequência (2a feira da semana seguinte) foram vendidas 16 unidades, adicione esse dado à lista e imprima a lista corrigida.
# e imprima a lista corrigida.
Quantidades.append(16)
print(Quantidades)


# In[ ]:


# c) descobriu-se, posteriormente, que na 3a feira da primeira foram vendidas 13 e não 15 unidades.
# faça a correção e imprima a lista corrigida.
Quantidades.pop(1)
Quantidades.insert(1,13)
print(Quantidades)


# **Problema 2**

# In[ ]:


# A seguir estão os nomes e as respectivas idades de 5 pessoas
Nomes = ["Carol", "João Pedro", "Mariana", "Rafael", "Patrícia"]
Idades = [18, 20, 19, 20, 18]


# In[ ]:


# ATENÇÃO: as correções a seguir não devem ser feitas de forma manual (alterando diretamente nas listas)
# Em cada item, você precisa utilizar um método próprio de listas para esse fim


# In[ ]:


# a) remova o nome Patrícia e a respectiva idade das listas
Nomes.pop(4)
Idades.pop(4)


# In[ ]:


# b) adicione Gabriela, que tem 19 anos, às listas, mantendo a ordem alfabética da lista de nomes
Nomes.insert(1, "Gabriela")
Idades.insert(1, 19)


# In[ ]:


# c) atualize a idade de Rafael para 21 anos
Idades.pop(4)
Idades.insert(4,21)


# In[ ]:


# d) substitua o nome Carol por Carolina
Nomes.pop(0)
Nomes.insert(0, "Carolina")


# In[ ]:


# e) imprima as listas atualizadas
print(Nomes)
print(Quantidades)

