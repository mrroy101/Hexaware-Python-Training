import mysql.connector


class DBUtil:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="root",
            database="ordermanagement"
        )

    def getDBConnection(self):
        return self.con.cursor()