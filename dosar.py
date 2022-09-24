import pandas as pd

df = pd.read_csv("dosar.csv")
df.columns = ["Statie", "Nume", "Lat","Long", "Tema"]

print(df)

with open("dosar.md", "w") as fis:
    for row in df.iloc:
        fis.write(f"\n# {row['Statie']}. {row['Nume']}\n")
        fis.write(f"{row['Tema']}")

