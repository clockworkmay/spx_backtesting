import numpy as np
import pandas as pd
import datetime

def loadSpxData(spxDataFilePaths, dateParseYmd):
    spxPrice = []
    for filepath in spxDataFilePaths:
        spxPriceCurrent = pd.read_csv(filepath,
                                      header=0,
                                      names=["date", "time", "open", "high", "low", "close", "vol"],
                                      parse_dates=[["date", "time"]],
                                      date_parser=dateParseYmd)
        spxPrice.append(spxPriceCurrent)

    spxPrice = pd.concat(spxPrice, ignore_index=True)
    spxPrice = spxPrice.set_index(["date_time"])

    return spxPrice

def checkSpxPriceData(testDateRangeInitial, spxPrice):
    # check the integrity of the loaded data
    # - keep data if there is a full set of data from 930 to 1600

    if len(testDateRangeInitial) == 0:
        dateRange = spxPrice.index.values

    testDateRange = []
    for dateToCheck in testDateRangeInitial:
        startTime = dateToCheck.replace(hour=9, minute=30)
        endTime = dateToCheck.replace(hour=16, minute=0)
        currDateRows = spxPrice.loc[startTime:endTime]

        if len(currDateRows) == 391:  # 391 = 9:30 to 16:00 - TODO a more robust check is probably needed
            testDateRange.append(dateToCheck)

    return testDateRange