# Hovedprogram

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from extract.ssb_pxweb import fetch_sickdata_from_ssb

if __name__ == "__main__":
    query = {} # TODO

    ssb_extract = fetch_sickdata_from_ssb(query)
    print(ssb_extract)
    