# Importing Builtin Libraries
import sys
import string
import random
import pandas as pd

# APPENDING PATH FOR IMPORTING Libraries
sys.path.append("C:/Users/lenovo/data structure in python/BE project/rdms/relationalDBManagementSystem/backEnd/propertyFiles")
sys.path.append("C:/Users/lenovo/data structure in python/BE project/rdms/relationalDBManagementSystem/backEnd/SQLConnectors")
sys.path.append("C:/Users/lenovo/data structure in python/BE project/rdms/relationalDBManagementSystem/backEnd/Processors/Encrypters")

# Importing User defined Modules
from sqlConnector import *
from EnvironmentVariables import *
from dummyDataPayload import *
from Encryption import *


# COMMAND TO GET LOWERBOUND
getLowerBoundCmd = getLowerBound.format(tableName)

# GET LOWERBOUND
maxValueInDB = executeGetCommand(getLowerBoundCmd)

# RETURNS A TUPLE - GET FIRST ELEMENT
if maxValueInDB[0][0] == None:
    lowerBound = 0
else:
    lowerBound = maxValueInDB[0][0] + 1

upperBound = lowerBound + numberofDummyDataToBeInserted

# number of characters in the PrefixEmail string.
maxLengthOfPrefixEmail = 9

# Get command Executed
commandString = ""
templateString = "{}"
comma = ","

piiColumns = [firstname,surname,email,aadhar,PAN,passport,mobileNumber,permanantAddress,residentialAddress]

# RUN FOR LOOP TO GENERATE DUMMY DATA -- ROW WISE
# DYNAMIC NUMBER IS BASICALLY ROW_NUMBER
for dynamicNumber in range (lowerBound, upperBound):

    # CREATE RANDOM ALPHANUMERIC EMAIL FOR INSERTION
    alphaNumericEmail = ''.join(random.choices(string.ascii_uppercase + string.digits, k = maxLengthOfPrefixEmail))
    RandomGrade_10 = round(random.uniform(55.0, 99.9),1)
    RandomGrade_12 = round(random.uniform(55.0, 99.9),1)
    # INITIALISE EMPTY ENCRYPTED ARRAY TO STORE ENCRYPTED VALUES OF 9 COLOUMNS
    ans = fillEnctryptedValues(alphaNumericEmail,dynamicNumber)

    # INITIALISE 42 COLOUMNS LENTH STRING TO FILL UP VALUES
    templateString = """({},"{}","{}","{}","{}","{}","{}",{},"{}",{},"{}",{},"{}",{},"{}","{}","{}","{}",{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})"""
    commandString = commandString + templateString.format(int(rollNumber.format(dynamicNumber)),registrationId.format(dynamicNumber),encrypted[0],encrypted[1],
                                                          fathersName.format(dynamicNumber),mothersName.format(dynamicNumber),encrypted[2],isAadhar,encrypted[3],
                                                          isPAN,encrypted[4],isPassport,encrypted[5],isIndian,nationality,encrypted[6],
                                                          encrypted[7],encrypted[8],tenthCGPA,twelthCGPA,tenthGrade.format(RandomGrade_10),twelthGrade.format(RandomGrade_12),firstSemCGPA,secondSemCGPA,
                                                          thirdSemCGPA,fourthSemCGPA,fifthSemCGPA,sixthSemCGPA,seventhSemCGPA,eightthSemGCPA,isDiploma,diplomaMarks,isBacklog,numberOfBacklogs,activeBacklog,
                                                          PassiveBacklog,isYD,YDYears,isEducationGap,educationGapYears,isPICTStudent,currentBatch)

    # ADD COMMA AFTER EVERY ROW BUT LAST ONE
    if(dynamicNumber<upperBound-1):
        commandString = commandString + ","


# print(insertData.format(tableName,coloumnNames,commandString))

# Execute Command to Insert Values
# result = executeInsertCommand(insertData.format(tableName,coloumnNames,commandString))

# Sample of Rows inserted
print("Total rows inserted {}".format(numberofDummyDataToBeInserted))

# decryption function
from pandas import DataFrame
selectQuery = "SELECT {} FROM {}".format(piiColoumnNames,tableName)
resoverall = executeGetCommand(selectQuery)
piiColoumnNamesdf = ["firstname","surname","email","aadhar","PAN","passport","mobileNumber","permanantAddress","residentialAddress"]
df = pd.DataFrame(resoverall,columns = piiColoumnNamesdf)
print(df)
# df.columns = resoverall.keys()
dataFrameDecrypted = DataFrame()


for index, row in df.iterrows():
    decrypted = []

    # GO THOUGH LOOP OF COLOUMNS AND ENCRYPT VALUES
    for colName in piiColoumnNamesdf:
        decryptedValue = wrapperDecyptFunction(row[colName])
        decrypted.append(decryptedValue)

    zipped = zip(piiColoumnNamesdf,decrypted)
    a_dictionary = dict(zipped)
    dataFrameDecrypted = dataFrameDecrypted.append(a_dictionary,True)

#DataFrame to CSV AND REMOVED FIRST COLUMN (SR. NO.)
dataFrameDecrypted.to_csv('decrypted.csv',index=False)
print(dataFrameDecrypted)
