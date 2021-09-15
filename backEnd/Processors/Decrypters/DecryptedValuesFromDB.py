#IMPORTING BUILT IN PACKAGES
import sys
from pandas import DataFrame
sys.path.append("hardCodedpath/backEnd/propertyFiles")
# sys.path.append("../Encrypters")
sys.path.append("hardCodedpath/DummyDataGeneration")
sys.path.append("hardCodedpath/SQLConnectors")

# Import Userdefined Functions
from EnvironmentVariables import *
from dummyDataPayload import *
from sqlConnector import executeGetCommand



selectQuery = "SELECT {} FROM {}".format(piiColoumnNames,tableName)
resoverall = executeGetCommand(selectQuery)
df = DataFrame(resoverall)
# df.columns = resoverall.keys()

print(df)
