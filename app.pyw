


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QIcon
import os

class Ui_FlaskProject(object):
    def setupUi(self, FlaskProject):
        FlaskProject.setObjectName("FlaskProject")
        FlaskProject.resize(212, 237)
        FlaskProject.setFixedSize(212, 237)
        FlaskProject.setStyleSheet("QWidget{\n"
"background-color:cyan;\n"
"}")
        self.ProjectName = QtWidgets.QLineEdit(FlaskProject)
        self.ProjectName.setGeometry(QtCore.QRect(10, 60, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProjectName.setFont(font)
        self.ProjectName.setStyleSheet("QLineEdit{\n"
"background:white;\n"
"\n"
"}")
        self.ProjectName.setObjectName("ProjectName")
        self.ProjectPath = QtWidgets.QLineEdit(FlaskProject)
        self.ProjectPath.setGeometry(QtCore.QRect(10, 110, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ProjectPath.setFont(font)
        self.ProjectPath.setStyleSheet("QLineEdit{\n"
"background:white;\n"
"\n"
"}")
        self.ProjectPath.setObjectName("ProjectPath")
        self.label1 = QtWidgets.QLabel(FlaskProject)
        self.label1.setGeometry(QtCore.QRect(0, 0, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setStyleSheet("QLabel{\n"
"color:red;\n"
"}")
        self.label1.setTextFormat(QtCore.Qt.PlainText)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.browsebutton = QtWidgets.QPushButton(FlaskProject)
        self.browsebutton.setGeometry(QtCore.QRect(70, 140, 61, 23))
        self.browsebutton.setStyleSheet("QPushButton{\n"
"background-color:blue;\n"
"color:white;\n"
"}")
        self.browsebutton.setObjectName("browsebutton")
        self.createbutton = QtWidgets.QPushButton(FlaskProject)
        self.createbutton.setGeometry(QtCore.QRect(-10, 170, 231, 31))
        self.createbutton.clicked.connect(self.Create)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.createbutton.setFont(font)
        self.createbutton.setStyleSheet("QPushButton{\n"
"background-color:green;\n"
"color:white;\n"
"}")
        self.createbutton.setObjectName("createbutton")
        self.label2 = QtWidgets.QLabel(FlaskProject)
        self.label2.setGeometry(QtCore.QRect(30, 30, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setStyleSheet("")
        self.label2.setTextFormat(QtCore.Qt.PlainText)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(FlaskProject)
        self.label3.setGeometry(QtCore.QRect(20, 80, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label3.setFont(font)
        self.label3.setStyleSheet("")
        self.label3.setTextFormat(QtCore.Qt.PlainText)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.clearbutton = QtWidgets.QPushButton(FlaskProject)
        self.clearbutton.setGeometry(QtCore.QRect(-10, 210, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.clearbutton.setFont(font)
        self.clearbutton.setStyleSheet("QPushButton{\n"
"background-color:red;\n"
"color:white;\n"
"}")
        self.clearbutton.setObjectName("clearbutton")

        self.retranslateUi(FlaskProject)
        QtCore.QMetaObject.connectSlotsByName(FlaskProject)

        
    def create_Project(self,Project_Name,pathOfProject):
        project=(f'{pathOfProject}/{Project_Name}')
        
        os.mkdir(project)
        # Static Folder
        path1 = f'{Project_Name}/static/Img'
        path2 = f'{Project_Name}/static/Css'
        path3 = f'{Project_Name}/static/Js'
        # Templates Folder and Files
        path4=f'{Project_Name}/templates'

        # Creating Folder's
        os.makedirs(path1)
        os.makedirs(path2)
        os.makedirs(path3)
        os.makedirs(path4)


        index=f'{path4}/index.html'
        with open(index,'w') as file:
                file.write(''' 
                <!doctype html>
                <html lang="en">
                <head>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">

                <!-- Bootstrap CSS -->
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">

                <title>Hello, world!</title>
                </head>
                <body>
                <h1>Hello, world!</h1>

                <!-- Optional JavaScript; choose one of the two! -->

                <!-- Option 1: Bootstrap Bundle with Popper -->
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>

                <!-- Option 2: Separate Popper and Bootstrap JS -->
                <!--
                <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js" integrity="sha384-SR1sx49pcuLnqZUnnPwx6FCym0wLsk5JZuNx2bPPENzswTNFaQU1RDvt3wT4gWFG" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.min.js" integrity="sha384-j0CNLUeiqtyaRmlzUHCPZ+Gy5fQu0dQ6eZ/xAww941Ai1SxSY+0EQqNXNE6DZiVc" crossorigin="anonymous"></script>
                -->
                </body>
                </html>

                ''')

        # <--------------------#App.py#--------------------------->
        App=f'{Project_Name}/App.py'
        with open(App,'w') as file:
                file.write('''from flask import Flask
        app = Flask(__name__)

        @app.route('/')
        def hello_world():
        return 'Hello, World!'" ''')

        css=f'{path2}/style.css'
        with open(css,'w') as file:
                file.write('''  /*Write Your Css Code Here*/ ''')

        js=f'{path3}/index.js'
        with open(js,'w') as file:
                file.write('''  /*Write Your JavaScript Code Here*/ ''')

    def Browse(self):
        try:

                qf=QFileDialog()
                directory = QFileDialog.getExistingDirectory(FlaskProject, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
                self.ProjectPath.setText(directory)
        except Exception as e:
                print(e)



    def Create(self):
        try:
        
                Project=self.ProjectName.text()
                Project_Path=self.ProjectPath.text()
                if Project=='' and Project_Path =='':
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        
                        msg.setInformativeText(f'All Fields Are Required.')
                        msg.setWindowIcon(QtGui.QIcon('logo.png'))
                        msg.setWindowTitle("Error")
                        msg.exec_()
                # elif ':' not in Project_Path:
                #         msg = QMessageBox()
                #         msg.setIcon(QMessageBox.Critical)
                        
                #         msg.setInformativeText(f'Invalid Path.')
                #         msg.setWindowIcon(QtGui.QIcon('logo.png'))
                #         msg.setWindowTitle("Error")
                #         msg.exec_()

                else:


                        self.create_Project(Project, Project_Path)

                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        
                        msg.setInformativeText(f'Project Created Successfully.\n In Directory:-\n {Project_Path} ',)
                        msg.setWindowIcon(QtGui.QIcon('logo.png'))
                        msg.setWindowTitle("Sucess")
                        msg.exec_()
        except Exception as e:
                print(e)
                if '[WinError 183]' in str(e):
                        msg = QMessageBox()
                        msg.setIcon((QMessageBox.Critical))
                        msg.setInformativeText(f'Directory Already Present.')
                        
                        msg.setWindowIcon(QtGui.QIcon('logo.png'))
                        msg.setWindowTitle("Error")
                        msg.exec_()
                elif '[WinError 3]' in str(e):
                        msg = QMessageBox()
                        msg.setIcon((QMessageBox.Critical))
                        msg.setInformativeText(f'Please enter a valid path.')
                        
                        msg.setWindowIcon(QtGui.QIcon('logo.png'))
                        msg.setWindowTitle("Invalid Path")
                        msg.exec_()

         
                
         
    def Clear(self):
        try:
            self.ProjectName.clear()
            self.ProjectPath.clear()
        except Exception as e:
                print(e)    
    def retranslateUi(self, FlaskProject):
        _translate = QtCore.QCoreApplication.translate
        FlaskProject.setWindowTitle(_translate("FPC", "FPC"))
        self.label1.setText(_translate("FlaskProject", "Flask Project Creator"))
        self.browsebutton.setText(_translate("FlaskProject", "Browse"))
        self.browsebutton.clicked.connect(self.Browse)
        self.createbutton.setText(_translate("FlaskProject", "Create"))
        self.label2.setText(_translate("FlaskProject", "Enter Your Project Name :-"))
        self.label3.setText(_translate("FlaskProject", "Enter Your Project Path :-"))
        self.clearbutton.setText(_translate("FlaskProject", "Clear"))
        self.clearbutton.clicked.connect(self.Clear)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FlaskProject = QtWidgets.QWidget()
    ui = Ui_FlaskProject()
    FlaskProject.setWindowIcon(QIcon('logo.png'))
    ui.setupUi(FlaskProject)
    FlaskProject.show()
    sys.exit(app.exec_())
