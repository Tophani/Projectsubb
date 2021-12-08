import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'lib',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
     """CREATE TABLE IF NOT EXISTS Account(
        name VARCHAR(255),
        Email VARCHAR(80),
        Phone_number INT,
        type VARCHAR(255),
        password VARCHAR(30),
        ID INT NOT NULL AUTO_INCREMENT,
        PRIMARY KEY(ID)

        )
        """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Books(
        genres VARCHAR(255),
        Author VARCHAR(255),
        Title VARCHAR(255)
        )
        """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Upload(
        Book VARCHAR(255),
        Author VARCHAR(255),
        View VARCHAR(255),
        location VARCHAR(255)

        )
        """
)