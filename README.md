<h2 align="center">PDF Merger Desktop Application 🖨️ </h2> 

<p align="center"> 
Single Page Application built using React and  <a href="http://www.boredapi.com/">bored api</a>
</p>
  
## 📝 Table of Contents  
- [About](#about)  
- [Deployment](#deployment) 
- [Usage](#usage)
- [Built Using](#built_using)
- [Acknowledgments](#acknowledgement)  
- [License](#license)  
  
## 🏁 About <a name = "#getting_started"></a>  
I receive some documents via Mail that I scan and store in a safe space. Some documents include
more than one page which creates a collection of single PDF file when scanned. Hence, I wanted to build
a quick and easy tool that merges all these pdf files into single file.

There are many options available online to merge PDF files but I do not trust any online "Free" source where
I have to upload my sensitive PDF documents to another site just to merge them. Hence, the idea formed to build my own PDF Merger desktop application.


## 🚀 Deployment <a name = "deployment"></a>  
- Get one of the latest release zip file
- Unzip the file and you'll find Program.exe file inside
- Double click the executable and it should start
  
## 🎈 Usage <a name="usage"></a>  
- The application is divided into three parts. Top most part has a button labelled `Save To`. When user clicks this button, a pop up appears where user can select the location to save their merged PDF file.
- Middle half has a big shaded area, this location allows user to drag and drop multiple PDF files that will be merged.
- User can also order the files in sequence they want them to appear in merged outcome.
- Finally, at the bottom, we have two buttons: `Merge` and `Cancel`.
- When user clicks on merge, the merging process will start and file named `merged.pdf` will be placed in 
the location specified by user
- When user presses `Cancel`, the application is reset so user can perform the merge operation on new set of files again.
  
## ⛏️ Built Using <a name = "built_using"></a>  
- Python3
- PyPDF2
- PyQt5
  
## 👏 Acknowledgements <a name = "acknowledgement"></a>    
- The free landing page has been acquired from here https://cruip.com/demos/solid/. All credit goes to their respective owners.
  
## 📝 License <a name = "acknowledgement"></a>  
- MIT



