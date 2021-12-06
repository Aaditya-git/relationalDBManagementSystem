# ==============================================================
# ======================= SQL PROPERTIES =======================
# ==============================================================

# CONNECTION PROPERTIES
dbUserName = "rdmsUser"

# tobe Encrypted
# password = "gAAAAABhK7M5eUiWIJw4mPdQUWeTo1AshWyTRI6gJ-THPlTuPYYhHMnY1Llrb0gKZ9ZN0bpAkNvXeWezPLnYR2B1fBUu5FwKZg==" --rootPaass
password = "gAAAAABhK576ntIFAmqgnXs6u06dtzHoJbPGzXNXTjRIRve-Z9aBF3Ztvtsz3fH6d2_QMtve15emipkg0Q_GcOAnYRMJiNxaUg=="
hostName = "localhost"
portName = "3306"

# TABLE PROPERTIES
dbName = "rdms"
tableName = "studentdetails"
coloumnNames = "rollNumber,registrationId,firstname,surname,fathersName,mothersName,email,isAadhar,aadhar,isPAN,PAN,\
isPassport,passport,isIndian,nationality,mobileNumber,permanantAddress,residentialAddress,tenthCGPA,twelthCGPA,tenthGrade,\
twelthGrade,firstSemCGPA,secondSemCGPA,thirdSemCGPA,fourthSemCGPA,fifthSemCGPA,sixthSemCGPA,seventhSemCGPA,eightthSemGCPA,isDiploma,\
diplomaMarks,isBacklog,numberOfBacklogs,activeBacklog,PassiveBacklog,isYD,YDYears,isEducationGap,educationGapYears,isPICTStudent,currentBatch"

piiColoumnNames = "firstname,surname,email,aadhar,PAN,passport,mobileNumber,permanantAddress,residentialAddress"
piicolumnName = ['firstname','surname','email','aadhar','PAN','passport','mobileNumber','permanantAddress','residentialAddress']
reqCols = ['rollNumber','registrationId','firstname','surname','email','mobileNumber']
MandatoryDataToBeSent = ["registrationId","rollNumber","firstname","surname"]

# COMMANDS TOBE EXECUTED
# Command to get Lower Bound
getLowerBound = "SELECT MAX(rollNumber) FROM {}"

# Command to Insert Dummy Data
insertData = "INSERT INTO {} ({}) VALUES {}"

# SELECT QUESRY
selectQuery = "SELECT {} FROM {} WHERE registrationId in ({})"

# INSERT DUMMY Data
numberofDummyDataToBeInserted = 10
hardCodedpath = "C:\\Users\\lenovo\\data structure in python\\BE project\\rdms\\relationalDBManagementSystem\\backEnd"

# number of characters in the PrefixEmail string.
maxLengthOfPrefixEmail = 9
maxMobileLen = 10
maxAadharlen = 14
maxPanlen = 10
maxPassLen = 8
maxReglen = 5
maxAddlen = 10

# PII COLUMN NAMES
# piiColumns = ["firstname","surname","email","aadhar","PAN","passport","mobileNumber","permanantAddress","residentialAddress"]

# ==============================================================
# =========== ENCRYPTION AND DECRYTION PROPERTIES ==============
# ==============================================================
decreptionKey = "tN9oA_eCulJhWOF_gKEs3FdFUHzIfuj0JmDgjS-DWxo="



#================================================================
#===================Send email===================================
#================================================================
from_email='no.reply.tnpproject@gmail.com'
to_emails=['aadityab134@gmail.com','danimanas28@gmail.com','bamey2241997@gmail.com']
emailNotificationAPIKey = "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"



#================================================================
#===================File Rename==================================
#================================================================
RENAMED = "InterestedStudents.csv"





InputFolderPath = "C:/Users/lenovo/data structure in python/BE project/relationalDBManagementSystem/relationalDataBaseManagement/input"
