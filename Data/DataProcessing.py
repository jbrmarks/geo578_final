# Author: Joe Marks
# Python v. 2.7.13

import math
import os
#import numpy



# A function to get tract numbers from 500 cities data
def getTractNumbers(fileName, tractNumbers, tractTracker):
    # Open the file to read
    with open(fileName, "r") as f:
        # Save header for reference (500 cities data may be missing the header)
        # header = f.readline().strip().split(",")
        # Iterate through each line
        for line in f:
            # For each record, parse it into its seperate attributes
            record = line.strip().split(",")
            # Check if there is a header for this file
            if(record[0] == 'StateAbbr'):
                # If there is a header, skip it
                continue
            # Get the tract number
            tractNumber = record[4].split("-")[1]
            # Place the tract number in the dictionary
            tractNumbers[tractNumber] = line
            # Also place into unused tracts for tracking
            tractTracker[tractNumber] = line

def getCensusTracts(leFileName, tractNumbers, leData, tractTracker):
    # Open the file to read
    with open(leFileName, "r") as f:
        # Save header for reference
        header = f.readline()
        # Iterate through each line
        for line in f:
            # For each record, parse it into its seperate attributes
            record = line.strip().split(",")
            # Get the tract number
            tractNumber = record[0]
            # If the tract number belongs to the city
            if tractNumber in tractNumbers:
                # Save the life expectancy information
                leData[tractNumber] = line
                # Mark as used in unusedTracts
                tractTracker[tractNumber] = 'used'
    return header
            


##def writeLEData(leData, header, writeFileName):
##    # Open the write file
##    with open(writeFileName, "w") as f:
##        # Prepare a list of comma seperated values for each line
##        writeList = []
##        # Append header to writelist
##        writeList.append(header)
##        # Get each value from dictionary and append values
##        for key in leData:
##            writeList.append(leData[key])
##        f.writelines(writeList)


def write500Data(tractNumbers, fiveHundredHeader, writeFileName):
    # Open the write file
    with open(writeFileName, "w") as f:
        # Prepare a list of comma seperated values for each line
        writeList = []
        # Append header to writelist
        writeList.append(fiveHundredHeader)
        # Get each value from dictionary and append values
        for key in tractNumbers:
            writeList.append(tractNumbers[key])
        f.writelines(writeList)
        
def writeUnusedTractsData(unusedTracts, header, writeFileName):
    # Open the write file
    with open(writeFileName, "w") as f:
        # Prepare a list of comma seperated values for each line
        writeList = []
        # Append header to writelist
        writeList.append(header)
        # Get each value from dictionary and append values
        for key in unusedTracts:
            writeList.append(unusedTracts[key])
        f.writelines(writeList)

def processCity(cityName):

    # Create empty variables
    tractNumbers = {};
    fiveHundredHeader = "StateAbbr,PlaceName,PlaceFIPS,TractFIPS,Place_TractID,Population2010,ACCESS2_CrudePrev,ACCESS2_Crude95CI,ARTHRITIS_CrudePrev,ARTHRITIS_Crude95CI,BINGE_CrudePrev,BINGE_Crude95CI,BPHIGH_CrudePrev,BPHIGH_Crude95CI,BPMED_CrudePrev,BPMED_Crude95CI,CANCER_CrudePrev,CANCER_Crude95CI,CASTHMA_CrudePrev,CASTHMA_Crude95CI,CHD_CrudePrev,CHD_Crude95CI,CHECKUP_CrudePrev,CHECKUP_Crude95CI,CHOLSCREEN_CrudePrev,CHOLSCREEN_Crude95CI,COLON_SCREEN_CrudePrev,COLON_SCREEN_Crude95CI,COPD_CrudePrev,COPD_Crude95CI,COREM_CrudePrev,COREM_Crude95CI,COREW_CrudePrev,COREW_Crude95CI,CSMOKING_CrudePrev,CSMOKING_Crude95CI,DENTAL_CrudePrev,DENTAL_Crude95CI,DIABETES_CrudePrev,DIABETES_Crude95CI,HIGHCHOL_CrudePrev,HIGHCHOL_Crude95CI,KIDNEY_CrudePrev,KIDNEY_Crude95CI,LPA_CrudePrev,LPA_Crude95CI,MAMMOUSE_CrudePrev,MAMMOUSE_Crude95CI,MHLTH_CrudePrev,MHLTH_Crude95CI,OBESITY_CrudePrev,OBESITY_Crude95CI,PAPTEST_CrudePrev,PAPTEST_Crude95CI,PHLTH_CrudePrev,PHLTH_Crude95CI,SLEEP_CrudePrev,SLEEP_Crude95CI,STROKE_CrudePrev,STROKE_Crude95CI,TEETHLOST_CrudePrev,TEETHLOST_Crude95CI,Geolocation\n"
    leData = {};
    tractTracker = {};
    unusedTracts = {};

    # Path names
    fiveHundredPath = cityName + "/" + cityName + "_500.csv"
    lepath = cityName + "/" + cityName.split("_")[-1] + "_A.csv"
    leOutputPath = cityName + "/" + cityName + "_LE.csv"
    unusedTractsPath = cityName + "/" + cityName + "_unusedTracts.csv"

    getTractNumbers(fiveHundredPath, tractNumbers, tractTracker)
    print "500 data successfully imported"

    header = getCensusTracts(lepath, tractNumbers, leData, tractTracker)
    print "Life expectancy data successfully imported"

    # Delete output file if it already exists
    if os.path.exists(leOutputPath):
        os.remove(leOutputPath);

    writeLEData(leData,header, leOutputPath)
    print ("Life expectancy data successfully written")

    # Delete output file if it already exists
    if os.path.exists(fiveHundredPath):
        os.remove(fiveHundredPath);

    writeLEData(tractNumbers,fiveHundredHeader, fiveHundredPath)
    print ("Header added to 500 data")
    
    # Create dict of unused tracts
    for key in tractTracker:
        if tractTracker[key] != 'used':
            unusedTracts[key] = tractTracker[key]
    
    # Delete output file if it already exists
    if os.path.exists(unusedTractsPath):
        os.remove(unusedTractsPath);

    writeLEData(unusedTracts, fiveHundredHeader, unusedTractsPath)
    print ("Unused tracts written to file")


# Main function
if __name__ == "__main__":

    processCity("Boston_MA")
    processCity("Denver_CO")
    processCity("Detroit_MI")
    processCity("Las_Vegas_NV")
    processCity("Memphis_TN")
    processCity("Nashville_TN")
    processCity("Oklahoma_City_OK")
    processCity("Portland_OR")
    processCity("Seattle_WA")
    processCity("Washington_DC")

    


