import logging as log

import pandas as pd

if __name__ == '__main__':
    log.basicConfig(level=log.INFO)
    dict_={'a':[11,21,31],'b':[12,22,32]}
    df=pd.DataFrame(dict_)
    log.info(f"type of df is {type(df)}")
    log.info(f"head of df is \n{df.head()}")
    log.info(f"mean of df is \n{df.mean()}")