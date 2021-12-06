# Importing Builtin Libraries
import sys
import string
import random
import pandas as pd
from pandas import DataFrame

# Importing User defined Modules
from backEnd.SQLConnectors.sqlConnector import *
from backEnd.DummyDataGenerate.dummyDataPayload import *

from backEnd.Utilities.utility import *
from backEnd.Utilities.SendEmailNotification.sendEmail import sendMailUsingSMTP

# THIS FUNCTION WILL RETURN ENCRYPTED VALUES FOR PII DATA FOR DUMMY DATA
def getEnctryptedValuesForPII(reqPIIList):

    encryptedPIIData = []

    # GO THOUGH LOOP OF COLOUMNS AND ENCRYPT VALUES
    for index, colValue in enumerate(reqPIIList):

        # GET ENCRYPTED VALUE OF COLOUMN FROM PIIDATA
        encryptedPIIValue = wrapperEncryptFunction(colValue)

        # APPEND IT TO ENCRYPTED ARRAY
        encryptedPIIData.append(encryptedPIIValue)


    return encryptedPIIData

# THIS FUNCTION WILL CREATE A CSV FILE AT A FIXED LOCATION WITH THE STUDENT DETAILS
def getStudentDetailsCSV(coloumnsRequestedFromWeb):

    # This variable will contain all coloumns - FIXED + REQUESTED
    coloumnToBeFetched=getAllColoumnstoFetch(coloumnsRequestedFromWeb)

    reqColStr = getListOfStrings(coloumnToBeFetched)

    # Get the List of Interested Students from CSV provided as INPUT
    interestedStudents = setInterestedStudentsFromCSV()

    # Store a Query to be Executed to fetch the Coloumns from DB for Interested Students
    executeSQ = selectQuery.format(reqColStr,tableName,interestedStudents)
    resoverall = executeGetCommand(executeSQ)

    # Create a DataFrame of the returned result
    EncryptedDataFrame = DataFrame(resoverall,columns = coloumnToBeFetched)

    decryptedDataFrame = EncryptedDataFrame

    # LOOP over DataFrame from DB to decrypt the encrypted values in DB
    for rowIndex, row in EncryptedDataFrame.iterrows():

        for colIndex,col in enumerate(coloumnToBeFetched):

            if col in piicolumnName:

                decryptedDataFrame.iloc[rowIndex,colIndex] = wrapperDecyptFunction(row[col])
            else:

                decryptedDataFrame.iloc[rowIndex,colIndex] = row[col]

    # Release Memory
    EncryptedDataFrame = DataFrame()

    decryptedDataFrame.to_csv('backEnd\\outputs\\StudentDetails.csv')
    print(decryptedDataFrame)

def insertDummyData():
        # COMMAND TO GET LOWERBOUND
        getLowerBoundCmd = getLowerBound.format(tableName)

        # GET LOWERBOUND
        maxValueInDB = executeGetCommand(getLowerBoundCmd)
        # print('max value is {}'.format(maxValueInDB))

        # RETURNS A TUPLE - GET FIRST ELEMENT
        if maxValueInDB[0][0] == None:
            lowerBound = 0
        else:
            lowerBound = maxValueInDB[0][0] + 1
        upperBound = lowerBound + numberofDummyDataToBeInserted

        # Get command Executed
        commandString = ""
        templateString = "{}"
        comma = ","

        # RUN FOR LOOP TO GENERATE DUMMY DATA -- ROW WISE
        # DYNAMIC NUMBER IS BASICALLY ROW_NUMBER
        for rowValue in range (lowerBound, upperBound):
            # CREATE RANDOM ALPHANUMERIC EMAIL FOR INSERTION
            firstnameid = firstname.format(getFirstname())
            surnameid = surname.format(getSurname())
            rollnumberid = rollNumber.format(getRollno())
            registrationNo = registrationId.format(getRandomNum(maxReglen))
            emailid = email.format(getRandomAlphaNum(maxLengthOfPrefixEmail))
            aadharid = aadhar.format(getRandomNum(maxAadharlen))
            mobileid = mobileNumber.format(getRandomNum(maxMobileLen))
            panid = PAN.format(getRandomAlphaNum(maxPanlen))
            passid = passport.format(getRandomAlphaNum(maxPassLen))
            perAdd = permanantAddress.format(getAddress(maxAddlen))
            resAdd = residentialAddress.format(getAddress(maxAddlen))

            # Selecting 10th and 12 th Grade
            RandomGrade_10 = getMarks()
            RandomGrade_12 = getMarks()

            # 1st to 6th sem cgpas'
            firstCGPA = getCgpa()
            secondCGPA = getCgpa()
            thirdCGPA = getCgpa()
            fourthCGPA = getCgpa()
            fifthCGPA = getCgpa()
            sixthCGPA = getCgpa()

            InitialName = getFirstname()
            MiddleName = getFatherName()
            MotherInitial = getMotherName()
            FamilyName = getSurname()
            regisId = getRegistrationId()

            # INITIALISE EMPTY ENCRYPTED ARRAY TO STORE ENCRYPTED VALUES OF 9 COLOUMNS
            reqPiilist = []
            reqPiilist.append(firstnameid)

            reqPiilist.extend((surnameid,rollnumberid,registrationNo,emailid,aadharid,mobileid,panid,passid,perAdd,resAdd))

            encrypted = fillEnctryptedValues(reqPiilist)

            # INITIALISE 42 COLOUMNS LENTH STRING TO FILL UP VALUES
            templateString = """({},"{}","{}","{}","{}","{}","{}",{},"{}",{},"{}",{},"{}",{},"{}","{}","{}","{}",{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})"""
            commandString = commandString + templateString.format(int(rollNumber.format(rollnumberid)),registrationId.format(id[regisId].format(registrationNo)),encrypted[0],encrypted[1],
                                                                  fathersName.format(MiddleName),mothersName.format(MotherInitial),encrypted[4],isAadhar,encrypted[3],
                                                                  isPAN,encrypted[7],isPassport,encrypted[8],isIndian,nationality,encrypted[6],
                                                                  encrypted[9],encrypted[10],tenthCGPA,twelthCGPA,tenthGrade.format(RandomGrade_10),twelthGrade.format(RandomGrade_12),firstSemCGPA.format(firstCGPA),secondSemCGPA.format(secondCGPA),
                                                                  thirdSemCGPA.format(thirdCGPA),fourthSemCGPA.format(fourthCGPA),fifthSemCGPA.format(fifthCGPA),sixthSemCGPA.format(sixthCGPA),seventhSemCGPA,eightthSemGCPA,isDiploma,diplomaMarks,isBacklog,numberOfBacklogs,activeBacklog,
                                                                  PassiveBacklog,isYD,YDYears,isEducationGap,educationGapYears,isPICTStudent,currentBatch)

            # ADD COMMA AFTER EVERY ROW BUT LAST ONE
            if(rowValue<upperBound-1):
                commandString = commandString + ","
            else:
                commandString = commandString + ";"

        # print(insertData.format(tableName,coloumnNames,commandString))

        # Execute Command to Insert Values
        result = executeInsertCommand(insertData.format(tableName,coloumnNames,commandString))

        # Sample of Rows inserted
        print("Total rows inserted {}".format(numberofDummyDataToBeInserted))
if __name__ == '__main__':
    # insertDummyData()
    # getStudentDetailsCSV()
    # insertDummyData()
    # getStudentDetailsCSV(inputFields)
    # sendMailUsingSMTP()
