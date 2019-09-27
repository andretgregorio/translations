# Translations Query Writer
Script that reads a standarized excel file and returns a a `.sql` file with all the queries to insert or update the translation queries into the database.

## Running
In order to execute the script, you must have python 3 installed in your machine. To check if you have python3, just run `python3 --version` at your command line.

Once you have checked you python3 installation, follow the steps bellow in your command line:

1. `cd` to the project directory.
2. `python3 main.py <options>`

### Options

* *-q* or *--query*: tells the script to generate INSERT or UPDATE queries. Accepted values are 'insert' or 'update'.
* *-i* or *--initia-row*: the first line of the excel file to be included in the translation.
* *-f* or *--final-row*: the last line of the excel file to be included in the tranlsation.

### Exemples
*Generate queries to insert values from line 42 to line 47:*
```python3 main.py -q=insert -i=42 -f=47```