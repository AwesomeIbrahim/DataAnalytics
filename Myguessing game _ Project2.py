#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.path.append('/Users/ibrahimraji/documents/pythonfiles')
import Functionrepo as funcs
validatedvalue = funcs.gameplay()
if validatedvalue == 'n':
    print("Game has ended. Thank you for playing")
while validatedvalue != 'n':
    validatedvalue = funcs.gameplay()


# In[ ]:





# In[ ]:




