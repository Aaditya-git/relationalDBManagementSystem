import sys
import os
import shutil

sys.path.append('C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem')
sys.path.append('C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem\\relationalDataBaseManagement\\relationalDataBaseManagement')

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from backEnd.DummyDataGenerate.DummyDataGeneration import getStudentDetailsCSV
from backEnd.Processors.SendEmailNotification.sendEmail import sendMailUsingSMTP,sendMailUsingSMTPToUser
from settings import *
from backEnd.propertyFiles.utility import deleteFilesInFolder,renameFile,saveFile,getListOfStrings,handleMarks
from EnvironmentVariables import InputFolderPath



def home(request):
    return(render(request, "home.html", {"text":"home"}))

def index(request):
    if request.method=="POST" and request.FILES["studentIds"]:

        # DELETE EXISTING FILES BEFORE SAVING NEW FILES
        deleteFilesInFolder(InputFolderPath)

        # TAKE INPUTS FROM HTML FROM A POST CALL
        userEmail = request.POST.getlist('email')
        inputFields = request.POST.getlist('inputFields')
        companyName = request.POST.getlist('company')
        # if 'tenthGrade' in inputFields:
        #     inputFields = inputFields + marks
        inputFields = handleMarks(inputFields)

        inputeCSVFile = request.FILES["studentIds"]

        # SAVE CSV FILE TO DESIRED LOCATION
        saveFile(inputeCSVFile,MEDIA_ROOT)

        # GET THE DETAILS OF INTERESTED STUDENTS IN THE CSV
        getStudentDetailsCSV(inputFields)

        # SEND EMAIL TO DESIRED EMAIL
        # sendMailUsingSMTP()
        sendMailUsingSMTPToUser(userEmail,companyName[0])

        return(render(request, "home.html", {"text":"Your Email was sent to:{}".format(getListOfStrings(userEmail))}))
    return(render(request, "index2.html"))
