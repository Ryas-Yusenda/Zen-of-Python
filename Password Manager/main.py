import pandas as pd
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import uic
from cryptography.fernet import Fernet

class ConnSqlite():
    
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS Account (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user varchar(255) NOT NULL,
            password varchar(255) NOT NULL
            )""")
        self.conn.commit()
        
    def create_data(self, user, password):
        self.cur.execute("INSERT INTO Account (user, password) VALUES (?, ?)", (user, password))
        self.conn.commit() 

    def update_data(self, id, user, password):
        self.cur.execute("UPDATE Account SET user = ?, password = ? WHERE id = ?", (user, password, id))
    
    def read_data(self):
        sql = pd.read_sql_query("SELECT * FROM Account", self.conn)
        df = pd.DataFrame(sql, columns=['id', 'user', 'password'])
        return df
    
    def delete_data(self, id):
        self.cur.execute("DELETE FROM Account WHERE id = ?", (id,))
        self.conn.commit()
    
    def encrypt_data(self, data, key=None):
        # HVpI4sVXEbpTxbSpqHyvZa5I0-rpvtC2F0UPm11YyuM=
        if key != None:
            f = Fernet(key)
            token = f.encrypt(data.encode())
            return token
    
    def decrypt_data(self, data, key=None):
        if key != None:
            f = Fernet(key)
            token = f.decrypt(data).decode()
            return token
        
class MyGUI(QMainWindow):

    def __init__(self):

        super(MyGUI, self).__init__()
        uic.loadUi("./design.ui", self)

        self.show()
        
        self.sqlConn = ConnSqlite()
        
        self.saveButton.clicked.connect(self.saveData)
        self.unlockButton.clicked.connect(self.showData)
    
    def showData(self):
        data = self.sqlConn.read_data()
        for i in range(len(data)):
            self.tableWidget.insertRow(i)
            key = self.keyInput.text()
            self.tableWidget.setItem(i, 0, QTableWidgetItem(self.sqlConn.decrypt_data(data['user'][i], key)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(self.sqlConn.decrypt_data(data['password'][i], key)))
    
    def saveData(self):
        username = self.usernameInput.text() if self.usernameInput.text() != "" else False
        password = self.passwordInput.text() if self.passwordInput.text() != "" else False
        
        if username and password:
            key = self.keyInput.text()
            username = self.sqlConn.encrypt_data(username, key)
            password = self.sqlConn.encrypt_data(password, key)
            self.sqlConn.create_data(username, password)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            print('Window closed')
        else:
            event.ignore()
            
def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()