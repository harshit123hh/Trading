from datetime import date
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
from bhavcopyloader import Load_bhav_copy
import pandas as pd
import datetime
bhavcopy = Load_bhav_copy("20230101",datetime.datetime.now().strftime("%Y%m%d"))


grouped = bhavcopy.groupby(["SYMBOL","SERIES"])

result = []

for name, group in grouped:
    group = group.sort_values(by="DATE")
    group["gap"] = (group["OPEN"] - group["CLOSE"].shift(1)) * 100 / group["CLOSE"].shift(1)
    group["vol_chg"] = group["TOTTRDVAL"].pct_change()
    result.append(pd.DataFrame(group.iloc[-1]).T)

result = pd.concat(result)
result = result[result.DATE==result.DATE.max()]

print(result[(result.vol_chg>=3) & (result.gap>=3) & (result.CLOSE >= 200)])
