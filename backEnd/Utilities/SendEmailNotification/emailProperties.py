from backEnd.propertyFiles.EnvironmentVariables import BASE_DIR

# SMTP PARAMETERS
EMAIL_SUBJECT = "TNP Made Easy by Amey | StudentDetails | {}"
EMAIL_FROM = 'no.reply.tnpproject@gmail.com'
EMAIL_TO = ['bamey2241997@gmail.com','aadityab134@gmail.com','danimanas28@gmail.com']
MESSAGE_BODY = "Please find attached File with the requested Details."
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "no.reply.tnpproject@gmail.com"
SMTP_PASSWORD = "aykewuftgquwrshm"

# ATTACHMENT PARAMTERS
PROJECT_PATH_FOR_CSV_FILE = "\\backEnd\\outputs\\"
OUTPUT_CSV_FILE_NAME="StudentDetails.csv"
PATH_TO_CSV_FILE = BASE_DIR + PROJECT_PATH_FOR_CSV_FILE + OUTPUT_CSV_FILE_NAME
FILE_NAME_TOBE_MAILED = "studentDetails_{}.csv"
