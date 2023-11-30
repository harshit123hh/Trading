import pandas as pd
from ta import add_all_ta_features
from ta.utils import dropna
import sys
from datetime import date
sys.path.append("/home/fispi/Trading/Tools/Screeners")
import datetime
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
from bhavcopyloader import Load_bhav_copy
import pandas as pd
bhavcopy = Load_bhav_copy("20210101",datetime.datetime.now().strftime("%Y%m%d"))

#bhavcopy = bhavcopy[bhavcopy.DATE==bhavcopy["DATE"].max()]


grouped = bhavcopy.groupby(["SYMBOL","SERIES"])

result = []

for name, group in grouped:
    df = group.sort_values(by="DATE")
    if len(df)<=250:
        continue
    print(name)
    df = add_all_ta_features(df, open="OPEN", high="HIGH", low="LOW", close="CLOSE", volume="TOTTRDQTY")
    df.to_csv("/home/fispi/Trading/Tools/GenOfflineIndicator/OfflineInd/%s_%s"%(name[0],name[1]))







