#!/usr/bin/env python
# coding: utf-8

# # Oblig 1 - totalkostnadene for elbil og for bensinbil samt årlig kostnadsdifferanse 

# In[43]:


print ("El bil årlig kostnad")
a=5000
print (f"Forsikring i året: {a}kr")
b=8.38*365
print (f"Trafikkforsikringsavgift i året: {b}kr")
c=0.2*2*10000
print (f"drivstoff forbruk: {c}kr")
d=0.1*10000
print (f"bom utgifter:{d}kr") 
print (f"total kostnad for el bil i året {a+b+c+d}")
EL=a+b+c+d


# In[50]:


print ("drivstoff bil årlig kostnader" )
g=7500
print (f"Forsikring for bensinbil:{g}kr/året")
h=8.38*365
print (f"Trafikkforsikringsavgift i året: {h}kr")
f=1*10000
print (f"drivstoff forbruk: {f}kr")
j=0.3*10000
print (f"bom utgifter:{j}kr") 
print (f"totla kostnad for drivstoff bil i året {g+h+f+j}")
Drivstoff=g+h+f+j


# In[52]:


print(" årlig differanse mellom drivstoff bil og el bil")

print(Drivstoff- EL,"kr")


