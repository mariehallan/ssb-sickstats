# Hente statestikk fra SSB's APIer
import json
import requests 
import pandas
from pyjstat import pyjstat

def fetch_sickdata_from_ssb():
    # Dokumentasjon fra SSB: https://www.ssb.no/en/api/statbank-pxwebapi-user-guide
        # The limits per extract are 800,000 data cells, and the number of queries is currently 30 per minute
    # Info om tabellen: https://www.ssb.no/statbank/table/12440
    # Eksempel fra SSB: https://www.ssb.no/api/pxwebapi/api-eksempler-pa-kode/json-stat-til-pandas-dataframe-funksjon
    
    ssb_api_url = f"https://data.ssb.no/api/pxwebapi/v2/tables/12440/data?lang=no&valueCodes[ContentsCode]=SykefravProsent&codelist[NACE2007]=vs_NACE260sykefratot4&valueCodes[Kjonn]=2,1&valueCodes[NACE2007]=61-63,86&valueCodes[Tid]=from(2005K1)"
    print(f"Henter data fra SSB tabell 12440 av sykefraværsprosent for næring IKT-virksomhet og Helsetjenester fra 2005")

    response = requests.get(ssb_api_url, timeout=30)
    
    response.raise_for_status() # Stopp programmet hvis ikke 200 OK

    # Lagre data fra SSB spørring i en dataset
    dataset = pyjstat.Dataset.read(response.text)

    # Skrive inn data til pandas DataFrame
    dataframe = dataset.write('dataframe') 
    # Kolonner: kjønn; næring (SN2007);  statistikkvariabel; kvartal;  value
 
    return dataframe
