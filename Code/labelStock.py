import pandas as pd
import os
dir = 'StockData'
company = ['BA','FB','NFLX','TSLA']
for c in company:
    file_path = os.path.join(dir, c + "_pred.csv")
    df = pd.read_csv(file_path)
    labels = []
    for _,row in df.iterrows():
        if row['Close'] >= row['Open']:
            labels.append(1)
        else:
            labels.append(0)
    df['Label'] = labels
    df.to_csv(file_path)




