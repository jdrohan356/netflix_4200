import pandas as pd
import matplotlib as plt
from datetime import datetime
import re

filename = 'netflix_titles.csv'

def calc_complexity(string):
    ''' Automated Readability Index '''

    string = string.lower()

    sentence_count = max([len(string.split('.')[:-1]), 1])
    word_count = len(string.split())
    char_count = len(re.sub(r'\W+', '', string))

    return round(4.71 * (char_count / word_count) + 0.5 * (word_count / sentence_count) - 21.43)





def main():

    netflix_df = pd.read_csv(filename)
    netflix_df.set_index('show_id', inplace=True)
    netflix_df.dropna(inplace=True)
    netflix_df = netflix_df[(netflix_df['country'] == 'United States') & (netflix_df['type'] == 'Movie')]
    netflix_df.drop(columns=['country', 'type'], inplace=True)

    netflix_df['duration'] = list(map(lambda x: x.split()[0], netflix_df['duration']))
    netflix_df['date_added'] = list(map(lambda x: datetime.strptime(x, '%B %d, %Y').date(),
                                        netflix_df['date_added']))

    netflix_df['complexity'] = list(map(calc_complexity, netflix_df['description']))

    print(netflix_df)
























if __name__ == '__main__':
    main()
