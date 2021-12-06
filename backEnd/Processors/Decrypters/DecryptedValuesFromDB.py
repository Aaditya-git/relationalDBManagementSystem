#IMPORTING BUILT IN PACKAGES
import sys
from pandas import DataFrame


# sys.path.append("../Encrypters")
sys.path.append("../../DummyDataGenerate")
sys.path.append("../backEnd/SQLConnectors")

# print(sys.path)
# Import Userdefined Functions
# from EnvironmentVariables import *
from DummyDataGeneration import *
# from sqlConnector import *



# selectQuery = "SELECT {} FROM {}".format(piiColoumnNames,tableName)
# resoverall = executeGetCommand(selectQuery)
# EncryptedDataFrame = DataFrame(resoverall)
# decryptedDataFrame = EncryptedDataFrame
# for rowIndex, row in EncryptedDataFrame.iterrows():
#     for colIndex,col in enumerate(row):
#         # print('this rowIndex{} colIndex{} elemetn {}'.format(rowIndex,colIndex,col))
#         decryptedDataFrame.iloc[rowIndex,colIndex] = wrapperDecyptFunction(col)
# # Release Memory
# EncryptedDataFrame = DataFrame()
# print(decryptedDataFrame)
# decryptedDataFrame.to_csv('../FileParsers/DecryptedCSV.csv')
