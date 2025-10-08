# Hovedprogram

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from extract.ssb_pxweb import fetch_sickdata_from_ssb

if __name__ == "__main__":

    ssb_extract = fetch_sickdata_from_ssb()
    print(ssb_extract)
    