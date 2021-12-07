import sys
import os
import shutil

# ==============================================================
# ======================= USER IMPORTS =========================
# ==============================================================
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from backEnd.DummyDataGenerate.DummyDataGeneration import getStudentDetailsCSV
from backEnd.Utilities.SendEmailNotification.sendEmail import sendMailUsingSMTP,sendMailUsingSMTPToUser
from rdbms.relationalDataBaseManagement.settings import *
from backEnd.Utilities.utility import deleteFilesInFolder,renameFile,saveFile,getListOfStrings
from backEnd.propertyFiles.EnvironmentVariables import INPUT_FOLDER_PATH


def home(request):
    return(render(request, "home.html", {"text":"home"}))

def index(request):
    if request.method=="POST" and request.FILES["studentIds"]:

        # DELETE EXISTING FILES BEFORE SAVING NEW FILES
        deleteFilesInFolder(INPUT_FOLDER_PATH)

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
