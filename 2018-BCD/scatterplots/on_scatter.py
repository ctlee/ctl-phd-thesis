import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.ticker as mticker
import pickle
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from itertools import cycle, islice
import seaborn as sns
import numpy as np


df = pd.read_excel('~/Desktop/BCD_for_pandas.xlsx', sheetname='on_pandas')
#df=df.set_index(['Ligand'])
df_err=df.copy()
#df=df.drop(labels='error',axis=1)
df=df.pivot(index='Ligand', columns='Method', values='k on')
df=df.sort_values('Experiment', axis=0)
df_err['k on']=df_err['error']
df_err=df_err.drop(labels='error', axis=1)
df_err=df_err.pivot(index='Ligand', columns='Method', values='k on')
#df_err=df_err.groupby('Method')
#print df.columns
print df
print df_err

#df=df.stack()
#print df
#df_tidy=pd.melt(df, id_vars=['Ligand','Method'])

#print df_tidy

my_colors=['b', 'g',' k', 'm', 'y']
#my_colors=list(islice(cycle(['black', 'firebrick',' darkorange', 'royalblue', 'powderblue']), None, len(df)))





fig = plt.figure()
ax=fig.add_subplot(111)



ttl= 'Calculated On Rates'
#df.plot( y='k on', kind='scatter',ax=ax) 
#df.plot( x=df.index, y=df.columns,yerr=df_err,capsize=4,capthick=1, colormap='Set1', linestyle='--', marker='o',legend=True, ax=ax,)
#df.plot( x=df.index, y=df.columns,yerr=df_err,capsize=4,capthick=1, style=['k--o','b--x','k--o','b-x','k-x'],legend=True, ax=ax,)
styles=['o--','^--','s--','^--','s--']
#print 'columns', df.columns 
colors=['black', 'mediumblue', 'cornflowerblue','firebrick','indianred']
for col, style, color in zip(df.columns, styles, colors):
    df[col].plot(fmt=style,color=color, yerr=df_err[col], capsize=4, capthick=1, ms=7, ax=ax)
ax.legend()

ax.set_xlim(np.array([-0.5, 0.5])+ax.get_xlim())
ax.xaxis.set_major_locator(mticker.FixedLocator(np.arange(len(df))))
ax.xaxis.set_major_formatter(mticker.FixedFormatter(df.index))
ax.set_xticklabels(df.index, rotation=-20)
ax.set_xlabel('Ligand', size=14)
ax.set_ylabel('k on ($\mathregular{M^{-1}\cdot s^{-1}}$)', size= 14)
ax.set_title('Calculated On Rates', size=18)
plt.tight_layout()
#ax.margins(0.05)
#print ax.get_xbound
#ax.set_xbound(lower=-0.5,upper=6.5)


#df.unstack(level=0).unstack(level=0).plot()
fig.savefig('on_scatter.png', dpi=1000)
#plt.show()
#print df.index

#print df

#sns.pairplot(df)
