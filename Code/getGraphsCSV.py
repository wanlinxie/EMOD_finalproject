import pandas as pd
import os
dir = "Data2"
company = ['BA','FB','NFLX','TSLA']
sources = ['businessinsider.com','marketwatch.com','yahoo.com']

for c in company:
    new_file = {"dates":[],"content_score":[],"title_score":[],"firstP_score":[],"category":[]}
    for s in sources:
        filename = c + "_" + s + "_urls.csv"
        filepath = os.path.join(dir,filename)
        df = pd.read_csv(filepath,encoding='latin-1')
        for _, row in df.iterrows():
            new_file['dates'].append(row['dates'])
            new_file['content_score'].append(row['content_scores'])
            new_file['title_score'].append ( row['title_score'] )
            new_file['firstP_score'].append ( row['firstP_score'] )
            new_file['category'].append(s[:-4])
    data = pd.DataFrame.from_dict(new_file)
    newfilename = c + "_graphs.csv"
    newpath = os.path.join(dir,newfilename)
    data.to_csv(newpath, index= False)

