# Python_and_SQL
Using Python to connect to Oracle DB

This Python script is a simple database management system for students. It uses the oracledb module to connect to an Oracle database.
This script provides a simple interface for managing student data in an Oracle database. It allows the user to perform basic CRUD (Create, Read, Update, Delete) operations on the T_PY_ALUNO table. It also includes an option to import student data from a CSV file. 

The script first attempts to establish a connection to the Oracle database using the oracledb.connect() function. If the connection fails, it sets a flag 'conexao' to False and prints the error. If the connection is successful, it sets 'conexao' to True.
The script then enters a loop that continues as long as conexao is True. In this loop, it presents a menu to the user with various options related to student management, such as:
1) retrieving all students;
2) listing a student by ID;
3) registering a new student;
4) updating a student’s information
5) deleting a student;
6) deleting all students;
7) saving the data to a CSV file;
8) exiting the application
  
Depending on the user’s choice, the script performs different database operations using SQL queries. These operations include:

### Retrieving all students:
It executes a SELECT * FROM T_PY_ALUNO query to fetch all records from the T_PY_ALUNO table.

### Listing a student by ID: 
It prompts the user for a student ID, then executes a SELECT * FROM T_PY_ALUNO WHERE id = {id_aluno} query to fetch the record of the student with the given ID.

### Registering a new student: 
It prompts the user for the student’s details, then executes an INSERT INTO T_PY_ALUNO (nome, idade, endereco, curso) VALUES ('{nome}', {idade}, '{endereco}', '{curso}') query to insert a new record into the T_PY_ALUNO table.
OBS: nome = name ; idade = age ; endereco = address ; curso = course

### Updating a student’s information: 
It prompts the user for a student ID and the new details, then executes an UPDATE T_PY_ALUNO SET nome = '{nome}', idade = {idade}, endereco = '{endereco}', curso='{curso}' WHERE id = {id} query to update the record of the student with the given ID.

### Deleting a student: 
It prompts the user for a student ID, then executes a DELETE FROM T_PY_ALUNO WHERE id = {id} query to delete the record of the student with the given ID.

### Deleting all students: 
If the user chooses option 6, the script executes a DELETE FROM T_PY_ALUNO query to delete all records from the T_PY_ALUNO table.

### Importing students from a CSV file: 
If the user chooses option 7, the script imports student data from a CSV file named ‘alunos.csv’. It reads the file line by line, and for each line, it executes an INSERT INTO T_PY_ALUNO (nome, idade, endereco, curso) VALUES (:1, :2, :3, :4) query to insert a new record into the T_PY_ALUNO table. The values are taken from the current line of the CSV file.

### Exiting the application:
If the user chooses option 8, the script sets conexao to False, which causes the loop to exit. It then closes the database connection.

- Performed for the Database Application & Data Science course.
- Code made in the Replit IDE.

