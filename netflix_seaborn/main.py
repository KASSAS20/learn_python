import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Netflix.csv", encoding='latin1')
# data.head()
# sns.barplot(data=data, x='Premiere', y='Runtime')
# plt.show()

class task_2:
    def __init__(self, data) -> None:
        self.data = data
    
    def data_type(self) -> dict:
        result = {}
        for name in self.data.columns:
            result[name] = str(data[name].dtype)
        return result
    
    def data_count(self) -> tuple:
        return f'{self.data.shape[1],self.data.shape[0]}'

    def destribution_genre(self) -> None:
        genre_counts = self.data.groupby('Genre')['Title'].count().reset_index()
        sns.barplot(data=genre_counts, x='Genre', y='Title')
        plt.xlabel('Genre')
        plt.ylabel('Title')
        plt.title('Распределение фильмов по жанрам')
        plt.show()
    
    def destribution_lang(self) -> None:
        lang_counts = self.data.groupby('Language')['Title'].count().reset_index()
        sns.barplot(data=lang_counts, x='Language', y='Title')
        plt.xlabel('Language')
        plt.ylabel('Title')
        plt.title('Распределение фильмов по языкам')
        plt.show()

    def destribution_year(self) -> None:
        premiere_counts = self.data.groupby('Premiere')['Title'].count().reset_index()
        sns.barplot(data=premiere_counts, x='Premiere', y='Title')
        plt.xlabel('Premiere')
        plt.ylabel('Title')
        plt.title('Распределение фильмов по годам')
        plt.show()


class task_3:
    def __init__(self, data) -> None:
        self.data = data
    
    def destribution_imdb(self) -> None:
        sns.barplot(data=self.data, x = 'Title', y = 'IMDB Score')
        plt.xlabel('Title')
        plt.ylabel('IMDB')
        plt.title('Распределение фильмов по IMDB')
        plt.show()
    def destribution_genre(self) -> None:
        task_2(self.data).destribution_genre()
    def destribution_imdb_of_time(self) -> None:
        avg_rating_by_year = self.data.groupby('Premiere')['IMDB Score'].mean()
        sns.lineplot(x=avg_rating_by_year.index, y=avg_rating_by_year.values)
        plt.xlabel('Premiere')
        plt.ylabel('IMDB')
        plt.title('Временой интервал фильмов по рейтингу')
        plt.show()





task_3(data).destribution_imdb_of_time()



