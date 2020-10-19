# merge_pdf
## Description
Merge pdf files, in order, from specific folder. 
## How to use
Run de program by terminal. 

Write the path of the .pdf files, and opcional the destination folder to the merge files.
If you only type the pdfs file path, the merge file will make in the parent folder.
The program auto complite the name file and use a generic name if you lost write it. 
If destination file already exist, a warning is displayed
### Use example
**$ python3 main.py usr/pdfsFolder** # Merge pdf files from the folder, and generate the mergeFile.pdf in parent folder (usr)

**$ python3 main.py usr/pdfsFolder usr/pdfsMergeFolder** # Merge pdf files from the folder, and generate the mergeFile.pdf in specific folder

**$ python3 main.py usr/pdfsFolder usr/pdfsMergeFolder/myfile.pdf** # Merge pdf files from the folder, and generate the mergeFile.pdf in specific folder with other name (myfile.pdf)

**$ python3 main.py usr/pdfsFolder usr/pdfsMergeFolder/myfile** # Merge pdf files from the folder, and generate the mergeFile.pdf in specific folder with other name (myfile.pdf (it workd to without extension))

---
# merge_pdf (ESPAÑOL)
## Descripción
Fusionar archivos pdf, en orden desde una carpeta específica. 

## Como usar
Ejecute el programa desde terminal 

Escribe la ruta de los archivos .pdf y opcionalmente el folder de destino para unir los archivos. 
Si solo escribes la ruta de los pdfs, el archivo de fusión se creará en el directorio padre. 
El programa autocompleta el nombre del archivo y usa un nombre genérica si tu olvidas escribirlo.
Si el archivo de destino ya existe, se mostrará una advertencia.

### Ejemplo de uso
**$ python3 main.py usr/pdfsFolder** # Unir los archivos pdf de la carpeta y crear el archivo mergeFile.pdf en el directorio padre. 

**$ python3 main.py usr/pdfsFolder usr/pdfsMergeFolder** # Unir los archivos pdf de la carpeta y crear el archivo mergeFile.pdf en unca carpeta en específico.

**$ python3 main.py usr/pdfsFolder usr/pdfsMergeFolder/myfile.pdf** # Unir los archivos pdf de la carpeta y crear el archivo mergeFile.pdf en unca carpeta en específico con otro nombre (myfile.pdf)

**$ python3 main.py usr/pdfsFolder usr/pdfsMergeFolder/myfile** # Unir los archivos pdf de la carpeta y crear el archivo mergeFile.pdf en unca carpeta en específico con otro nombre (myfile.pdf (funciona también sin la extensión))




