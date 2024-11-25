import pandas as pd
info = pd.read_csv("dec1.csv")
print(info.head(-100))
pan = info["archivo"]
print(pan)