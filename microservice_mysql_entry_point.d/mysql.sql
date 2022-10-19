CREATE DATABASE InoversityLibrary;
CREATE USER 'LibraryUser'@'%' IDENTIFIED BY 'LibraryUser';
GRANT ALL PRIVILEGES ON InoversityLibrary.* TO 'LibraryUser'@'%';
