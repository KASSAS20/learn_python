import seaborn as sns 
import matplotlib.pyplot as plp 
import pandas as pd 

data = pd.read_csv("Netflix.csv")
data.head()
sns.scatterplot(data = data, x='x', y='y')
plp.show()
print(data)