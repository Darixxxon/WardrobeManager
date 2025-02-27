USE WARDROBE_DB


CREATE TABLE Shoes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    Brand VARCHAR(255),
    Model VARCHAR(255),
    Size VARCHAR(50),
    Type VARCHAR(100),
    Colour_1 VARCHAR(50),
    Colour_2 VARCHAR(50),
    Dir VARCHAR(255),
    New BIT DEFAULT 1
);

CREATE TABLE Pants (
    id INT IDENTITY(1,1) PRIMARY KEY,
    Brand VARCHAR(255),
    Size VARCHAR(50),
    Length VARCHAR(50),
    Type VARCHAR(100),
    Style VARCHAR(100),
    Colour_1 VARCHAR(50),
    Colour_2 VARCHAR(50),
    Dir VARCHAR(255),
    New BIT DEFAULT 1
);

CREATE TABLE Bases (
    id INT IDENTITY(1,1) PRIMARY KEY,
    Brand VARCHAR(255),
    Size VARCHAR(50),
    Length VARCHAR(50),
    Type VARCHAR(100),
    Style VARCHAR(100),
    Colour_1 VARCHAR(50),
    Colour_2 VARCHAR(50),
    Dir VARCHAR(255),
    New BIT DEFAULT 1
);

CREATE TABLE Overtops (
    id INT IDENTITY(1,1) PRIMARY KEY,
    Brand VARCHAR(255),
    Size VARCHAR(50),
    Type VARCHAR(100),
    Style VARCHAR(100),
    Colour_1 VARCHAR(50),
    Colour_2 VARCHAR(50),
    Dir VARCHAR(255),
    New BIT DEFAULT 1
);

CREATE TABLE Coats (
    id INT IDENTITY(1,1) PRIMARY KEY,
    Brand VARCHAR(255),
    Size VARCHAR(50),
    Type VARCHAR(100),
    Style VARCHAR(100),
    Colour_1 VARCHAR(50),
    Colour_2 VARCHAR(50),
    Dir VARCHAR(255),
    New BIT DEFAULT 1
);

CREATE TABLE Hats (
    id INT IDENTITY(1,1) PRIMARY KEY,
    Brand VARCHAR(255),
    Size VARCHAR(50),
    Type VARCHAR(100),
    Colour_1 VARCHAR(50),
    Colour_2 VARCHAR(50),
    Dir VARCHAR(255),
    New BIT DEFAULT 1
);

CREATE TABLE Combinations (
    id INT IDENTITY(1,1) PRIMARY KEY,
    shoes_id INT REFERENCES Shoes(id),
    pants_id INT REFERENCES Pants(id),
    base_id INT REFERENCES Bases(id),
    overtop_id INT NULL REFERENCES Overtops(id),
    coat_id INT NULL REFERENCES Coats(id),
    hat_id INT NULL REFERENCES Hats(id),
    reviewed BIT DEFAULT 0,
    rate INT NULL
);
