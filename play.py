from dsmlbc5.hi import hello

hello()

from dsmlbc5.hi import hello4

hello4()


import seaborn as sns
df = sns.load_dataset("tips")

from dsmlbc5.eda.eda import check_df

check_df(df)

from dsmlbc5.eda.eda import check_df, grab_col_names

cat_cols, num_cols, cat_but_car = grab_col_names(df)

from dsmlbc5.eda.eda import *

import dsmlbc5
help(dsmlbc5)


from dsmlbc5.eda import eda

import dsmlbc5.eda

help(eda)


import pandas as pd

help(pd)

help(pd.tseries)


help(eda.check_df)

