# merge_pdf
## Description
By terminal **merge pdf files**, in order, from specific folder.

# Install modules
```bash
$ pip install PyPDF2
```

## How to use
Run de program by **terminal.** 

Write the **path of the .pdf files**, and opcional the **destination folder** to the merge files.
If you **only type the pdfs file path**, the merge file will make in the **parent folder.**
The program **auto complite the name** of destiny file **file** and use a **generic name** if you lost write it. 
If **destination file already exist**, a **warning** is displayed

### Use example
```bash
# Merge pdf files from the folder, and generate the mergeFile.pdf in parent folder (usr)
$ python3 main.py usr/pdfsFolder 

# Merge pdf files from the folder, and generate the mergeFile.pdf in specific folder
$ python3 main.py usr/pdfsFolder usr/pdfsMergeFolder 

# Merge pdf files from the folder, and generate the mergeFile.pdf in specific folder with other name (myfile.pdf)
$ python3 main.py usr/pdfsFolder usr/pdfsMergeFolder/myfile.pdf

# Merge pdf files from the folder, and generate the mergeFile.pdf in specific folder with other name (myfile (it workd to without extension))
$ python3 main.py usr/pdfsFolder usr/pdfsMergeFolder/myfile 
```
