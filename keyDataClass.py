import sqlite3

class KeyDataConn:

    def __init__(self, user_database):
        self.user_database = user_database

    def getAllUserData(self):
        self.con = sqlite3.connect(self.user_database)
        self.cur = self.con.cursor()
        exec = self.cur.execute('SELECT * from person_table')
        userList = []
        for row in exec:
            userList.append([row[0], row[1], row[2], row[3]])

        return userList


