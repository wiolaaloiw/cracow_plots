import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from data_fetcher import fetch_zabudowa_data, fetch_przystanki_data, fetch_cena_data, fetch_przystanki_rodzaj_data, fetch_piramida_wieku, fetch_zabudowa_vs_zielen



# piramida wieku
df = pd.read_csv("piramida_wieku_krk.csv")
plt.figure(figsize=(30,20))
plt.suptitle("piramidy wieku dla wszystkich dzielnic", fontsize=20)
grupy_wiekowe = ["0-2", "3-6", "7-14", "15-18", "19-24", 
                "25-34", "35-44", "45-59/64", "60-65/79", "80+"]
y_pos = np.arange(len(grupy_wiekowe))

for i in range(18):
    ax = plt.subplot(6,3, i+1)
    row = df.iloc[i]
    kobiety = [row['k_0_2'], row['k_3_6'], row['k_7_14'], 
               row['k_15_18'], row['k_19_24'], row['k_25_34'],
               row['k_35_44'], row['k_45_59_64'], row['k_60_65_79'],
               row['k_po_80']]
    mezczyzni = [row['m_0_2'], row['m_3_6'], row['m_7_14'],
                 row['m_15_18'], row['m_19_24'], row['m_25_34'],
                 row['m_35_44'], row['m_45_59_64'], row['m_60_65_79'],
                 row['m_po_80']]
    ax.barh(y_pos, kobiety, color='pink', label='Kobiety')
    ax.barh(y_pos, [-m for m in mezczyzni], color='lightblue', label='Mężczyźni')
    ax.set_title(row['nazwa'], fontsize=10)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(grupy_wiekowe, fontsize=8)
    ax.set_xlabel('Liczba osób', fontsize=8)
plt.tight_layout()
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


# wykresy transport kolejowy 
df_przystanki_rodzaj = fetch_przystanki_rodzaj_data()
df = pd.DataFrame(df_przystanki_rodzaj)
df_pivot = df.pivot( index = "nazwa", columns = "rodzaj", values="ilość przystanków")
df_pivot.to_csv("przystanki_rodzaj.csv", index=True)
plt.figure(figsize=(10, 6))
plt.bar(df_pivot.index, df_pivot["tramwajowy"], label="Tramwajowy", color="blue", width=0.4, align="center")
plt.bar(df_pivot.index, df_pivot["autobusowy"], label="Autobusowy", color="orange", width=0.4, align="edge")
plt.xlabel('Dzielnice')
plt.ylabel("Liczba przystanków")
plt.title("Liczba  i radzaj przystanków w dzielnicach Krakowa")
plt.xticks(rotation = 90)
plt.tight_layout()


# procent powierzchni zabudowy do powierzchni terenów zielonych
df_pr_zabudowy_do_zieleni = fetch_zabudowa_vs_zielen()
df_pr_zabudowy_do_zieleni.to_csv("procent_zabudowy_do_zieleni.csv", index = False)
print(df_pr_zabudowy_do_zieleni)
plt.figure(figsize=(30,20))
plt.suptitle("Zestawienie powierzchni zabudowy do powierzchni terenów dzielonych w dzielnicach [%]")
for i in range(len(df_pr_zabudowy_do_zieleni)):

    row =df_pr_zabudowy_do_zieleni.iloc[i]
    nazwa = row["nazwa"]
    zabudowa = row["procent_zabudowy"]
    zielen = row["procent_zielen"]
    plt.subplot(6, 3, i + 1)
    plt.pie([zabudowa,zielen], 
            labels = ["Zabudowa\n" + str(round(zabudowa, 2)) + "%",
                      "Zieleń\n" + str(round(zielen,2)) + "%"], 
            colors = ["brown","green"])
    plt.title(nazwa,fontsize = 12)
plt.tight_layout(rect=[0, 0, 1, 0.95])
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

