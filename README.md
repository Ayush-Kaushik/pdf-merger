# PDF Merger Desktop Application

### Motivation to build:
I receive some documents via Mail that I scan and store in a safe space. Some documents include
more than one page which creates a collection of single PDF file when scanned. Hence, I wanted to build
a quick and easy tool that merges all these pdf files into single file.

There are many options available online to merge PDF files but I do not trust any online "Free" source where
I have to upload my sensitive PDF documents just to merge them. Hence, the idea formed to build my own PDF Merger desktop application.

### What I learned from this project?
- Re-enforced my Python syntactical skills and tried to follow OOP approach to have extensibility in mind
- GitHub actions and utilized free resource to build and package my application that could be shipped
- Using PyQT5, PYPDF2 and Pyinstaller for the first time so it was a good learning experience 

## How to run this application
- Get one of the latest release zip file
- Unzip the file and you'll find Program.exe file inside
- Double click the executable and it should start

## How to use this application
- The application is divided into three parts. Top most part has a button labelled `Save To`. When user clicks this button, a pop up appears where user can select the location to save their merged PDF file.
- Middle half has a big shaded area, this location allows user to drag and drop multiple PDF files that will be merged.
- User can also order the files in sequence they want them to appear in merged outcome.
- Finally, at the bottom, we have two buttons: `Merge` and `Cancel`.
- When user clicks on merge, the merging process will start and file named `merged.pdf` will be placed in 
the location specified by user
- When user presses `cancel`, the application is reset so user can perform the merge operation on new set of files again.