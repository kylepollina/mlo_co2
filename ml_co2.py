##################################################
## Mauna Loa CO2 data scraper
##################################################
## {License_info}
##################################################
## Author: Kyle Pollina
## Copyright: Copyright 2021, https://github.com/kylepollina/ml_co2
## Credits: [{credit_list}]
## License: {license}
## Version: {mayor}.{minor}.{rel}
## Maintainer: {maintainer}
## Email: kylepollina@pm.me
## Status: In Development
##################################################


##################
""" How to use """
##################

# from ml_co2 import monthly_mean
# from ml_co2 import annual_mean
# from ml_co2 import annual_mean_growth
# from ml_co2 import weekly_mean

from typing import Optional, Union

import requests

def monthly_mean(start: Optional[str] = None, end: Optional[Union[str]] = None) -> dict:
    """ TODO Get the monthly_mean """
    url = 'https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_mm_mlo.txt'
    res = requests.get(url)
    raw = res.content
    lines = raw.splitlines()
    _license = lines[:50]
    headers = lines[48]

    mean = {
        'url': url,
        'license': _license,
        'headers': headers,
        'raw': raw,
        'data': {
            'yr': [],
            'mon': [],
            'day': [],
            'decimal': [],
            'ppm': [],
            '#days': [],
            '1 yr ago': [],
            '10 yr ago': [],
            'since 1800': []
        }
    }

    breakpoint()
    # Parse data
    for row in lines[49:]:
        yr, mon, day, decimal, ppm, days, _1yr, _10yr, _1800 = row.split()
        mean['data']['yr'].append(yr)
        mean['data']['mon'].append(mon)
        mean['data']['day'].append(day)
        mean['data']['decimal'].append(decimal)
        mean['data']['ppm'].append(ppm)
        mean['data']['#days'].append(days)
        mean['data']['1 yr ago'].append(_1yr)
        mean['data']['10 yr ago'].append(_10yr)
        mean['data']['since 1800'].append(_1800)

    return mean
