# csv2sql
Generates SQL Insert statement from csv file

You must chmod +ux csv2sql.py.  

Currently, the csv file you are working with should be named category1.csv.  
csv2sql.py assumes there is a header row in the csv.  
When the script is run, it creates a text file named tableData.sql with
INSERT INTO Category VALUES(col1, col2, col3...);
