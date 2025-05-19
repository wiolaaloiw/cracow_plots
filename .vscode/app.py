# import mysql.connector
# from mysql.connector import Error
# import pandas as pd
# import matplotlib.pyplot as plt 
# import numpy as np
# import seaborn as sns


 

# def create_server_connection(host_name, user_name, user_password, db_name):
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host=host_name,
#             user=user_name,
#             passwd=user_password,
#             database=db_name
#         )
#         print("Successful")
#     except Error as err:
#         print("Error")
#     return connection
# connection = create_server_connection("localhost", "root", "Jestemkoksem12!", "potencjal_dzielnic_krakowa")

# host = "localhost"
# user = "root"
# password = "Jestemkoksem12!"
# database = "potencjal_dzielnic_krakowa"

# conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

# if conn:
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM zabudowa_dzielnice")
#     result_list = cursor.fetchall()


# query = """
# SELECT ilość,
#   CASE 
#         WHEN typ_index = 'm' THEN 'Mieszkalny'
#         WHEN typ_index = 'i' THEN 'Inwestycyjny'
#         WHEN typ_index = 'h' THEN 'Handlowy'
#         WHEN typ_index = 'b' THEN 'Biurowy'
#         WHEN typ_index = 's' THEN 'Socjalny'
#         WHEN typ_index = 't' THEN 'Turystyczny'
#         WHEN typ_index = 'z' THEN 'Zabudowa przemysłowa'
#         WHEN typ_index = 'k' THEN 'Komunalny'
#         WHEN typ_index = 'g' THEN 'Gospodarczy'
#         WHEN typ_index = 'p' THEN 'Produkcyjny'
#         ELSE 'Nieznany'  -- Jeśli typ nie pasuje do żadnej z powyższych opcji
#     END AS typ_nazwa
# FROM zabudowa_dzielnice
# WHERE nazwa = 'Czyżyny';

# # """

# df = pd.read_sql(query,conn)
# df.to_csv("Typ zabudowy_Bieńczyce.csv")


# fig = plt.figure()
# ax = fig.add_subplot()
# bars = ax.bar(df['typ_nazwa'], df['ilość'])
# ax.set_axisbelow(True)
# ax.grid(axis="y", linestyle='--', alpha=0.5)
# plt.xticks(rotation=45, ha='right')
# fig.suptitle("Typy zabudowy w Bieńczyce", fontsize =14, fontweight="bold")
# ax.bar_label(bars, padding=1, fontsize= 9)
# ax.set_title("Ilość zabudowy w Bieńczyce")
# ax.set_xlabel("Typ zabudowy")
# ax.set_ylabel("Ilość zabudowy")
# plt.show()


# if conn:
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM dzielnice_przystanki")
#     result_list = cursor.fetchall()

# df = pd.DataFrame(result_list,columns=["Dzielnica","Liczba przystanków"])
# df.to_csv("dzielnice_przystanki.csv")

# df = pd.read_csv("dzielnice_przystanki.csv")
# plt.figure(figsize=(12, 8))
# plt.bar(df["Dzielnica"], df["Liczba przystanków"])
# plt.title("Liczba przystanków w poszczególnych dzielnicach Krakowa")
# plt.xlabel("Dzielnica")
# plt.ylabel("Liczba przystanków")
# plt.xticks(rotation=45)
# plt.show()
    
# if conn: 
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM rejestr_cen")
#     result_list = cursor.fetchall()

# query = """
# SELECT 
#     rc.sr_cena_m2 AS cena_za_m2, 
#     d.nazwa AS dzielnica
# FROM 
#     rejestr_cen rc
# LEFT JOIN 
#     dzielnice d ON rc.id_dzielnica = d.id_dzielnica
# """
# df = pd.read_sql(query, conn)
# df.to_csv("cena_za_m2.csv", index=False)
# sns.boxplot(
#         x='dzielnica', 
#         y='cena_za_m2', 
#         hue='dzielnica',
#         legend=False,
#         data=df,
#         palette="viridis"
#     )
# plt.title("Rozkład cen za m² w dzielnicach Krakowa", fontsize=16, fontweight='bold')
# plt.xlabel("Dzielnica", fontsize=12)
# plt.ylabel("Cena za m² (PLN)", fontsize=12)
# plt.xticks(rotation=45, ha='right')
# plt.show() 

