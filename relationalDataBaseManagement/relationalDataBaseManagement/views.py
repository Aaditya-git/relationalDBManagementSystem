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
from backEnd.propertyFiles.utility import deleteFilesInFolder,renameFile,saveFile,getListOfStrings
from EnvironmentVariables import InputFolderPath




def home(request):
    return(render(request, "home.html", {"text":"home"}))

def index(request):
    if request.method=="POST" and request.FILES["studentIds"]:

        # DELETE EXISTING FILES BEFORE SAVING NEW FILES
        deleteFilesInFolder(InputFolderPath)

        # TAKE INPUTS FROM HTML FROM A POST CALL
        inputFields = request.POST.getlist('inputFields')
        userEmail = request.POST.getlist('email')
        inputeCSVFile = request.FILES["studentIds"]

        # SAVE CSV FILE TO DESIRED LOCATION
        saveFile(inputeCSVFile,MEDIA_ROOT)

        # GET THE DETAILS OF INTERESTED STUDENTS IN THE CSV
        getStudentDetailsCSV(inputFields)

        # SEND EMAIL TO DESIRED EMAIL
        # sendMailUsingSMTP()
        sendMailUsingSMTPToUser(userEmail)

        return(render(request, "home.html", {"text":"Your Email was sent to:{}".format(getListOfStrings(userEmail))}))
    return(render(request, "index.html"))
