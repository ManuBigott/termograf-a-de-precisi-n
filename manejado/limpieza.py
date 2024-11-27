import pandas as pd
info = pd.read_csv("manejado/dec1.csv")
def Limpieza(df, umbral_ceros=5):


  df_filtrado = df[df["%"] >= umbral_ceros]
  return df_filtrado
print(Limpieza(info, umbral_ceros=5))