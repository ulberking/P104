import pandas as pd
df = pd.read_csv('C:/Users/Minho/OneDrive/바탕 화면/python/C104/SOCR-HeightWeight.csv')
height = df['Height(Inches)'].tolist()
n = len(height)
if (n%2==0):
    median=height[n//2]
else:
    median=(height[(n+1)//2]+height[(n-1)//2])/2
print(median)