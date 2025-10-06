# Hovedprogram

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from extract.ssb_pxweb import fetch_from_ssb

if __name__ == "__main__":
    query = {} # TODO

    ssb_extract = fetch_from_ssb(ssb_table_id, query)
    print(ssb_extract)
    