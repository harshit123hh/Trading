from datetime import date
import datetime
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
from bhavcopyloader import Load_bhav_copy
import pandas as pd
bhavcopy = Load_bhav_copy("20220101",datetime.datetime.now().strftime("%Y%m%d"))


grouped = bhavcopy.groupby(["SYMBOL","SERIES"])

result = []

for name, group in grouped:
    group = group.sort_values(by="DATE")
    group["ema_5"] = group["CLOSE"].ewm(span=5).mean()
    group["ema_10"] = group["CLOSE"].ewm(span=10).mean()
    group["ema_20"] = group["CLOSE"].ewm(span=20).mean()
    group["ema_50"] = group["CLOSE"].ewm(span=50).mean()
    group["ema_250"] = group["CLOSE"].ewm(span=250).mean()
    result.append(pd.DataFrame(group.iloc[-1]).T)




result = pd.concat(result)
result = result[result.DATE==result.DATE.max()]

result = result[result.CLOSE>=250]
print(result[(result["ema_5"]>1.03 * result["ema_10"]) & (result["ema_10"] > 1.06*result["ema_20"]) & (result["ema_20"] > 1.18*result["ema_50"])])
