# Passenger air transportation


This project is databases learning project. Whole workflow was divided into three stages: 
1. Description of subject area and development ER-diagram.
2. Database schema development, creating database in postgresql, filling in the database.
3. Writing database queries.

## Description of subject area and development ER-diagram. ##

In results first stage was developed [ER-diagram of subject area](https://github.com/MikhailCherepanovD/Passenger-air-transportation/blob/master/ERDiagram.pdf). 


## Database schema development ##
There was developed following scheme of database:
![](https://raw.githubusercontent.com/MikhailCherepanovD/Passenger-air-transportation/master/SchemeDB.jpg)



Also representasion in PDF:
[Scheme of database](https://github.com/MikhailCherepanovD/Passenger-air-transportation/blob/master/SchemeDB.pdf);


Code for creating a database in postgresql: [creating database](https://github.com/MikhailCherepanovD/Passenger-air-transportation/blob/master/CreateDB.sql);

### Filling database ###

Database filling is implemented in python using the psycopg2 library. The filling takes place in a random order.

Code for filling database in python: [filling database](https://github.com/MikhailCherepanovD/Passenger-air-transportation/blob/master/InsertingTables.py);


## Queries to database 

The text of queries in russian language:
[Description of requests](https://github.com/MikhailCherepanovD/Passenger-air-transportation/blob/master/RequestsRussianLang.txt);


Database queries in postgresql language:
[requests in postgresql](https://github.com/MikhailCherepanovD/Passenger-air-transportation/blob/master/Requests.sql);




## Dependencies

1. Creating:  PostgreSQL 14;
2. Filling: Python 3, psycopg2, numpy.


## To run

1. git clone [git@github.com:MikhailCherepanovD/Passenger-air-transportation.git](git@github.com:MikhailCherepanovD/Passenger-air-transportation.git)

2. To create database:

```
psql -h localhost -p 5432 -U postgres -c "CREATE DATABASE airtransportation;"

psql -h localhost -p 5432 -U postgres -d airtransportation -f createDB.sql

```
2. To fill database:

```
python3 ./ InsertingTables.py

```

