import squarify
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(12,12))

business = pd.read_csv('../business.csv')
by_state = business.groupby('state')

a = by_state['business_id'].count()

print(a)

a.sort_values(ascending=False,inplace=True)

squarify.plot(sizes= a[0:15].values, label= a[0:15].index, alpha=0.9)

plt.axis('off')
plt.tight_layout()
plt.savefig('business_treemap.png')
plt.show()

# state
# AB      8012
# AK         2
# AL         3
# AR         1
# AZ     56686
# BAS        1
# BC         1
# CA        19
# CON        1
# CT         3
# DOW        1
# DUR        1
# FL         4
# GA         2
# IL      1932
# NC     14720
# NE         2
# NJ         1
# NM         1
# NV     36312
# NY        22
# OH     14697
# ON     33412
# PA     11216
# QC      9219
# SC      1162
# TN         1
# TX         6
# UT         1
# VA         2
# VT         2
# WA         3
# WI      5154
# XGL        1
# XGM        4
# XWY        2