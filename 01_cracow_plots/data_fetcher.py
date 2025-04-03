import pandas as pd
from connector import create_server_connection

def fetch_data(query):
    conn = create_server_connection()
    df = pd.read_sql(query, conn)
    return df

def fetch_zabudowa_data():
    query = """
    SELECT ilość,
      CASE 
            WHEN typ_index = 'm' THEN 'Mieszkalny'
            WHEN typ_index = 'i' THEN 'Inwestycyjny'
            WHEN typ_index = 'h' THEN 'Handlowy'
            WHEN typ_index = 'b' THEN 'Biurowy'
            WHEN typ_index = 's' THEN 'Socjalny'
            WHEN typ_index = 't' THEN 'Turystyczny'
            WHEN typ_index = 'z' THEN 'Zabudowa przemysłowa'
            WHEN typ_index = 'k' THEN 'Komunalny'
            WHEN typ_index = 'g' THEN 'Gospodarczy'
            WHEN typ_index = 'p' THEN 'Produkcyjny'
            ELSE 'Nieznany'
        END AS typ_nazwa
    FROM zabudowa_dzielnice
    WHERE nazwa = 'Czyżyny';
    """
    return fetch_data(query)

def fetch_przystanki_data():
    query = "SELECT * FROM dzielnice_przystanki"
    return fetch_data(query)

def fetch_cena_data():
    query = """
    SELECT 
        rc.sr_cena_m2 AS cena_za_m2, 
        d.nazwa AS dzielnica
    FROM 
        rejestr_cen rc
    LEFT JOIN 
        dzielnice d ON rc.id_dzielnica = d.id_dzielnica
    """
    return fetch_data(query)

def fetch_przystanki_rodzaj_data():
    query = """
    SELECT *
    FROM dzielnice_przystanki_rodzaj
    """
    return fetch_data(query)
    
def fetch_piramida_wieku():
    query = """
    SELECT 
        p.*, dz.nazwa
    FROM piramida_wieku_krk p
    INNER JOIN dzielnice dz ON p.id_dzielnica = dz.id_dzielnica
    """
    return fetch_data(query)

def fetch_zabudowa_vs_zielen():
    query = """
    SELECT 
    nazwa, 
    # ROUND(powierzchnia_zabudowy, 2) AS powierzchnia_zabudowy,
    # ROUND(powierzchnia_zielen,2) AS powierzchnia_zielen,
    ROUND((powierzchnia_zabudowy / (powierzchnia_zabudowy + powierzchnia_zielen)) * 100, 2) AS procent_zabudowy,
    ROUND((powierzchnia_zielen / (powierzchnia_zabudowy + powierzchnia_zielen)) * 100, 2) AS procent_zielen
    FROM 
    zestawienie_pow_zieleni_do_zabudowy
""" 
    return fetch_data(query)


