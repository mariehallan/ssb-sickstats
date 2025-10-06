# Hente statestikk fra SSB's APIer
import requests, pandas

def fetch_sickdata_from_ssb(query):
    # Doc: https://www.ssb.no/en/api/statbank-pxwebapi-user-guide
    # The limits per extract are 800,000 data cells, and the number of queries is currently 30 per minute
    # PxWeb v2 bruker POST/GET med spesifisert query; svar i JSON/CSV.
    
    ssb_api_url = f"https://data.ssb.no/api/pxwebapi/v2/tables/12440/data?lang=en"
    print(f"Henter data fra SSB tabell 12440 med query {query}")

    response = requests.get(ssb_api_url, params=query, timeout=30)
    
    response.raise_for_status()
    print(f"SSB respons:", response)

    response_json = response.json()
    print(f"Response JSON keys: {response_json.keys()}") 
    
    return pandas.DataFrame(response.json())  # evt. parse JSON-stat/CSV
