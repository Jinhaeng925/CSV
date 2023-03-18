# 1) changing the file to include all the data for the year of 2018
# 2) change the title to - Daily and low high temperatures - 2018
# 3) extract low temps from th efile and add to chart
# 4) shade in the area between high and low

# using the datetime module
# adding dates to the x axis

import csv
from datetime import datetime
import matplotlib.pyplot as plt

infile = open("sitka_weather_2018_simple.csv")
csvfile = csv.reader(infile)

header_row = next(csvfile)

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
lows = []
dates = []

mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(mydate)

for row in csvfile:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    thedate = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(thedate)

# print(highs)


fig = plt.figure()

plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor="purple", alpha=0.2)

plt.title("Daily and Low High Temperatures - 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

fig.autofmt_xdate()

plt.show()


# 1) changing the file to include all the data for the year of 2018
# 2) change the title to - Daily and low high temperatures - 2018
# 3) extract low temps from th efile and add to chart
# 4) shade in the area between high and low

# using the datetime module
# adding dates to the x axis

"""

FROM ChatGPT

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = (
    "sitka_weather_2018_simple.csv"  # Change file name to include all data for 2018
)
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get high, low temperatures, and dates
    highs, lows, dates = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)

# Plot the high and low temperatures
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot
plt.title("Daily and Low High Temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

fig.autofmt_xdate()

plt.show()
"""
