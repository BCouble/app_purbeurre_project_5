import mysql.connector
from libs.constant import USER, PASSWD, HOST, DATABASE


class Connect_bdd:
    def __init__(self):
        """ mysql management """
        self.db = mysql.connector.connect(user=USER, password=PASSWD, host=HOST, database=DATABASE)
        self.cursor = self.db.cursor(buffered=True)
        self.result = []

    def execute_mysql(self, query):
        """ mysql req """
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        return self.result

    def destroy_mysql(self):
        """ mysql destroy """
        self.cursor.close()
