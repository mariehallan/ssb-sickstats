# Hovedprogram

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from extract.ssb_pxweb import fetch_sickdata_from_ssb
from transform.clean import clean_ssb_dataframe

if __name__ == "__main__":

    print("Henter orginal data fra SSB spørring")
    ssb_extract = fetch_sickdata_from_ssb()
    print(ssb_extract)
    cleaned_dataframe = clean_ssb_dataframe(ssb_extract)
    print("\nPrinter ut transformert/renset data")
    print(cleaned_dataframe)
    