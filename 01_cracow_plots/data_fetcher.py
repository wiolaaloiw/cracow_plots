import pandas as pd
from connector import create_server_connection, close_connection

def fetch_data(query, params=None):

    conn = None
    try:
        conn = create_server_connection()
        if conn is None:
            raise ConnectionError("Nie udało się nawiązać połączenia z bazą danych")
        
        df = pd.read_sql(query, conn, params=params)
        return df
    except Exception as e:
        print(f"Błąd wykonania zapytania: {e}")
        raise
    finally:
        if conn:
            close_connection(conn)
def fetch_buildings_data():
    query = """
    SELECT * FROM insert_buildings
    """
    return fetch_data(query)


# def fetch_zabudowa_data(nazwa="Czyżyny"):
 
#     query = """
#     SELECT ilość,
#       CASE 
#             WHEN typ_index = 'm' THEN 'Mieszkalny'
#             WHEN typ_index = 'i' THEN 'Inwestycyjny'
#             WHEN typ_index = 'h' THEN 'Handlowy'
#             WHEN typ_index = 'b' THEN 'Biurowy'
#             WHEN typ_index = 's' THEN 'Socjalny'
#             WHEN typ_index = 't' THEN 'Turystyczny'
#             WHEN typ_index = 'z' THEN 'Zabudowa przemysłowa'
#             WHEN typ_index = 'k' THEN 'Komunalny'
#             WHEN typ_index = 'g' THEN 'Gospodarczy'
#             WHEN typ_index = 'p' THEN 'Produkcyjny'
#             ELSE 'Nieznany'
#         END AS typ_nazwa
#     FROM zabudowa_dzielnice
#     WHERE nazwa = 'Czyżyny';
#     """
#     return fetch_data(query)
  
# def fetch_przystanki_data():
#     query = "SELECT * FROM dzielnice_przystanki"
#     return fetch_data(query)

# def fetch_cena_data():
#     query = """
#     SELECT 
#         rc.sr_cena_m2 AS cena_za_m2, 
#         d.nazwa AS dzielnica
#     FROM 
#         rejestr_cen rc
#     LEFT JOIN 
#         dzielnice d ON rc.id_dzielnica = d.id_dzielnica
#     """
#     return fetch_data(query)

# def fetch_przystanki_rodzaj_data():
#     query = """
#     SELECT *
#     FROM dzielnice_przystanki_rodzaj
#     """
#     return fetch_data(query)
    
# def fetch_piramida_wieku():
#     query = """
#     SELECT 
#         p.*, dz.nazwa
#     FROM piramida_wieku_krk p
#     INNER JOIN dzielnice dz ON p.id_dzielnica = dz.id_dzielnica
#     """
#     return fetch_data(query)

# def fetch_zabudowa_vs_zielen():
#     query = """
#     SELECT 
#     nazwa, 
#     # ROUND(powierzchnia_zabudowy, 2) AS powierzchnia_zabudowy,
#     # ROUND(powierzchnia_zielen,2) AS powierzchnia_zielen,
#     ROUND((powierzchnia_zabudowy / (powierzchnia_zabudowy + powierzchnia_zielen)) * 100, 2) AS procent_zabudowy,
#     ROUND((powierzchnia_zielen / (powierzchnia_zabudowy + powierzchnia_zielen)) * 100, 2) AS procent_zielen
#     FROM 
#     zestawienie_pow_zieleni_do_zabudowy
# """ 
#     return fetch_data(query)

# def fetch_dzielnice_placówki():
#     query = """
#     SELECT *
#     FROM potencjal_dzielnic_krakowa.dzielnice_placówki
#     """
#     return fetch_data(query)

# def fetch_data_procent_kobiety_mezczyzni():
#     query = """
#     SELECT nazwa, procent_kobiet, procent_mężczyzn
#     FROM potencjal_dzielnic_krakowa.procent_kobiety_meżczyzni
#     """
#     return fetch_data(query)

# def fetch_tereny_zielone_sum_ha():
#     query = """
#     SELECT *
#     FROM potencjal_dzielnic_krakowa.tereny_zielone
#     """
#     return fetch_data(query)

# def fetch_ilosc_os_na_placowki():
#     query = """
#     SELECT dzielnice_placówki.*, dzielnice.liczba_zameldowanych, liczba_zameldowanych/dzielnice_placówki.`ilość placówek` AS placówki_na_os
#     FROM dzielnice_placówki
#     JOIN dzielnice
#     ON dzielnice.nazwa = dzielnice_placówki.nazwa
#     """
#     return fetch_data(query)

# def fetch_pow__zabudowa_zielen_na_os():
#     query = """
#     SELECT 
#     z.nazwa,
#     z.zielen_na_mieszkanca_m2,
#     b.powierzchnia_zabudowy_na_mieszkanca_m2
#     FROM 
#         powierzchnia_trenow_zielonych_na_osobe z
#     JOIN 
#         powierzchnia_trenow_zabudowanych_na_osobe b 
#         ON z.nazwa = b.nazwa
#     ORDER BY 
#         z.nazwa
#     """
#     return fetch_data(query)

