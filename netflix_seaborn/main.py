import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Netflix.csv", encoding='latin1')
# data.head()
# sns.barplot(data=data, x='Premiere', y='Runtime')
# plt.show()

class task_1:
    def __init__(self, data):
        self.data = data
    
    def data_type(self):
        result = {}
        for name in self.data.columns:
            result[name] = str(data[name].dtype)
        return result

print(task_1(data=data).data_type())