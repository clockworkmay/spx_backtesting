import numpy as np
import pandas as pd

def spx30MinRangeBlocks(testDateRange, spxPrice):
    # TEST: what is the range of SPX in 30 minute blocks? are there calmer periods than others?

    spxPriceRange = []
    for dateToCheck in testDateRange:
        currDateToCheck = dateToCheck
        startTime = currDateToCheck.replace(hour=9, minute=30)
        endTime = currDateToCheck.replace(hour=16, minute=1)
        timeArray = np.arange(startTime, endTime, np.timedelta64(30, 'm'), dtype='datetime64')

        timeInd = 0
        dayPriceRange = []
        while timeInd < len(timeArray) - 1:
            startTimeInterval = timeArray[timeInd]
            endTimeInterval = timeArray[timeInd + 1]
            spxPriceSub = spxPrice.loc[startTimeInterval:endTimeInterval]
            maxSpxPrice = spxPriceSub.high.max()
            minSpxPrice = spxPriceSub.low.min()
            rangeSpxPrice = maxSpxPrice - minSpxPrice
            dayPriceRange.append(rangeSpxPrice)
            timeInd = timeInd + 1

        spxPriceRange.append(dayPriceRange)

    spxPriceDataFrame = pd.DataFrame(spxPriceRange, index=testDateRange, columns=timeArray[1:len(timeArray)])

    spxPriceDataFrameMean = spxPriceDataFrame.mean()

    return spxPriceDataFrameMean

def spxEarlyRangeBoundTest(testDateRange, spxPrice):
    # TEST: how many days stay within the range defined by 9:30 to 10 (and increasing in 30 min increments) the whole day?

    breachMinMaxArray = []
    breachFinalArray = []
    for dateToCheck in testDateRange:
        currDateToCheck = dateToCheck
        startTime = currDateToCheck.replace(hour=9, minute=30)
        endTime = currDateToCheck.replace(hour=16, minute=1)
        closeTime = currDateToCheck.replace(hour=16, minute=0)
        startCheckTime = currDateToCheck.replace(hour=10, minute=00)
        endCheckTime = currDateToCheck.replace(hour=16, minute=1)
        timeArray = np.arange(startCheckTime, endCheckTime, np.timedelta64(30, 'm'), dtype='datetime64')

        spxPriceSub = spxPrice.loc[startTime:endTime]
        maxFullSpxPrice = spxPriceSub.high.max()
        minFullSpxPrice = spxPriceSub.low.min()
        endFullSpxPrice = spxPrice.loc[closeTime].close

        timeInd = 0
        breachMinMax = []
        breachFinal = []
        while timeInd < len(timeArray):
            startTimeInterval = startTime
            endTimeInterval = timeArray[timeInd]
            spxPriceSub = spxPrice.loc[startTimeInterval:endTimeInterval]
            maxSpxPrice = spxPriceSub.high.max()
            minSpxPrice = spxPriceSub.low.min()

            breachedMinMax = 0
            if maxFullSpxPrice > maxSpxPrice or minFullSpxPrice < minSpxPrice:
                breachedMinMax = 1

            breachedFinal = 0
            if endFullSpxPrice > maxSpxPrice or endFullSpxPrice < minSpxPrice:
                breachedFinal = 1

            breachMinMax.append(breachedMinMax)
            breachFinal.append(breachedFinal)
            timeInd = timeInd + 1

        breachMinMaxArray.append(breachMinMax)
        breachFinalArray.append(breachFinal)

    breachMinMaxDataFrame = pd.DataFrame(breachMinMaxArray, index=testDateRange, columns=timeArray)
    breachFinalDataFrame = pd.DataFrame(breachFinalArray, index=testDateRange, columns=timeArray)

    breachMinMaxPercentage = breachMinMaxDataFrame.sum() / len(testDateRange)
    breachFinalPercentage = breachFinalDataFrame.sum() / len(testDateRange)

    return breachMinMaxPercentage, breachFinalPercentage