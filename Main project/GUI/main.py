# Mini-Project year-3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QGridLayout


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")
        self.resize(500, 120)
        self.user_dictionary = {}

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font size>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('please enter your username: ')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font size>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('please enter your password: ')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_signUp = QPushButton('SignUp')
        button_signUp.clicked.connect(self.save_password)
        layout.addWidget(button_signUp, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        self.setLayout(layout)

    def save_password(self):
        msg = QMessageBox()
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        if username not in self.user_dictionary:
            self.user_dictionary[username] = password
        else:
            print("Username is already exists")
        print(self.user_dictionary)

    def check_password(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        if username not in self.user_dictionary:
            print("username is not exist")
        if self.user_dictionary[username] == password:
            print("enter to the application.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LoginForm()
    form.show()

    sys.exit(app.exec_())
