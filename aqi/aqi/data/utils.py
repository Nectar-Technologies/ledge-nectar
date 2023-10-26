import ast
from datetime import datetime, date

from typing import List


def timestamp_to_date(x)->List[date]:
    """Transform timestamp sequence back to dates 
    """
    new_s:List[date] = []
    if isinstance(x, list):
        list_x = x 
    else:
        list_x = ast.literal_eval(x)

    for xx in list_x:
        if xx != 0:
            new_s.append(datetime.fromtimestamp(xx).date())
        else:
            new_s.append(None)
    return new_s


def try_check_month(x, month):
    """Try to check if value is equal to define month otherwise return False
    """
    try:
        return x.month == month
    except:
        return False
