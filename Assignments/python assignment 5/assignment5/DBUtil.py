from mysql.connector import connect


class DBUtil:
    def __init__(self, host, user, password, port, database):
        self.connection = connect(
            host="localhost",
            user="root",
            password="root",
            port="3306",
            database="ticketBookingSystem"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            self.cursor.fetchall()
        except Exception as e:
            print(f"Query Execution Error! {e}")
            self.connection.rollback()

    def fetch_all(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"FetchAll Error: {e}")
            self.connection.rollback()
            return None

    def fetch_one(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print(f"FetchOne Error: {e}")
            self.connection.rollback()
            return None

    def close_connection(self):
        self.cursor.fetchall()
        self.cursor.close()
        self.connection.close()


# Example usage:
if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = "Root"
    port = 3306
    database = "ticketbookingsystem"

    db_util = DBUtil(host, user, password, port, database)

    query = "SELECT * FROM Event"

    db_util.execute_query(query)

    result_all = db_util.fetch_all(query)
    if result_all:
        print(result_all)
    else:
        print("Error fetching all rows.")

    result_one = db_util.fetch_one(query)
    if result_one:
        print(result_one)
    else:
        print("Error fetching one row.")

    db_util.close_connection()
