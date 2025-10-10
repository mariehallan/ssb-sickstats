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


	parsed_quarter = dataframe['kvartal'].astype(str).apply(parse_quarter)
	dataframe['år'] = parsed_quarter.apply(lambda quarter_dict: quarter_dict['yyyy'])
	dataframe['kvartal'] = parsed_quarter.apply(lambda quarter_dict: quarter_dict['k'])

	# renameing av kolonner
	renamed_columns = {
		'kjønn': 'Kjønn',
		'næring (SN2007)': 'Næring',
		'år': 'År',
		'kvartal': 'Kvartal',
		'value': 'Fraværsprosent'
	}
	dataframe.columns = [renamed_columns.get(col, col) for col in dataframe.columns]

	# Fjerne unødvendig "statistikkvariabel" kolonne
	dataframe.drop('statistikkvariabel', axis=1, inplace=True)

	return dataframe
