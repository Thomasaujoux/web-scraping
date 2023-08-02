

################## THIS FILE IS TO BE USED AFTERWARDS FOR REPROCESSING ##################

import numpy as np
import pandas as pd
import fileinput
import json


df = pd.DataFrame()
with fileinput.input(files='./laph.jl') as file:
    for line in file:
        conv = json.loads(line)
        df = pd.concat([df, pd.DataFrame([conv])], ignore_index=True)
df.head()


df['url'].drop_duplicates(inplace=True)
df['url'] = 'https://www.auchan.fr' + df['url']
#df['url'] = 'https://www.franprix.fr' + df['url']

df.to_csv('./auchan.csv')
#df.to_csv('./franprix.csv')