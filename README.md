# Translations Query Writer
Script that reads a standarized excel file and returns a a `.sql` file with all the queries to insert or update the translation queries into the database.

## Running
In order to execute the script, you must have python 3 installed in your machine. To check if you have python3, just run `python3 --version` at your command line.

Once you have checked you python3 installation, follow the steps bellow in your command line:

1. `cd` to the project directory.
2. `$ pip install`
3. `python3 main.py <options>`

### Options

* *-q* or *--query*: string: tells the script to generate INSERT or UPDATE queries. Accepted values are 'insert', 'update_value' or 'update_translation_status'.
* *-i* or *--initia-row*: int: the first line minus 1 of the excel file to be included in the translation. Ex: if you want to start at the line 3, use -i=2.
* *-f* or *--final-row*: int: the last line of the excel file to be included in the tranlsation. This is really the last line.
* *-ts* or *--translation-status*: int: the translation status for the query.
* *-l* or *--locations*: string: a list of desired locations to generate the query. The locations should be comma separated.

### Exemples
*Generate queries to insert values for all locations from line 42 to line 47, with a translation_status of 10:*
```python3 main.py -q=insert -i=41 -f=47```

*Generates query to update only a few location to translation_status to 0:*
```python3 main.py -q=update_translation_status -i=41 -f=47 -ts=0 -l=es_Cl,es_AR,es_MX```

*Generates query to update the value of all locations in the file:*
```python3 main.py -q=update_value -i=3 -f=8```