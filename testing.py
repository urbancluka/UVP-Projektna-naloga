import pandas as pd 

podatki_o_avtih = pd.read_csv("data.csv", index_col=False)
print([podatki_o_avtih.head()])
print(podatki_o_avtih["Price (EUR)"].mean())