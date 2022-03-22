import pandas as pd
df = pd.read_csv('C:/Users/Minho/OneDrive/바탕 화면/python/C104/SOCR-HeightWeight.csv')
weight=df['Weight(Pounds)'].tolist()
n=len(weight)
if(n%2==0):
    median=weight[n//2]
else:
    median=(weight[(n+1)//2]+weight[(n-1)//2])/2
print(median)
