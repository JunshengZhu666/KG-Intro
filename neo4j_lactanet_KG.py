#!/usr/bin/env python
# coding: utf-8

# In[78]:


import csv
import py2neo
from py2neo import Graph, Node, Relationship, NodeMatcher


# In[79]:


g = Graph('http://localhost:7474', user = 'neo4j', password = 'neo4j****')


# In[80]:


with open('/Users/JZ/Desktop/triples8','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    for item in reader:
        if reader.line_num == 1:
            continue
        print("Current_Line：",reader.line_num,"Current_Content：",item)
        start_node=Node("Lactanet",name=item[0])
        end_node=Node("Lactanet",name=item[1])
        relation=Relationship(start_node,item[3],end_node)
        g.merge(start_node,"Lactanet","name")
        g.merge(end_node,"Lactanet","name")
        g.merge(relation,"Lactanet","name")


# In[ ]:





# In[ ]:





# In[ ]:




