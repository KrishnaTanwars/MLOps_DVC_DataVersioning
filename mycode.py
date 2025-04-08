import pandas as pd
import os

data = {
    "Name":["alice","bob","charlie"],
    "Age":[10, 20, 28],
    "city":["Delhi","Mumbai","Goa"]
}

df = pd.DataFrame(data)

data_dir = "data"
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,"sample_data.csv")
df.to_csv(file_path,index=False)
print(f"csv file save to {file_path}")