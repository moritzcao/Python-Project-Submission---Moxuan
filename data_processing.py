import pandas as pd
import random


class data_processing:
    def __init__(self):
        # Read the raw data by using Pandas
        self.movie_df = pd.read_csv('IMDB_Movies.txt', sep='\t')

        # Generate an unique genre list for users to input
        self.unique_genre_list = []
        for genre in self.movie_df['genre']:
            for gen in genre.split(', '):
                self.unique_genre_list.append(gen)
        self.unique_genre_list = list(set(self.unique_genre_list))

    def recommend_a_movie(self, selected_genre):
        # Filter the DataFrame to get the movies that contain our selected genre
        genre_df = self.movie_df[self.movie_df['genre'].str.contains(selected_genre)]
        genre_df.reset_index(drop=True, inplace=True)

        # Selected a random index of DataFrame to get a movie
        random_index = random.randint(0, genre_df.shape[0]-1)
        selected_df = genre_df.loc[random_index]

        # Return selected movie information as a dictionary
        movie_dict = {
            'rank': selected_df['rank'],
            'title': selected_df['title'],
            'year': selected_df['year'],
            'link': selected_df['link'],
            'genre': selected_df['genre'],
            'description': selected_df['description']
        }
        return movie_dict


if __name__ == '__main__':
    DP = data_processing()

    unique_genre_list = DP.unique_genre_list
    print(unique_genre_list)

    recommended_genre = DP.recommend_a_movie('Romance')
    print(recommended_genre)


