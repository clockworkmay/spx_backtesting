# spx backtesting

import numpy as np
import pandas as pd
from datetime import datetime

import backtests
import utilities

# testing parameters
startDate = "2016-01-01"
endDate = "2021-06-30"

# spxDataFilePaths = {
#     "data/SANDP-500_160101_161231.txt",
#     "data/SANDP-500_170101_171231.txt",
#     "data/SANDP-500_180101_181231.txt",
#     "data/SANDP-500_190101_191231.txt",
#     "data/SANDP-500_200101_201231.txt",
#     "data/SANDP-500_210101_210701.txt"}
spxDataFilePaths = {
    "data/SANDP-500_160101_161231.txt"}

## SETUP ##

# testing parameters setup
testDateRangeInitial = pd.date_range(startDate, endDate)
dateParseYmd = lambda x: datetime.strptime(x, "%Y%m%d %H%M%S")

# load pricing data file and check its integrity
spxPrice = utilities.loadSpxData(spxDataFilePaths, dateParseYmd)
testDateRange = utilities.checkSpxPriceData(testDateRangeInitial, spxPrice)

## TESTING ##

# TEST: what is the range of SPX in 30 minute blocks? are there calmer periods than others?
spx30MinRangeBlocks = backtests.spx30MinRangeBlocks(testDateRange, spxPrice)

# TEST: how many days stay within the range defined by 9:30 to 10 (and increasing in 30 min increments) the whole day?
# checked a few entries with https://www.barchart.com/stocks/quotes/$SPX/interactive-chart
# breachMinMaxPercentage, breachFinalPercentage = backtests.spxEarlyRangeBoundTest(testDateRange, spxPrice)

lala = 0

# TEST: does the range set by 9:30 to 10:05 hold until 12? 1? Does the range set by 1:30 to 2:05 hold until 3? 4?


# VERTICALS: how often does SPX end within a certain range of its staring price?

# VERTICALS: how often does SPX end within its expected move?

# VERTICALS: at what point in the day is SPX's final price rangebound?

# VERTICALS: how often is a gap (and continued trend after 10 min) indicative of a upward move? or same with gapdown?

# M2W: how often does SPX end within $0.50 of its price at 3:55?

# GENERAL: when in the day is SPX most frothy? are there flat periods during the day?

# TEST: