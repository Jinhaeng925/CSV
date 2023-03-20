# 1) Handle error checking using try and except
# 2) change file to use death valley data
# 3) Use the try except method
# using the datetime module
# adding dates to the x axis

import csv
from datetime import datetime
import matplotlib.pyplot as plt

infile_s = open("sitka_weather_2018_simple.csv")
csvfile_s = csv.reader(infile_s)
header_row_s = next(csvfile_s)

s_station_index = -1
s_name_index = -1
s_name = ""
s_tmax_index = -1
s_tmin_index = -1
s_date_index = -1

print("Index and Column Header for Sitka")
for index, column_header in enumerate(header_row_s):
    print(index, column_header)
    if column_header == "STATION":
        s_station_index = index
        # print(f"Sitka {column_header}= {s_station_index}")
    if column_header == "NAME":
        s_name_index = index
        # print(f"Sitka {column_header}= {s_name_index}")
    if column_header == "TMAX":
        s_tmax_index = index
        # print(f"Sitka {column_header}= {s_tmax_index}")
    if column_header == "TMIN":
        s_tmin_index = index
        # print(f"Sitka {column_header}= {s_tmin_index}")
    if column_header == "DATE":
        s_date_index = index
        # print(f"Sitka {column_header}= {s_date_index}")

highs_s = []
lows_s = []
dates_s = []

for row in csvfile_s:
    try:
        thedate = datetime.strptime(row[s_date_index], "%Y-%m-%d")
        high = int(row[s_tmax_index])
        low = int(row[s_tmin_index])
    except ValueError:
        print(f"\nMissing data for {row[s_date_index]}")
    else:
        highs_s.append(high)
        lows_s.append(low)
        dates_s.append(thedate)
        s_name = row[s_name_index]

infile_dv = open("death_valley_2018_simple.csv")
csvfile_dv = csv.reader(infile_dv)
header_row_dv = next(csvfile_dv)

dv_station_index = -1
dv_name_index = -1
dv_name = ""
dv_tmax_index = -1
dv_tmin_index = -1
dv_date_index = -1

print("Index and Column Header for Death Valley")
for index, column_header in enumerate(header_row_dv):
    print(index, column_header)
    if column_header == "STATION":
        dv_station_index = index
        # print(f"Death Valley {column_header}= {dv_station_index}")
    if column_header == "NAME":
        dv_name_index = index
        # print(f"Death Valley {column_header}= {dv_name_index}")
    if column_header == "TMAX":
        dv_tmax_index = index
        # print(f"Death Valley {column_header}= {dv_tmax_index}")
    if column_header == "TMIN":
        dv_tmin_index = index
        # print(f"Death Valley {column_header}= {dv_tmin_index}")
    if column_header == "DATE":
        dv_date_index = index
        # print(f"Death Valley {column_header}= {dv_date_index}")

highs_dv = []
lows_dv = []
dates_dv = []

for row in csvfile_dv:
    try:
        thedate = datetime.strptime(row[dv_date_index], "%Y-%m-%d")
        high = int(row[dv_tmax_index])
        low = int(row[dv_tmin_index])
    except ValueError:
        print(f"\nMissing data for {row[dv_date_index]}")
    else:
        highs_dv.append(high)
        lows_dv.append(low)
        dates_dv.append(thedate)
        dv_name = row[dv_name_index]

fig = plt.figure()

plt.suptitle(f"Temperature comparison between {s_name} and {dv_name}")

plt.subplot(2, 1, 1)
plt.plot(dates_s, highs_s, c="red", alpha=0.5)
plt.plot(dates_s, lows_s, c="blue", alpha=0.5)
plt.fill_between(dates_s, highs_s, lows_s, facecolor="purple", alpha=0.2)

plt.title(f"{s_name}", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.subplot(2, 1, 2)
plt.plot(dates_dv, highs_dv, c="red", alpha=0.5)
plt.plot(dates_dv, lows_dv, c="blue", alpha=0.5)
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor="purple", alpha=0.2)

plt.title(f"{dv_name}", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

fig.autofmt_xdate()

plt.show()
