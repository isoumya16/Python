#!/usr/bin/env python
# coding: utf-8

# <!-- Write a program that takes a real-life dataset of FIFA 19 players as input, and performs descriptive analytics on it. The
# program should be able to:
# 
# Analyze how different player attributes affect the overall rating.
# 
# Identify the players with the highest overall rating.
# 
# Determine which attributes are most important for determining the overall rating. -->

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Load the FIFA 19 player dataset (replace 'FIFA19.csv' with your dataset file)
data = pd.read_csv('FIFA19.csv')


# In[3]:


data.head()


# In[16]:


# Analyze how different player attributes affect the overall rating
correlation_matrix = data.corr()
plt.figure(figsize=(100, 100))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Player Attributes and Overall Rating')
plt.show()


# In[5]:


# Identify players with the highest overall rating
top_rated_players = data.sort_values(by='Overall', ascending=False).head(10)
print("Top Rated Players:")
print(top_rated_players[['Name', 'Overall']])


# In[7]:


# Determine which attributes are most important for determining the overall rating
attribute_columns = ['Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys',
                     'Dribbling', 'Curve', 'FKAccuracy', 'LongPassing', 'BallControl',
                     'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 'Balance',
                     'ShotPower', 'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
                     'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
                     'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
                     'GKKicking', 'GKPositioning', 'GKReflexes']

attribute_correlations = data[attribute_columns + ['Overall']].corr()
important_attributes = attribute_correlations['Overall'].sort_values(ascending=False)
print("Most Important Attributes for Overall Rating:")
print(important_attributes)


# In[8]:


# Plotting the correlation between important attributes and overall rating
plt.figure(figsize=(10, 6))
important_attributes.drop('Overall').plot(kind='bar')
plt.title('Correlation between Attributes and Overall Rating')
plt.xlabel('Attributes')
plt.ylabel('Correlation with Overall Rating')
plt.show()

