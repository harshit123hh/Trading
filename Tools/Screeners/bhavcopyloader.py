from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
import os
from datetime import datetime, timedelta, date
import pandas as pd

def getTradingDatesNSE(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:
            dates.append(current_date.strftime('%Y%m%d'))
        current_date += timedelta(days=1)
    holidays = open("/home/fispi/Trading/Tools/Screeners/holiday_nse","r").read().split("\n")

    return list(set(dates)-set(holidays))




bhav_copy_folder = "/home/fispi/Trading/Tools/Data"

def Load_bhav_copy(startdate,enddate,exchange="nse"):
    dates = getTradingDatesNSE(datetime.strptime(startdate,"%Y%m%d"), datetime.strptime(enddate,"%Y%m%d"))
    dates.sort()
    result = []
    for date in dates:
        if not os.path.exists(bhav_copy_folder+"/cm%sbhav.csv"%(datetime.strptime(date.strip(),"%Y%m%d").strftime('%d%b%Y'))):
            print("Bhav copy missing for %s"%date)
            bhavcopy_save(datetime.strptime(date.strip(),"%Y%m%d"), bhav_copy_folder)
            pass
        df = pd.read_csv(bhav_copy_folder+"/cm%sbhav.csv"%(datetime.strptime(date.strip(),"%Y%m%d").strftime('%d%b%Y')))
        df["DATE"] = date
        result.append(df)

    return pd.concat(result)


        

    



    pass

