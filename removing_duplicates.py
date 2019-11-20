import pandas as pd
import numpy as np
pd.set_option("display.max_columns",300)
amma= pd.read_csv(r"C:\Users\css115515\Desktop\nbabasketball\renga_test.csv" ,header=0,encoding="unicode_escape")
amma["a"]= 1
amma["match"]=[" ".join(sorted(x.split())) for x in amma["Episode_Title"].values]
rajagopal=amma.drop_duplicates(['a', 'match'], keep='first').drop(columns='match')
#rajagopal.to_csv(r"C:\Users\css115515\Desktop\basketball.csv")
print(amma["Episode_Title"].values)