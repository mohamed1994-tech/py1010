#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Oppg 1) 
#input av alder til bruker
alder = int(input('Hvilket år er du født? ') )
#minus året vi er i og alderen til brukeren
alder2024= 2024 - alder
#utskrift av alderen til brukeren
print(f"i løpet av året 2024 blir du: {alder2024} år.")


# In[ ]:


#Oppg 2)
# brukeren skrive inn hvor mange elever som kommer
antall_elever = int(input('Skriv inn antall elever:' ))
#antall elver gange 0.25 av det eleven klarer å spise
antall_elever=antall_elever*1/4
#skriver ut antall pizzer som trebges å kjøpes
print(f"Antall pizzaer som må handles inn til festen  {int(antall_elever)} stk")


# In[1]:


#Oppg 3)
import numpy as np
def  gradertilradianer(vinkel):
    #formelen for grader v_rad= grader * PI/180
    v_rad = v_grad*np.pi/180
    return (v_rad)

#skriver inn gradtalle fra bruker
v_grad = float(input('Skriv inn gradtallet:' ))
#kaller inn funksjonen og lagrer resultat
vinkel= gradertilradianer (v_grad)
#skriver ut resultatet 
print(f'{v_grad} Radiantallet til vinkelen verdi lik {vinkel}')


# In[ ]:


#Oppg 4)
#Dictionaryen har ulike land som nøkkel
#info om hovedstaden i landet og antall innbyggere
data= { "norge": ["oslo", 0.634], "england":["london", 8.982], "frankrike": ["paris", 2.161], "italia": ["roma", 2.873]}
#skriver ut Dictionaryen
print(data)
#tar input fra brukeren
# .lower() gjør at store og små bokstaver ikke har noe å si
land = input('Hvilket land ønsker du info om?:  ').lower()
#henter hovestad fra dictinoary 
hovedstad = data[land][0]
# henter innbyggertall fra dictinary
innbyggere = data[land][1]
#skriver ut infoen fra dictinary
print(hovedstad, "er hovedstaden i", land, "det er", innbyggere , "innbyggere i" , hovedstad)
#henter info fra bruker
data = input('Hvilket land ønsker du å legge til?:  ')
#oppdaterer dicinary
data.update()


# In[ ]:




