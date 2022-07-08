# Transaction Load

The goals of this exercise are the following :

- Set up an EC2 using a key pair, and access it programmatically using SSH (bonus : try to preinstall git when setting up the EC2 so that you don't have to do it once inside the instance)

- clone this project into the EC2 using the git command

- look at the format of the transaction files contained in the _resources_ folder

- create a lambda function that will trigger whenever a transaction file is put in a certain bucket of S3, and for each file, creates 2 files in another bucket, one display the sum of purchases for the day (a day is equivalent to a file) and the other the sum of sales for the day
  
- load the files into the source bucket, and check that your lambda function works