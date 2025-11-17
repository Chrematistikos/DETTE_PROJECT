import pandas as pd


df = pd.read_csv('HEURES.TRAVAIL.csv', sep=None, engine='python')
df = df.iloc[4:6, 1:]
df = df.dropna(axis=1, how='all')
df = df.apply(lambda x: pd.to_numeric(x.astype(str).str.replace('\u202f','').str.replace(' ','').str.replace(',',''), errors='coerce'))
print(df)
annees = df.iloc[0]  # première ligne
valeurs = df.iloc[1] # deuxième ligne
L = [val for ann, val in zip(annees, valeurs) if 1950 <= ann <= 2006]
print(L)


