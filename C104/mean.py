import pandas as pd
df = pd.read_csv('C:/Users/Minho/OneDrive/바탕 화면/python/C104/SOCR-HeightWeight.csv')
height = df['Height(Inches)'].tolist()
somme = 0
for h in height:
    somme=somme+h
mean = somme/len(height)
print(mean)