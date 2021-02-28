# Mauna Loa Observatory Carbon Dioxide Data Scraper

This Python package includes a script to scrape the NOAA Earth Science Research Lab for Carbon Dioxide (CO2) readings from the Mauna Loa Observatory in Hawai'i.

## Installation

`pip install mlo_co2`

## Usage

```python
>>> from datetime import datetime
>>> from mlo_co2 import (
...     monthly_mean, annual_mean,
...     annual_mean_increase, weekly_mean
... )

>>> mean = monthly_mean()
>>> mean.keys()
dict_keys(['url', 'license', 'description', 'headers', 'raw', 'data'])
>>> mean = monthly_mean(start=datetime(year=1985, day=1, month=1), end=datetime(year=2014, day=1, month=1))
```
