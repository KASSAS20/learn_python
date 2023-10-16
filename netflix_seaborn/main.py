import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Netflix.csv", encoding='latin1')
data.head()
sns.scatterplot(data=data, x='Runtime', y='IMDB Score')
plt.show()
print(data)
