import logging

import pandas as pd


def read_csv(path):
    csv = pd.read_csv(path)
    logging.info(f"Frame:\n{csv.head()}")


def data_frame(file):
    data = {'Id': [124, 557, 818, 124, 818, 847],
            'Name': ['Michael', 'John', 'Wiliam', 'Hamilton', 'George', 'Elton'],
            "Active": [True, True, False, False, False, False]}
    frame = pd.DataFrame(data)

    frame.to_csv(file)
    logging.info(f"Fame:\n{frame.head(1000)}")
    z = frame[['Name']]
    logging.info(f"frame['Name']:{type(frame['Name'])}:\n{frame['Name']}")
    logging.info(f"frame[['Name']]:{type(frame[['Name']])}:\n{frame[['Name']]}")
    logging.info(f"Frame:{type(z)}:\n{z}")
    logging.info(f"z.head(1000):{type(z.head(1000))}:\n{z.head(1000)}")
    logging.info(f"frame.iloc[0, 0]:{type(frame.iloc[0, 0])}:{frame.iloc[0, 0]}")
    logging.info(f"frame.iloc[1, 1]:{type(frame.iloc[1, 1])}:{frame.iloc[1, 1]}")
    logging.info(f"frame.iloc[1:5, 1:3]:{type(frame.iloc[1:5, 1:3])}\n:{frame.iloc[1:5, 1:3]}")
    logging.info(f"frame.loc[1, 'Name']:{type(frame.loc[1, 'Name'])}:{frame.loc[1, 'Name']}")
    logging.info(f"frame.loc[1, 'Active']:{type(frame.loc[1, 'Active'])}:{frame.loc[1, 'Active']}")
    logging.info(f"frame.iloc[1:5, 0:2]:{type(frame.loc[1:5, 'Name':'Active'])}\n:{frame.loc[1:5, 'Name':'Active']}")
    frame.index = ['a', 'b', 'c', 'd', 'e', 'f']
    logging.info(f"Fame:{type(frame.head(1000))}\n{frame.head(1000)}")
    logging.info(f"frame.loc['a', 'Name']:{type(frame.loc['a', 'Name'])}:{frame.loc['a', 'Name']}")
    logging.info(f"frame['Id']:{type(frame['Id'])}\n{frame['Id']}")
    logging.info(f"frame['Id'].unique():{type(frame['Id'].unique())}:{frame['Id'].unique()}")
    logging.info(f"frame[frame['Id']>600]:\n{type(frame[frame['Id'] > 600])}:{frame[frame['Id'] > 600]}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    data_frame('test.csv')
    read_csv('test.csv')
