import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_fetcher import fetch_zabudowa_data, fetch_przystanki_data, fetch_cena_data


# typy zabudowy 
df_zabudowa = fetch_zabudowa_data()
df_zabudowa.to_csv("Typ_zabudowy_Czyzyny.csv")
fig = plt.figure(figsize=(15, 7))
ax = fig.add_subplot()
bars = ax.bar(df_zabudowa['typ_nazwa'], df_zabudowa['ilość'])
ax.set_axisbelow(True)
plt.xticks(rotation=45, ha='right')
# fig.suptitle("Typy zabudowy w dzielnicy Czyżyny")
ax.bar_label(bars, padding=1, fontsize=9)
ax.set_title("Ilość zabudowy w dzielnicy Czyżyny ", fontsize=14, fontweight="bold")
ax.set_xlabel("Typ zabudowy")
ax.set_ylabel("Ilość zabudowy")
plt.show()

# liczba przystankow
df_przystanki = fetch_przystanki_data()
df_przystanki.to_csv("dzielnice_przystanki.csv")
plt.figure(figsize=(15,7))
plt.bar(df_przystanki["nazwa"], df_przystanki["ilość przystanków"])
plt.title("Liczba przystanków w poszczególnych dzielnicach Krakowa", fontsize=14, fontweight="bold")
plt.xlabel("Dzielnica")
plt.ylabel("Liczba przystanków")
plt.xticks(rotation=90)
plt.show()

# cena za m2
df_cena = fetch_cena_data()
df_cena.to_csv("cena_za_m2.csv", index=False)
plt.figure(figsize=(15, 7))
sns.boxplot(
    x='dzielnica',
    y='cena_za_m2',
    hue='dzielnica',
    legend=False,
    data=df_cena,
    palette="viridis")
plt.title("Rozkład cen za m² w dzielnicach Krakowa", fontsize=16, fontweight='bold')
plt.xlabel("Dzielnica", fontsize=12)
plt.ylabel("Cena za m² (PLN)", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.show()