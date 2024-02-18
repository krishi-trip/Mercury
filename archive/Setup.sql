-- Setup for database

DROP DATABASE IF EXISTS company;
CREATE DATABASE IF NOT EXISTS company;
USE company;

-- Table structure for table employee

DROP TABLE IF EXISTS employee;
CREATE TABLE employee (
  fname char(10) NOT NULL,
  lname char(20) NOT NULL,
  ssn decimal(9,0) NOT NULL,
  bdate date NOT NULL,
  address char(30) NOT NULL,
  sex char(1) NOT NULL,
  salary decimal(5,0) NOT NULL,
  superssn decimal(9,0) DEFAULT NULL,
  dno decimal(1,0) NOT NULL,
  PRIMARY KEY (ssn),
  KEY dno (dno),
  KEY empemp (superssn)
) ENGINE=InnoDB;

-- Dumping data for table employee

-- INSERT INTO employee VALUES ('John','Smith',123456789,'1965-01-09','731 Fondren, Houston TX','M',30000,333445555,5),('Franklin','Wong',333445555,'1955-12-08','638 Voss, Houston TX','M',40000,888665555,5),('Joyce','English',453453453,'1972-07-31','5631 Rice, Houston TX','F',25000,333445555,5),('Ramesh','Narayan',666884444,'1962-09-15','975 Fire Oak, Humble TX','M',38000,333445555,5),('James','Borg',888665555,'1937-11-10','450 Stone, Houston TX','M',55000,NULL,1),('Jennifer','Wallace',987654321,'1941-06-20','291 Berry, Bellaire TX','F',43000,888665555,4),('Ahmad','Jabbar',987987987,'1969-03-29','980 Dallas, Houston TX','M',25000,987654321,4),('Alicia','Zelaya',999887777,'1968-01-19','3321 Castle, Spring TX','F',25000,987654321,4);


-- ALTER TABLE employee ADD CONSTRAINT empemp FOREIGN KEY (superssn) REFERENCES employee (ssn);
-- ALTER TABLE employee ADD CONSTRAINT employee_ibfk_1 FOREIGN KEY (dno) REFERENCES department (dnumber);
-- ALTER TABLE department ADD CONSTRAINT depemp FOREIGN KEY (mgrssn) REFERENCES employee (ssn);
