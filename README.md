# Al Arsenault - w205_project
This GitHub repository contains the files for my W205 project. The project is an analysis of campaign contributions
in the 2016 US Presidential Race.

Files in this repository are broken down into groups:

- Executable Files:
-    - extract.py  - goes to the www.fec.gov website and downloads the Candidate, Committee, Pass-through Contributions
-    and Individual Contributions files. This program downloads .zip files. They need to be unzipped and given the proper names for the next phase of the project. Once the downloaded files are unzipped, they are pipe-delimited text files.
-    create_nodes_and_edges.py - takes the unzipped, pipe-delimited files, and processes them. Each file is first read in, and a complete .csv file is created with all data. The primary part of processing is done by taking each row of data from each file, selecting only those elements needed for the analysis, and creating new .csv files containing only those data elements. The files that are output from this program are used as node and edge files by Neo4J, and as input files by Tableau. The data elements in the initial master files and the elements in the output files are shown in the file "W205 Project Data Formats.pdf". The most interesting step in the data cleaning is the need to remove commas from name fields. When names are listed as "last name, first name" the comma will cause problems in the analysis phase if it is left in. 
-    

Documentation files:
- W205 Project Data Formats.pdf - as noted above, this file contains the structure of the initial files, and the structure of the final, .csv files
- Architecture - a summary of the overall project architecture
- 
Results files:
- there are several files that contain screen shots from previous runs of the project, from both Tableau and Neo4J
- 

