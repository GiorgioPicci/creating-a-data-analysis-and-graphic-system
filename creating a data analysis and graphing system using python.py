#!/usr/bin/env python
# coding: utf-8

# # Data Analysis with Python
# 
# ### challenge:
# 
# You work in a telecom company and you have customers from several different services, among the main ones: internet and telephone..
# 
# The problem is that, analyzing the history of the customers of the last years, you noticed that the company has Churn of more than 26% of the customers.
# 
# This represents a loss of millions for the company.
# 
# What does the company need to do to resolve this?
# 
# Data base: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[4]:


# 1 pass: Import the Data base 
import pandas as pd 

table= pd.read_csv('telecom_users.csv') 
# 2 pass: View the database
table = table.drop("Unnamed: 0", axis=1)
# - Understand what information is so available
# -Find database errors
display(tabela)


# In[5]:


# 3 Pass : data processing
# - Values that are wrongly recognized 
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
# - empty valuess
# deleting empty columns
# axis = 0 _> linha ou axis = 1 _> coluna
tabela = tabela.dropna(how="all", axis=1)
# deleting the empty lines
table = table.dropna(how="any", axis=0)
print(table.info())


# In[6]:


# 4 Pass : Initial Analysis
# How are our cancellations?
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))


# In[9]:


# 5 Pass : More complete analysis
# compare each column of my table with cancel column
import plotly.express as px
# step 1: create the chart
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
# step 2: display the chart
    grafico.show()


# In[8]:


get_ipython().system(' pip install plotly')


# ### Conclusões e Ações

#  * Customers with a monthly contract are MUCH more likely to cancel:
# 
# * We can do promotions for the customer to go to the annual contract
# * Larger families tend to cancel less than smaller families
# 
# * We can make promotions for the person to get an additional phone line
# * Low MonthsAsCustomer has A LOT of cancellations. Customers with little time as a customer tend to cancel a lot
# 
# The first customer experience at the carrier can be bad
# Maybe customer acquisition is bringing disqualified customers
# Idea: you can create an incentive for the customer to stay longer as a customer
# The more services a customer has, the less likely they are to cancel.
# 
# we can do promotions with more services for the customer
# something in our Fiber service is causing customers to cancel
# 
# act on the fiber
# Customers on boleto are MUCH more likely to cancel, so we can take some action, to use other payment methods
