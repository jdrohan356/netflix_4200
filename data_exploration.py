import pandas as pd
import matplotlib as plt
from datetime import datetime

filename = 'netflix_titles.csv'

def main():

    netflix_df = pd.read_csv(filename)
    netflix_df.set_index('show_id', inplace=True)
    netflix_df.dropna(inplace=True)
    netflix_df = netflix_df[(netflix_df['country'] == 'United States') & (netflix_df['type'] == 'Movie')]
    netflix_df.drop(columns=['description', 'country', 'type'], inplace=True)

    netflix_df['duration'] = list(map(lambda x: x.split()[0], netflix_df['duration']))
    netflix_df['date added'] = list(map(lambda x: datetime.strptime(x, '%m-%d-%Y').date(), netflix_df['date added']))

    print(netflix_df['date added'])

























if __name__ == '__main__':
    main()
