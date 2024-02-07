import pymysql

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            DBConnection.connection = pymysql.connect(
                host="localhost",
                user="root",
                password="root",
                port=3306,
                database="Ecommerce"
            )
            cur = DBConnection.connection.cursor()



        return DBConnection.connection

    @staticmethod
    def close_connection():
        if DBConnection.connection is not None:
            DBConnection.connection.close()

    def fetchall(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"FetchAll Error: {e}")
            self.connection.rollback()

    def fetchOne(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchone()
        except:
            print(f"FetchOne Error!")
            self.connection.rollback()

    def closeConnection(self):
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    DBConnection.get_connection()  # Call the get_connection method
