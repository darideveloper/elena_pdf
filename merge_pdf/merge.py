#! python3
# Combines all the pafs in the current working directory into a single pdf

import PyPDF2, os, sys

#Get all pdfs names
pdfFiles = []
dirPath = ' '
fileOutput = ' '

# Red the terminal
helpMenssage = 'Write the path of the .pdf files, and opcional the destination '
helpMenssage += 'folder to the merge file, \n(example: main.py "user/myPdfsFolder" "user/myFiles/mergeFiles.pdf").'
helpMenssage += '\nIf you only type the pdfs file path, the merge file will make in the parent folder \n(example: main.py "user/myPdfsFolder")'
if len(sys.argv) == 1: 
    print ('The program need more arguments. \n' + helpMenssage)
    sys.exit()
elif len(sys.argv) == 2:
    dirPath = sys.argv[1]
    fileOutput = os.path.join(os.path.dirname (dirPath), "mergeFiles.pdf")
elif len(sys.argv) == 3:  
    dirPath = sys.argv[1]
    fileOutput = sys.argv[2]
else: 
    print ('To much argument. \n' + helpMenssage)
    sys.exit()

if not os.path.isdir (dirPath): 
    print ("This folder dosent exist.")
    sys.exit()

#Check folder
for filename in os.listdir(dirPath):
    if filename.endswith('.pdf'): 
        pdfFiles.append(os.path.join(dirPath, filename))

# Check file and request to replice file
if os.path.isdir (fileOutput): 
    fileOutput = os.path.join(fileOutput, 'mergeFiles.pdf')
else: 
    if not fileOutput.endswith('.pdf'): 
        fileOutput += '.pdf'

if os.path.isfile(fileOutput):
    repleace = input ("The file %s already exist. Do you want to replace it (y/n)?" % (fileOutput))
    if repleace.lower()[0] != 'y': 
        print ("Program finished.")
        sys.exit()

# Order files
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# loop through all the pdf files
if pdfFiles: 
    for currentFile in pdfFiles: 
        pdfFileObj = open (currentFile, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # loop through all the pages (except the first) and add them
        print ("Merging %s " % (currentFile))
        if pdfReader.numPages: 
            for pageNum in range (0, pdfReader.numPages): 
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage (pageObj)            
    
    # Save the resulting pdf to a file
    pdfOutput = open (os.path.join(os.path.dirname(dirPath), fileOutput), 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

    print ('Done. Pages are now in %s file' % (os.path.join(dirPath, fileOutput)))
else: 
    print ("Dosent exist pdf files in this folder.")
