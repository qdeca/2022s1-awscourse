# Museum data manipulation

The goal of the exercise is to make you manipulate some more S3 and the RDS, thanks to psycopg2 and boto3

The goals are the following :
- get the csv file and load it in S3
- execute the python code to load the table in the RDS (replace the connection parameters with your own)
  by installing the following packages :
  - pip3 (sudo yum install pip)
  - python3-devel (sudo yum install python3-devel)
  - postgresql-devel (sudo yum install postgresql-devel)
  - gcc (sudo yum install gcc)
  - psycopg2 (pip install psycopg2)
- modify the code to then load the csv field in the RDS
- add some sql to create a table with only free museums in Paris
- add some sql to create a mini table that aggregates the sum of all free museum and the sum of all non-free ones, for each region