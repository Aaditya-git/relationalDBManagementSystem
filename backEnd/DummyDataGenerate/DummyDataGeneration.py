# Importing Builtin Libraries
import sys
import string
import random
import pandas as pd
from pandas import DataFrame

# APPENDING PATH FOR IMPORTING Libraries
sys.path.append("C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem\\backEnd\\propertyFiles")
sys.path.append("C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem\\backEnd\\SQLConnectors")
sys.path.append("C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem\\backEnd\\Processors\\Encrypters")
sys.path.append("C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem\\backEnd\\Processors\\SendEmailNotification")
sys.path.append("C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem\\backEnd\\DummyDataGenerate")

# Importing User defined Modules
from sqlConnector import *
from dummyDataPayload import *
# from encryDecryFn import fillEnctryptedValues
from utility import *
from sendEmail import sendMailUsingSMTP

def fillEnctryptedValues(reqPiilist):

    encrypted = []

    # GO THOUGH LOOP OF COLOUMNS AND ENCRYPT VALUES
    for index, colvalue in enumerate(reqPiilist):

        # GET ENCRYPTED VALUE OF COLOUMN FROM PIIDATA
        encryptedValue = wrapperEncryptFunction(colvalue)

        # APPEND IT TO ENCRYPTED ARRAY
        encrypted.append(encryptedValue)


    return encrypted

def getStudentDetailsCSV(reqColss):

    coloumnToBeFetched=getAllColoumnstoFetch(reqColss)
    reqColStr = getListOfStrings(coloumnToBeFetched)
    interestedStudents = setInterestedStudentsFromCSV()

    executeSQ = selectQuery.format(reqColStr,tableName,interestedStudents)
    resoverall = executeGetCommand(executeSQ)

    EncryptedDataFrame = DataFrame(resoverall,columns = coloumnToBeFetched)

    decryptedDataFrame = EncryptedDataFrame
    for rowIndex, row in EncryptedDataFrame.iterrows():
        for colIndex,col in enumerate(coloumnToBeFetched):

            if col in piicolumnName:
            # print('this rowIndex{} colIndex{} elemetn {}'.format(rowIndex,colIndex,col))
                decryptedDataFrame.iloc[rowIndex,colIndex] = wrapperDecyptFunction(row[col])
            else:
                decryptedDataFrame.iloc[rowIndex,colIndex] = row[col]

    # Release Memory
    EncryptedDataFrame = DataFrame()
    # print(EncryptedDataFrame)
    # print(decryptedDataFrame)
    decryptedDataFrame.to_csv('C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem\\backEnd\\outputs\\StudentDetails.csv')
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
    path = "C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem\\backEnd\\output\\StudentDetails.csv"

    # insertDummyData()
    # getStudentDetailsCSV(inputFields)
    # sendMailUsingSMTP()
