# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1btDXIBEh3MXDeeVpeWF1fOmwwxwno8CM
"""

import pandas as pd
df=pd.DataFrame({'Ism':['Xumoyun','Oybek','Merojiddin'],
 'Familiya':['Dehqonov','Akramov','Baxtiyorjonov'],
  'Yoshi':['19','21','23'],
  'Kursi' :['2','3','4']
                 })
print (df)

df.to_excel('hisobot.xlsx', index=False, sheet_name='Sheet1')