The purpose of this lab is to interact with a mySQL database via a python program.

1. In mysql, create a database called `lab11`.
2. Download the file `lab11.sql` and use it to populate the database `lab11`. From the folder where you downloaded the file, start `mysql` then:
   `create database lab11`
   `use lab11;`
   `source lab11.sql;`
3. Using Pycharm, create a new Python project called lab11.
4. Install the mysql connector in the virtual environment. Look at the file on Brightspabce if you do not know how to do that.
5. Create a function `insertGrade` that receives 4 parameters, a `lastName`, a `firstName`, a `province` and a `grade`. The function then connects to the database `lab11` and inserts the record.
6. Create a function `deleteGrade` that receives 4 parameters, a `lastName`, a `firstName`, a `province` and a `grade`. The function then connects to the database `lab11` and deletes that record.
7. Create a function `displayGrade`  that receives 3 parameters, a `lastName`, a `firstName`, a `province`.Make sure your query uses the sql LIKE function. The function then connects to the database `lab11` and returns a list of grades.
8. The 3 functions should make use of the function `readDbConfig` from the sample program available on Brightspace and github, zip file `week11.zip`
9. Write a python program that proposes the following options:

   - Enter a grade
   - Display a grade
   - Delete a grade
   - Exit

   For the display grade option, display the list of results as a html table, ie: generate the html code.
10. Upload your `py` file to Github.
