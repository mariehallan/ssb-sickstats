# Transformere og klargjøre data fra SSB til egen database 

from __future__ import annotations

from typing import Optional
import re
from pathlib import Path

import pandas as pd

# RegEx for kontroll av kvartalsformat
regex_YYYYKX = re.compile(r"^(\d{4})K([1-4])$")


def parse_quarter(quarter_str: str) -> dict:
	"""Sjekker om kvartalsformat er gyldig og returnerer en dictionary."""
	is_match = regex_YYYYKX.match(quarter_str)
	if not is_match:
		raise ValueError(f"Unsupported period format: {quarter_str}")
	year, quarter = quarter_str.split('K')
	return {'yyyy': int(year), 'k': int(quarter)}


def clean_ssb_dataframe(original_dataframe: pd.DataFrame) -> pd.DataFrame:
	"""Rename kolonner og fjerne unødvendige kolonner."""
	
	dataframe = original_dataframe.copy()
	
    # TODO: fjerne "statistikkvariabel" kolonnen
    # TODO: rename kolonnene  "value" kolonnen til "fraværsprosent" og "næring (SN2007)" til bare "næring", kanskje via dataframe = dataframe.rename(columns=rename_map)


	parsed_quarter = map(parse_quarter, dataframe['kvartal'].astype(str))
	dataframe['år'] = parsed_quarter.apply(lambda quarter_dict: quarter_dict['yyyy'])
	dataframe['kvartal'] = parsed_quarter.apply(lambda quarter_dict: quarter_dict['k'])

	return dataframe
