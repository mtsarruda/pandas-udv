# %%
import pandas as pd
import numpy as np
# %%

df = pd.read_csv(r'C:\Users\mathe\OneDrive\Área de Trabalho\projetos\treino\Data\data.csv',sep=';')

# %%
df['Target'].value_counts()
# %%
df.groupby('Target')['Inflation rate'].mean()

df['Target'].value_counts(normalize=True)

# %%
df.pivot_table(index='Target',
               columns=['Marital status'],
               values='Inflation rate',
               aggfunc=np.mean)
# %%
df.pivot_table(index='Target',
               columns=['Daytime/evening attendance\t','Marital status'],
               values='Previous qualification (grade)',
               aggfunc=np.mean)
# %%

df1 = pd.DataFrame({
    'a':[9,-5,7],
    'b':[-1,3,4]
})

# %%
def color_pos_neg(val):
    color = 'green' if val > 0 else 'red'
    return f'color: {color}'

# %%

teste = df1.style.applymap(color_pos_neg)

display(teste)

# %%

pivot_df = df.pivot_table(
    index ='Marital status',
    columns = 'Target',
    values = 'Previous qualification (grade)',
    aggfunc = np.mean
)

pivot_df
# %%

def h_max_min (data):
    styles = data.copy()
    for col in data.columns:
        max_val = data[col].max()
        min_val = data[col].min()
        styles[col] = ['background-color: lightgreen' if v == max_val else 'background-color: yellow'
                       if v == min_val else '' for v in data[col]
                       ]
    return styles

# %%
s_df = pivot_df.style.apply(h_max_min, axis=None)

display(s_df)

# %%
h_max_min(pivot_df)
# %%

# %%

# %%

# %%

# %%

# %%

