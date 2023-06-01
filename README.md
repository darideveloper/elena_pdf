<div><a href='https://github.com/github.com/darideveloper/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/github.com/darideveloper.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/elena_pdf/blob/master/Elena%20PDF%20logo.png?raw=true' alt='Elena PDF' height='80px'/>

# Elena PDF

Manage pdf files fast and easy Merge, split, convert pdf to image and convert images to pdf

Start date: **2023-03-27**

Last update: **2023-03-27**

Project type: **personal's project**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#run'>Run</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a></div>

# Install

```bash
$ pip install elena-pdf
```

## Windows

Installing last version of Microsoft Visual [C++ Redistributable](https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0)


## Linux

Most distros ship with `pdftoppm` and `pdftocairo`. If they are not installed, refer to your package manager to install `poppler-utils`

## Mac

Mac users will have to install [poppler for Mac](http://macappstore.org/poppler/).

# Run

## Merge pdf files

List of files to merge
``` python
files_to_merge = [
    "c:my_folder01.pdf",
    "c:my_folder02.pdf",
    "c:my_folder03.pdf"
]
```

Instance of the class
``` python
my_elena = elena.PdfManager (files_to_merge, replace=True, debug=True)

# replace: replace destination file if exist
# debug: print program status during execution
```

Merge file and save in specific output file
``` python
my_elena.merge("c:output_folderoutput_file.pdf")
```

Merge file and save in specific folder, with default output file name
``` python
my_elena.merge("c:output_folder")
```

## Split pdf files

List of files to merge
``` python
files_to_split = [
    "c:my_folder01.pdf",
    "c:my_folder02.pdf",
    "c:my_folder03.pdf"
]
```

Instance of the class
``` python
my_elena = elena.PdfManager (files_to_split, replace=True, debug=True)

# replace: replace destination file if exist
# debug: print program status during execution
```

Split files with default base name
``` python
my_elena.split("c:output_folder")
```

Split files with specific base name
``` python
my_elena.split("c:output_folder", " page ")
```

Split files with empty base name
``` python
my_elena.split("c:output_folder", "")
```

## Convert pdf to image
Output images extension: `jpg`

List of files to merge
``` python
files_to_convert = [
    "c:my_folder01.pdf",
    "c:my_folder02.pdf",
    "c:my_folder03.pdf"
]
```

Instance of the class
``` python
my_elena = elena.PdfManager (files_to_convert, replace=True, debug=True)

# replace: replace destination file if exist
# debug: print program status during execution
```

Convert files to images with default base name
``` python
my_elena.pdf_to_img("c:output_folder")
```

Convert files to images specific base name
``` python
my_elena.pdf_to_img("c:output_folder", " page ")
```

Convert files to images with empty base name
``` python
my_elena.pdf_to_img("c:output_folder", "")
```

## Convert image to pdf
Input images extension: `jpg, eps, tga, webp, gif`

List of files to merge
``` python
files_to_convert = [
    "c:my_folder01.jpg",
    "c:my_folder02.jpg",
    "c:my_folder03.jpg"
]
```

Instance of the class
``` python
my_elena = elena.PdfManager (files_to_convert, replace=True, debug=True)

# replace: replace destination file if exist
# debug: print program status during execution
```

Convert imges to pdf files, and generate one file for image
``` python
my_elena.pdf_to_img("c:output_folder")
```

Convert imges to pdf files, and merge in one oputput file
``` python
my_elena.pdf_to_img("c:output_folder", "c:output_folderimages_converted.pdf")
```

# Roadmap

* [X] Merge pdf files
* [X] Split pdf files
* [X] Convert pdf to image
* [X] Convert image to pdf


