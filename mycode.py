import pandas as pd
import os

data = {
    "Name":["alice","bob","charlie"],
    "Age":[10, 20, 28],
    "city":["Delhi","Mumbai","Goa"]
}

df = pd.DataFrame(data)

new_row = {"Name":"GF1",
           "age":20,
           "city":"city1"}
df.loc[len(df.index)]=new_row

new_row2 = {"Name":"GF2",
           "age":30,
           "city":"city2"}
df.loc[len(df.index)]=new_row2

data_dir = "data"
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,"sample_data.csv")
df.to_csv(file_path,index=False)
print(f"csv file save to {file_path}")