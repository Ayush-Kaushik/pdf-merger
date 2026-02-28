<h2 align="center">File Merger Desktop Application 🖨️ </h2>

Merge `PDF`, `JPEG` and `PNG` files on your laptop with ease in a safe and secure manner with `File Merger`. No need to use online tools that could potentially store your personal data.

## Build Status
| Branch | Status |
| --------------- | --------------- |
| Main | [![PDF Merger](https://github.com/Ayush-Kaushik/pdf-merger/actions/workflows/main.yml/badge.svg)](https://github.com/Ayush-Kaushik/pdf-merger/actions/workflows/main.yml)| 
| Release | [![PDF Merger](https://github.com/Ayush-Kaushik/pdf-merger/actions/workflows/release.yml/badge.svg)](https://github.com/Ayush-Kaushik/pdf-merger/actions/workflows/release.yml) |

## Table of Contents  
- [Build Status](#build-status)
- [Table of Contents](#table-of-contents)
- [About ](#about-)
- [Deployment ](#deployment-)
- [Usage ](#usage-)
  - [Merging PDF Files](#merging-pdf-files)
  - [Merging Images](#merging-images)
  - [When incorrect file extension is drag-dropped](#when-incorrect-file-extension-is-drag-dropped)
- [How to run this locally?](#how-to-run-this-locally)
- [Built Using ](#built-using-)
- [Acknowledgements ](#acknowledgements-)
- [License ](#license-)
  
## About <a name = "#getting_started"></a>
I created this tool to simplify the process of merging multiple files into a single large file while working with a large volume of PDF's containing sensitive information.

Attaching multiple documents to an email can be tedious, and there is a chance that a user could forget a file. Online free options are available, but they pose a security threat as it requires uploading PDF's.

This desktop application merges all the PDF, JPG\JPEG, and PNG files into a single large file.

The tool currently supports following formats:
- `PDF`
- `JPG\JPEG`
- `PNG`


## Deployment <a name = "deployment"></a>  
- Download the latest release zip file
- Unzip the file and you'll find Program.exe file inside
- Double click the executable and it should start the program
  
## Usage <a name="usage"></a>  
### Merging PDF Files
![Merging PDF Files](./.readme/PDF_Merging.gif)

### Merging Images
![Merging Images (JPG) Files](./.readme/Image_Merging.gif)

### When incorrect file extension is drag-dropped
![Invalid Extension Error](./.readme/Invalid_Extension_Error.gif)

## How to run this locally?
- Clone the repo locally
- Setup python virtual environment (venv) with following command

```
python -m venv local_venv
```

- Activate the virtual environment
```
.\.local_venv\Scripts\activate
```

- Install all the requieed packages:
```
pip istall -r requirements.txt
```

- Now run the program with following command:
```
python -m pdf_merger.app
```

## Built Using <a name = "built_using"></a>
- Python3
- PyPDF2
- PyQt5

> [!WARNING]
> Only use the command shown above since the project uses absolute imports for packages and modules

## Acknowledgements <a name = "acknowledgement"></a>
- Free PDF's for testing found here: https://freetestdata.com/document-files/pdf/
- Sample image files found here: https://file-examples.com/
  
## License <a name = "acknowledgement"></a>  
- MIT
