CSC1034: Practical 2
====================

This package is build as a part of the CSC1-34: Portfolio 1

This package allows analysis and display of proteins from Uniprot.


Useful Commands
-------------------
pipenv run python uniplot.py dump #Passes the data and displays the full set of data

pipenv run python uniplot.py list #Passes the data and displays the names of the proteins in the data

pipenv run python uniplot.py average #Passes the data and gives the average length of the protein

pipenv run python uniplot.py graph #Passes the data through to create a bar chart plot.py

pipenv run python uniplot.py pie #Passes the data through to create a pie chart in plot.py

pipenv run python uniplot.py help #Gives all commands user can use


How to use a different file
----------------------------
To use a different file, the user will be asked for a filename and need to input a file which exists.

If the user is not careful and uses even one letter in the wrong case then it will not run the intended file or not run
any file at all.

The 2 filenames that can be used without issue are:

- uniprot_receptor.xml.gz
- uniprot_sprot_small.xml.gz


Depth of Taxonomy
----------------------------
Depth allows the user to input which level of taxonomy you want, the higher the number the more categories there would
be.
This works for the bar chart and pie chart because the taxonomy is needed for each part of the bar and pie chart.
The only problem a user may experience is if they input a number for the taxonomy level which is too large.
