CREATE DATABASE InoversityLibrary;
GO

CREATE SCHEMA InoversityLibraryModel;
GO

CREATE ROLE Developers;
GO

-- TODO: parse the password and user id as variables from the .env global file
CREATE LOGIN LibraryAdmin WITH PASSWORD = 'xP3msnxkAd5MXg&?';
GO

CREATE USER LibraryAdmin FOR LOGIN LibraryAdmin;
GO

ALTER ROLE Developers ADD MEMBER [LibraryAdmin];
GO

GRANT CONTROL ON SCHEMA :: InoversityLibraryModel TO Developers;
GO
