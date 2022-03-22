import pandas as pd
df = pd.read_csv('C:/Users/Minho/OneDrive/바탕 화면/python/C104/SOCR-HeightWeight.csv')
weight=df['Weight(Pounds)'].tolist()
somme = 0
for h in weight:
    somme = somme+h
mean = somme/len(weight)
print(mean)