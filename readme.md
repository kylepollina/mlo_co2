# Mauna Loa Observatory Carbon Dioxide Data Scraper

This Python package includes a script to scrape the NOAA Earth Science Research Lab for Carbon Dioxide (CO2) readings from the Mauna Loa Observatory in Hawai'i.
You can access this data here: [https://www.esrl.noaa.gov/gmd/ccgg/trends/mlo.html](https://www.esrl.noaa.gov/gmd/ccgg/trends/mlo.html)

## Installation

```
pip install git+https://github.com/kylepollina/mlo_co2.git
```

## Features

### monthly_mean()
```
# Data from March 1958 through April 1974 have been obtained by C. David Keeling
# of the Scripps Institution of Oceanography (SIO) and were obtained from the
# Scripps website (scrippsco2.ucsd.edu).
# Monthly mean CO2 constructed from daily mean values
# Scripps data downloaded from http://scrippsco2.ucsd.edu/data/atmospheric_co2
# Monthly values are corrected to center of month based on average seasonal
# cycle. Missing days can be asymmetric which would produce a high or low bias.
# Missing months have been interpolated, for NOAA data indicated by negative stdev
# and uncertainty. We have no information for SIO data about Ndays, stdv, unc
# so that they are also indicated by negative numbers
```

Optional start date and end date parameters. Scraped from this url: [https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_mm_mlo.txt](https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_mm_mlo.txt)

```python
>>> from mlo_co2 import monthly_mean
>>> mean = monthly_mean(start=datetime(year=1985, day=1, month=1), end=datetime(year=2014, day=1, month=1))
>>> mean.keys()
dict_keys(['url', 'license', 'description', 'headers', 'raw', 'data'])
>>> mean['data'].keys()
dict_keys(['yr', 'mon', 'decimal', 'monthly average (ppm)', 'de-seasonalized (ppm)', '#days', 'st.dev of days', 'unc. of mon mean'])
```

### annual_mean()
```
# Data from March 1958 through April 1974 have been obtained by C. David Keeling
# of the Scripps Institution of Oceanography (SIO) and were obtained from the
# Scripps website (scrippsco2.ucsd.edu).
#
# The estimated uncertainty in the annual mean is the standard deviation
# of the differences of annual mean values determined independently by
# NOAA/ESRL and the Scripps Institution of Oceanography.
#
# NOTE: In general, the data presented for the last year are subject to change,
# depending on recalibration of the reference gas mixtures used, and other quality
# control procedures. Occasionally, earlier years may also be changed for the same
# reasons.  Usually these changes are minor.
#
# CO2 expressed as a mole fraction in dry air, micromol/mol, abbreviated as ppm
```

Optional start date and end date parameters. Scraped from this url: [https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_annmean_mlo.txt](https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_annmean_mlo.txt)

```python
>>> from mlo_co2 import annual_mean
>>> mean = annual_mean(start=datetime(year=1985, day=1, month=1), end=datetime(year=2014, day=1, month=1))
>>> mean.keys()
dict_keys(['url', 'license', 'description', 'headers', 'raw', 'data'])
>>> mean['data'].keys()
dict_keys(['yr', 'mean (ppm)', 'unc'])
```

### annual_mean_increase()
```
# Data from March 1958 through April 1974 have been obtained by C. David Keeling
# of the Scripps Institution of Oceanography (SIO) and were obtained from the
# Scripps website (scrippsco2.ucsd.edu).
#
# Annual CO2 mole fraction increase (ppm) from Jan 1 through Dec 31.
#
# The uncertainty in the Mauna Loa annual mean growth rate is estimated
# from the standard deviation of the differences between monthly mean
# values determined independently by the Scripps Institution of Oceanography
# and by NOAA/ESRL.
#
# NOTE: In general, the data presented for the last year are subject to change,
# depending on recalibration of the reference gas mixtures used, and other quality
# control procedures. Occasionally, earlier years may also be changed for the same
# reasons.  Usually these changes are minor.
#
# CO2 expressed as a mole fraction in dry air, micromol/mol, abbreviated as ppm
```

Optional start date and end date parameters. Scraped from this url: [https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_gr_mlo.txt](https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_gr_mlo.txt)

```python
>>> from mlo_co2 import annual_mean_increase
>>> mean = annual_mean_increase()
>>> mean.keys()
dict_keys(['url', 'license', 'description', 'headers', 'raw', 'data'])
>>> mean['data'].keys()
dict_keys(['yr', 'ann inc', 'unc'])
```

### weekly_mean()
```
# NOTE: DATA FOR THE LAST SEVERAL MONTHS ARE PRELIMINARY, ARE STILL SUBJECT
# TO QUALITY CONTROL PROCEDURES.
# NOTE: The week "1 yr ago" is exactly 365 days ago, and thus does not run from
# Sunday through Saturday. 365 also ignores the possibility of a leap year.
# The week "10 yr ago" is exactly 10*365 days +3 days (for leap years) ago.
```

Optional start date and end date parameters. Scraped from this url: [https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_weekly_mlo.txt](https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_weekly_mlo.txt)

```python
>>> from mlo_co2 import weekly_mean
>>> mean = weekly_mean()
>>> mean.keys()
dict_keys(['url', 'license', 'description', 'headers', 'raw', 'data'])
>>> mean['data'].keys()
dict_keys(['yr', 'mon', 'day', 'decimal', 'ppm', '#days', '1 yr ago', '10 yr ago', 'since 1800'])
```
