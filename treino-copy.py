# %%
import pandas as pd

# %%

df = pd.read_csv('insurance.csv')

df.head()

# %%

df.value_counts()

# %%

df.groupby(df['age']).agg(contagem = ('age','count'))


# %%

df.loc[(df['age'] > 60) & (df['sex'] == 'female') & (df['region'] != 'southeast')].shape[0]

# %%

df['ano'] = 2024
# %%
import numpy as np
# %%

df['cobranca_abusiva'] = ['sim' if i > 20000 else 'nao' for i in df['charges']]


# %%

df.drop(columns=['ano','cobranca_abusiva2'], inplace = True)

df

# %%
df['cobranca_abusiva'] = df['cobranca_abusiva'].map({
    'sim':1,
    "nao":0
})

df
# %%

df.describe()

# %%

df['region'].value_counts(normalize=True)

# %%
df.groupby('smoker')[['age','charges']].mean()

# %%
df.groupby(['smoker','sex'])[['age','charges']].std()

# %%
df['']

# %%
df.groupby(['>=1' if i >= 1 else '0' for i in df['children']])['charges'].mean()

# %%

df['smoker'].value_counts(normalize=True)

# %%

df['bmi_male'] = [
    'n/a' if sex != 'male' 
    else 'abaixo do normal' if bmi < 20 
    else 'acima do normal' if bmi > 24.9 
    else 'normal'
    for bmi, sex in zip(df['bmi'], df['sex'])]

# %%
from ydata_profiling import ProfileReport

# %%
design_report = ProfileReport(df)
design_report.to_file (output_file = 'report.html')

# %%
#PERGUNTA 1:
df = pd.read_csv('insurance.csv')
# %% 2 
df.info()

# %% 4 numericas
df.describe()

# %% 4 numericas
df['smoker'].value_counts(normalize = True)*100

# %% diferença fumantes e n fumantes

df.groupby('smoker')['charges'].mean()

# %% diferença filhos n filhos

df.groupby(['>=1' if i >= 1 else '0' for i in df['children']])['charges'].mean()

# %% diferença filhos n filhos
df['bmi_male'] = [
    'n/a' if sex != 'male' 
    else 'abaixo do normal' if bmi < 20 
    else 'acima do normal' if bmi > 24.9 
    else 'normal'
    for bmi, sex in zip(df['bmi'], df['sex'])]

# %% homem fumante bmi normal

df.loc[(df['smoker'] == 'yes') & (df['bmi_male'] == 'normal')].shape

# %% AMAZONIA

df = pd.read_csv('amazon.csv',encoding='latin-1')

# %% 

print(f'O dataset tem {df.shape[0]} linhas.')
# %% 
# df.loc[100:120,['state','month','number']]
df.loc[100:120,['state','month','number']]
# %% 
df.iloc[100:120, 1:4]
# %% 
df
# %% 
df.loc[(df['year'] == 2010),['number']].sum()

df.loc[(df['year'] == 2010) & (df['state'] == 'Mato Grosso') ,['number']].sum()

# %% 
df.loc[df['state'] == 'Acre'].groupby('month')['number'].mean()

# %% 
(df[df['state'] == 'Acre'].groupby('month')['number']
                         .aggregate(['mean','std'])
                         .rename(columns={'mean':'media', 'std':'desvio'})
                         .reset_index())
# %% 
df.groupby('state')['number'].mean().sort_values(ascending=False)

# %% 

# df['sudeste'] = [1 if state in ["Sao Paulo","Rio",'Minas Gerais','Espirito Santo'] else 0 
#                   for state in df['state']]


df['sudeste'] = np.where(
    df['state'].isin(["Sao Paulo", "Rio", "Minas Gerais", "Espirito Santo"])
    ,1
    ,0
)

# df['centro_oeste'] = [1 if state in ["Goias","Mato Grosso",'Mato Grosso do Sul','Distrito Federal'] else 0 
#                   for state in df['state']]

# %% 


df[df['sudeste'] == 1]['number'].sum()

# %% 

df[df['centro_oeste'] == 1]['number'].sum()


# %% 
df['number'].sum()









































