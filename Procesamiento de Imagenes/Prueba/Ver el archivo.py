import pandas as pd
info = pd.read_csv("dec1.csv")
print(info.head(-100))
def Limpieza(df, umbral_ceros=5):


  df_filtrado = df[df["%"] >= umbral_ceros]
  return df_filtrado
print(Limpieza(info, umbral_ceros=5))
