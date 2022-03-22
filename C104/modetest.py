import statistics as st
import pandas as pd
df = pd.read_csv('C:/Users/Minho/OneDrive/바탕 화면/python/C104/SOCR-HeightWeight.csv')
height = df['Height(Inches)'].tolist()
weight = df['Weight(Pounds)'].tolist()
modeWe = st.mode(weight)
modeHe = st.mode(height)
print('The mode of the weight is '+str(modeWe))
print('The mode of the height is '+str(modeHe))