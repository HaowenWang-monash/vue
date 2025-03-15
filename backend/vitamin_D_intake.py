import pandas as pd


data = {
    "Skin Type": ["I", "II", "III", "IV", "V", "VI"],
    "Exposure Time (UV Level)": ["10-15m", "15-20m", "20-30m", "30-40m", "40-60m", "60-80m"]
}


df = pd.DataFrame(data)
print(df["Skin Type"][1])
print (df["Exposure Time (UV Level)"])
print(df)