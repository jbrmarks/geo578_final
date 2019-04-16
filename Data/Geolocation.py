# Author: Joe Marks
# Python v. 2.7.13

import math
import os
#import numpy



# A function to get tract numbers from 500 cities data
def getData(fileName, tractNumbers):
    # Open the file to read
    with open(fileName, "r") as f:
        header = ""
        # Iterate through each line
        for line in f:
            # For each record, parse it into its seperate attributes
            record = line.split(",")
            # Check if there is a header for this file
            if(record[0] == 'StateAbbr'):
                # If there is a header, save it then continue skip it
                header = line
                header = header.strip() + ",lat,long\n"
                continue
            # Get the tract number
            tractNumber = record[4].split("-")[1]
            # Seperate lat and long
            latitude = record[8].split("(")[1]
            longitude = record[9].strip().split(")")[0]
            # Add latlong onto line
            line = line.strip() + "," + latitude + "," + longitude + "\n"
            # Place the tract number in the dictionary
            tractNumbers[tractNumber] = line
        return header
     


def writeData(tractNumbers, header, writeFileName):
    # Open the write file
    with open(writeFileName, "w") as f:
        # Prepare a list of comma seperated values for each line
        writeList = []
        # Append header to writelist
        writeList.append(header)
        # Get each value from dictionary and append values
        for key in tractNumbers:
            writeList.append(tractNumbers[key])
        f.writelines(writeList)
        


def processCity(cityName):

    # Create empty variables
    tractNumbers = {};

    # Path names
    fiveHundredPath = cityName + "/" + cityName + "_500.csv"


    header = getData(fiveHundredPath, tractNumbers)
    print "500 data successfully imported"


    # Delete output file if it already exists
    if os.path.exists(fiveHundredPath):
        os.remove(fiveHundredPath);

    writeData(tractNumbers, header, fiveHundredPath)
    print ("Geolocation split")
    


# Main function
if __name__ == "__main__":

#    processCity("Boston_MA")
    processCity("Denver_CO")
    processCity("Detroit_MI")
    processCity("Las_Vegas_NV")
    processCity("Memphis_TN")
    processCity("Nashville_TN")
    processCity("Oklahoma_City_OK")
    processCity("Portland_OR")
    processCity("Seattle_WA")
    processCity("Washington_DC")

    


