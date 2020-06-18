CREATE TABLE students(id Serial, name text, address text, age int);

INSERT INTO students(name, address, age) VALUES ('Yesid', 'Mexico', '24');
INSERT INTO students(name, address, age) VALUES ('Juan', 'Mexico', '26');

select * from students;