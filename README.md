# News Website Log Analysis Report Program

## Project Overview 
This program creates an internal reporting tool that uses information from the News database to discover what kind of articles the site's readers like. The generated analysis report displays three pieces of information:
1. Most Popular Three Articles of All Time
2. Most Popular Article Authors of All Time
3. Days with More Than 1%% of Requests Leading to Errors

When the program is executed, the Log Analysis report will be created and output to the console as plain text. The user can optionally redirect the console output to a text file. Instructions on how to do this are included in the Operating Instructions below.

## Installation Instructions

The following are the steps that must be followed as part of the installation before the program can be executed for the first time.

1) The loganal.py and loganaldb.py modules must be copied into a new directory within the vagrant directory on the virtual machine.
2) The newsdata.zip contains all of the PostgreSQL SQL needed to create and populate the News Database. The newsdata.zip file
must be downloaded and unzipped into the same directory where the loganal.py and loganaldb.py modules reside.
3) To load the data, cd into the vagrant directory and use the following command. Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

```
psql -d news -f newsdata.sql.
```

4) The following database views must be created before the program can run.  The following SQL queries should be run once at installation time to create the views required by the program.

```
  create view BadReqs as
  select date_trunc('day', time) as logdate, count(*) as BadCount
  from log
  where left(status,1) in ('4', '5')
  group by logdate
  order by logdate;

  create view TotReqs as
  select date_trunc('day', time) as logdate, count(*) as TotCount
  from log
  group by logdate
  order by logdate;
```
## List of Program Files Included

* loganal.py
* loganaldb.py

## Design of the Code

The application consists of two Python files, loganal.py and loganaldb.py. loganal.py contains the presentation logic to print the log analysis report. loganaldb.py contains the database access logic.

#### loganal.py

This file is the main program that is executed from the command line. The loganal.py file imports the get_loginfo function from the loganaldb.py file. Loganal.py calls the get_loginfo function to retrieve the information from the News database and Loganal.py prints that information to the console. Loganal.py calls the get_loginfo function with a "1" parameter to retrieve the data required to print the "Most Popular Three Articles of All Time" section of the report. Loganal.py calls the get_loginfo function with a "2" parameter to retrieve the data required to print the "Most Popular Article Authors of All Time" section of the report.
Loganal.py then calls the get_loginfo function with a "3" parameter to retrieve the data required to print the "Days with More Than 1%% of Requests Leading to Errors" section of the report.

#### loganaldb.py
This file contains all of the database access logic. This file contains the get_loginfo function that executes the SQL queries to read the data from the database tables.

The user executes the Log Analysis Report program by executing the loganal.py program. The loganal.py makes three calls to the "get_loginfo" function for each section of the report.  The results returned from the "get_loginfo" function are printed to the console. The "get_loginfo" function resides in the loganaldb.py program.  

When the "get_loginfo" function is called with a parameter equal to "1", the SQL is executed to get the information needed for the "Most Popular Three Articles of All Time" report section. This SQL joins the article and log tables to fetch the data for this section of the report. The SQL returns the results as a collection of strings in a Tuple. The strings returned from the SQL are displayed as lines within the section of the report.

When the "get_loginfo" function is called with a parameter equal to "2", the SQL is executed to read the information needed for the "Most Popular Article Authors of All Time" report section. This SQL joins the article, authors and log tables to fetch the data for this section of the report. The SQL returns the results as a collection of strings in a Tuple. The strings returned from the SQL are displayed as lines within the section of the report.

When the "get_loginfo" function is called with a parameter equal to "3", the SQL is executed to read the information needed for the "Days with More Than 1% of Requests Leading to Errors" report section. This SQL joins the BadReqs and TotReqs View tables to fetch the data for this section of the report. The SQL returns the results as a collection of strings in a Tuple. The strings returned from the SQL are displayed as lines within the section of the report. The SQL also utilizes a subquery.

## Operating Instructions

The program files should be placed in a new folder. The program should then be executed from the vagrant command line in that folder by entering:

```
python loganal.py > output.txt
```
The program will execute and the report will be generated and written out to the output.txt file.  

## Example of the Log Analysis Report

The following is the example of the report generated from the program. The output.txt file included in the zip file, is a sample of the report.

```
News Website Log Analysis Report

----Most Popular Three Articles of All Time----
"Candidate is jerk, alleges rival" -- 338647 views
"Bears love berries, alleges bear" -- 253801 views
"Bad things gone, say good people" -- 170098 views

----Most Popular Article Authors of All Time----
Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views

----Days with More Than 1% of Requests Leading to Errors----
Jul 17, 2016 -- 2.26% errors
```
## Credits and Acknowledgments
Created by: Steven Scanniello
Email: sscanni@comcast.net
