import mysql.connector
from libs.c_mysql import USER, PASSWD, HOST, DATABASE


class ConnectBdd:
    def __init__(self):
        """ mysql management """
        self.db = mysql.connector.connect(user=USER, password=PASSWD, host=HOST, database=DATABASE)
        self.cursor = self.db.cursor(buffered=True)
        self.result = []

    def execute_mysql_sel(self, query):
        """ mysql select """
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        return self.result

    def execute_mysql_count(self, query):
        """ mysql select count """
        result_count = self.cursor.execute(query)
        return result_count

    def execute_mysql_ins(self, query):
        """ mysql insert """
        self.cursor.execute(query)

    def execute_mysql_ins_data(self, query, data):
        """ mysql insert """
        self.cursor.execute(query, data)

    def destroy_mysql(self):
        """ mysql destroy """
        self.db.commit()
        self.cursor.close()
