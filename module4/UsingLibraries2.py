import logging

import pandas as pd


def read_csv(path):
    csv = pd.read_csv(path)
    logging.info(f"Frame:\n{csv.head()}")


def data_frame(file):
    frame = pd.read_csv(file)

    logging.info(f"Fame:\n{frame.head(1000)}")
    z = frame[['Artist']]
    logging.info(f"frame['Artist']:{type(frame['Artist'])}:\n{frame['Artist']}")
    logging.info(f"frame[['Artist']]:{type(frame[['Artist']])}:\n{frame[['Artist']]}")
    logging.info(f"frame[['Artist','Length','Genre']]:{type(frame[['Artist','Length','Genre']])}:\n{frame[['Artist','Length','Genre']]}")
    logging.info(f"Frame:{type(z)}:\n{z}")
    logging.info(f"z.head(1000):{type(z.head(1000))}:\n{z.head(1000)}")
    logging.info(f"frame.iloc[0, 0]:{type(frame.iloc[0, 0])}:{frame.iloc[0, 0]}")
    logging.info(f"frame.iloc[1, 1]:{type(frame.iloc[1, 1])}:{frame.iloc[1, 1]}")
    logging.info(f"frame.iloc[1:5, 1:3]:{type(frame.iloc[1:5, 1:3])}\n:{frame.iloc[1:5, 1:3]}")
    logging.info(f"frame.loc[1, 'Artist']:{type(frame.loc[1, 'Artist'])}:{frame.loc[1, 'Artist']}")
    logging.info(f"frame.loc[1, 'Soundtrack']:{type(frame.loc[1, 'Soundtrack'])}:{frame.loc[1, 'Soundtrack']}")
    logging.info(
        f"frame.iloc[1:5, 'Artist':'Soundtrack']:{type(frame.loc[1:5, 'Artist':'Soundtrack'])}\n:{frame.loc[1:5, 'Artist':'Soundtrack']}")
    frame.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    logging.info(f"frame.head(1000):{type(frame.head(1000))}\n{frame.head(1000)}")
    logging.info(f"frame.loc['a', 'Artist']:{type(frame.loc['a', 'Artist'])}:{frame.loc['a', 'Artist']}")
    logging.info(f"frame['Rating']:{type(frame['Rating'])}\n{frame['Rating']}")
    logging.info(f"frame['Rating'].unique():{type(frame['Rating'].unique())}:{frame['Rating'].unique()}")
    logging.info(f"frame[frame['Rating']>8]:\n{type(frame[frame['Rating'] > 8])}:{frame[frame['Rating'] > 8]}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    data_frame('TopSellingAlbums.csv')
    read_csv('test.csv')
